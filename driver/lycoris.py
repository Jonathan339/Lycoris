import logging
import os
import tarfile
import zipfile
from pathlib import Path

import requests

from common.constants import chromium_executable
from common.constants import firefox_executable
from driver.chrome.chrome import Chrome
from driver.firefox.firefox import Firefox
from driver.resource import Resource


class Lycoris(Resource):
    def __init__(self, driver: str, auto_download: bool = True) -> None:
        self.driver = driver.lower()
        if self.driver not in {'chrome', 'gecko'}:
            raise ValueError("driver must be either 'chrome' or 'gecko'")

        Path(self.folder_path()).mkdir(parents=True, exist_ok=True)
        if auto_download:
            self.download_zip(self.driver_url())

    def instance_driver(self):
        """Return a driver-specific helper instance."""
        if self.driver == 'chrome':
            return Chrome()
        return Firefox()

    def driver_url(self) -> str:
        return self.instance_driver().get_link()

    def executable(self):
        """Return the path of the executable."""
        system = self.instance_driver().get_system()
        executable_map = (
            chromium_executable if self.driver == 'chrome' else firefox_executable
        )
        return os.path.normpath(executable_map[system].format(self.folder_path()))

    def extract_file(self):
        """Extract `.tar.gz` and `.zip` archives into the driver folder."""
        archive_path = self.file_path()
        Path(self.folder_path()).mkdir(parents=True, exist_ok=True)

        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path) as zip_file:
                zip_file.extractall(self.folder_path())
            return

        if archive_path.endswith('.tar.gz'):
            with tarfile.open(archive_path, 'r:gz') as tar:
                tar.extractall(self.folder_path())
            return

        raise ValueError(f'Unsupported archive format: {archive_path}')

    def download(self, url):
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        with open(self.file_path(), 'wb') as file_handle:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file_handle.write(chunk)
        return self.file_path()

    def download_zip(self, url):
        """Download and extract the driver archive for Chrome or Gecko."""
        logging.info('Downloading %s driver from %s', self.driver, url)
        self.download(url)
        self.extract_file()
        return self.file_path()
