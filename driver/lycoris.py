import json
import logging
import os
import shutil
import tarfile
import tempfile
import zipfile
from pathlib import Path

import requests

from common.constants import chromium_executable
from common.constants import firefox_executable
from driver.chrome.chrome import Chrome
from driver.firefox.firefox import Firefox
from driver.resource import Resource


class Lycoris(Resource):
    def __init__(
        self,
        driver: str,
        version: str | None = None,
        auto_download: bool = True,
        force_download: bool = False,
        install_dir: str | None = None,
    ) -> None:
        self.driver = driver.lower()
        if self.driver not in {'chrome', 'gecko'}:
            raise ValueError("driver must be either 'chrome' or 'gecko'")

        self.version = version
        self.force_download = force_download
        self.install_dir = install_dir
        self._driver_instance = None
        self._resolved_url = None

        Path(self.folder_path()).mkdir(parents=True, exist_ok=True)
        if auto_download:
            self.install(force=self.force_download)

    def instance_driver(self):
        """Return a driver-specific helper instance."""
        if self._driver_instance is None:
            self._driver_instance = Chrome() if self.driver == 'chrome' else Firefox()
        return self._driver_instance

    def driver_url(self) -> str:
        if self._resolved_url is None:
            self._resolved_url = self.instance_driver().get_link(self.version)
        return self._resolved_url

    def executable(self):
        """Return the path of the executable."""
        system = self.instance_driver().get_system()
        executable_map = (
            chromium_executable if self.driver == 'chrome' else firefox_executable
        )
        return os.path.normpath(executable_map[system].format(self.folder_path()))

    def installed_version(self):
        return self.metadata().get('version')

    def exists(self) -> bool:
        return self.executable_exists()

    def should_download(self, force: bool = False) -> bool:
        if force:
            return True

        if not self.exists():
            return True

        metadata = self.metadata()
        if self.version and metadata.get('version') != self.version:
            return True

        return False

    def _safe_extract_zip(self, archive_path: str, destination: str) -> None:
        with zipfile.ZipFile(archive_path) as zip_file:
            for member in zip_file.infolist():
                member_path = os.path.abspath(os.path.join(destination, member.filename))
                if not member_path.startswith(os.path.abspath(destination) + os.sep):
                    raise ValueError(f'Unsafe zip member: {member.filename}')
            zip_file.extractall(destination)

    def _safe_extract_tar(self, archive_path: str, destination: str) -> None:
        with tarfile.open(archive_path, 'r:gz') as tar:
            for member in tar.getmembers():
                member_path = os.path.abspath(os.path.join(destination, member.name))
                if not member_path.startswith(os.path.abspath(destination) + os.sep):
                    raise ValueError(f'Unsafe tar member: {member.name}')
            tar.extractall(destination)

    def _promote_extracted_files(self, source_dir: str) -> None:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            destination_path = os.path.join(self.folder_path(), item)
            if os.path.exists(destination_path):
                if os.path.isdir(destination_path):
                    shutil.rmtree(destination_path)
                else:
                    os.remove(destination_path)
            shutil.move(source_path, destination_path)

    def extract_file(self):
        """Extract `.tar.gz` and `.zip` archives into the driver folder."""
        archive_path = self.archive_path()
        Path(self.folder_path()).mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory(dir=self.folder_path()) as temp_dir:
            if archive_path.endswith('.zip'):
                self._safe_extract_zip(archive_path, temp_dir)
            elif archive_path.endswith('.tar.gz'):
                self._safe_extract_tar(archive_path, temp_dir)
            else:
                raise ValueError(f'Unsupported archive format: {archive_path}')
            self._promote_extracted_files(temp_dir)

    def download(self, url):
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        with open(self.archive_path(), 'wb') as file_handle:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file_handle.write(chunk)
        return self.archive_path()

    def write_metadata(self):
        payload = {
            'driver': self.driver,
            'version': self.instance_driver().resolve_version(self.version),
            'url': self.driver_url(),
            'archive_path': self.archive_path(),
            'executable_path': self.executable(),
        }
        Path(self.metadata_path()).write_text(json.dumps(payload, indent=2), encoding='utf-8')
        return payload

    def install(self, force: bool = False):
        should_download = self.should_download(force=force)
        if should_download:
            logging.info('Downloading %s driver from %s', self.driver, self.driver_url())
            self.download(self.driver_url())
            self.extract_file()
        self.write_metadata()
        return self.executable()

    def download_zip(self, url):
        """Backwards-compatible wrapper around the install flow."""
        self._resolved_url = url
        return self.install(force=True)
