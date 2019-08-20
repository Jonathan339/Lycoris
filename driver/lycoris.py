import logging
import os
import tarfile
import zipfile
from pathlib import Path

import requests

from driver.common.constants import *
from driver.common.info import InfoChromeDriver
from driver.common.info import InfoGeckoDriver


class Lycoris:

    def __init__(self, driver: str) -> None:
        self.driver = driver
        Path(self.folder_path).mkdir(parents=True, exist_ok=True)
        self.download_zip()

    @property
    def instance_driver(self) -> "Instanced driver":
        """Return the instance of driver."""
        try:
            if self.driver == 'chrome' or self.driver == 'Chrome' or self.driver == 'CHROME':
                return InfoChromeDriver()
            elif self.driver == 'gecko' or self.driver == 'Gecko' or self.driver == 'GECKO':
                return InfoGeckoDriver()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    @property
    def folder_path(self) -> str:
        return os.path.normpath(str(Path.home()) + '/' + '.driver')

    @property
    def local_filename(self) -> str:
        """ Return the file name."""
        return self.instance_driver.get_link().split('/')[-1]

    @property
    def file_path(self) -> str:
        """ Returns the path of the file."""
        return os.path.normpath(self.folder_path + '/' + self.local_filename)

    def executable(self):
        """ Return the path of the executable."""
        if str(self.instance_driver.__class__.__name__) == 'InfoChromeDriver':
            return os.path.normpath(
                chromium_executable[str(self.instance_driver.get_system())].format(self.folder_path))
        else:
            return os.path.normpath(
                firefox_executable[str(self.instance_driver.get_system())].format(self.folder_path))

    def extract_file(self):
        """ Extract files tar.gz and zip."""
        try:
            Path(self.folder_path).mkdir(parents=True, exist_ok=True)
            if os.path.exists(self.folder_path):
                if self.file_path.endswith('zip'):
                    zip_file = zipfile.ZipFile(self.file_path)
                    zip_file.extractall(self.folder_path)
                    zip_file.close()

                if self.file_path.endswith('tar.gz'):
                    tar = tarfile.open(self.file_path, "r:gz")
                    tar.extractall(self.folder_path)
                    tar.close()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    def download(self, url):
        try:
            r = requests.get(url, stream=True)
            with open(self.file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return self.file_path
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    def download_zip(self):
        """Download the driver for Chrome or Gecko."""
        try:
            if self.driver == 'chrome' or self.driver == 'Chrome' or self.driver == 'CHROME':
                if os.path.exists(self.folder_path):
                    logging.warning('This takes a mule, thanks for waiting.')
                    self.download(self.instance_driver.get_link())
                    self.extract_file()
            elif self.driver == 'gecko' or self.driver == 'Gecko' or self.driver == 'GECKO':
                if os.path.exists(self.folder_path):
                    logging.warning('This takes a mule, thanks for waiting.')
                    self.download(self.instance_driver.get_link())
                    self.extract_file()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
