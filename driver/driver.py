import glob
import logging
import os
import requests
import tarfile
import zipfile

from driver.constants import *
from driver.info import Info
from driver.info import InfoChromeDriver
from driver.info import InfoGeckoDriver
from pathlib import Path


class Driver:

    def __init__(self, driver: str) -> None:
        self.driver = driver
        Path(self.folder_path()).mkdir(parents=True, exist_ok=True)
        self.download_zip()

    def instance_driver(self):
        try:
            if self.driver == 'chrome' or self.driver == 'Chrome' or self.driver == 'CHROME':
                return InfoChromeDriver()
            elif self.driver == 'gecko' or self.driver == 'Gecko' or self.driver == 'GECKO':
                return InfoGeckoDriver()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    def folder_path(self) -> str:
        return os.path.normpath(str(Path.home()) + '/' + '.Driver')

    def local_filename(self) -> str:
        '''return the filename'''
        return self.instance_driver().get_link().split('/')[-1]

    def file_path(self) -> str:
        return os.path.normpath(self.folder_path() + '/' + self.local_filename())

    def excutable(self):
        if self.instance_driver() == InfoChromeDriver():
            return os.path.normpath(chromium_executable[str(self.instance_driver().get_system())].format(self.folder_path()))
        if self.instance_driver() == InfoGeckoDriver():
            return os.path.normpath(firefox_executable[str(self.instance_driver().get_system())].format(self.folder_path()))

    def extract_file(self):
        '''Extract files tar.gz and zip.'''
        try:
            Path(self.folder_path()).mkdir(parents=True, exist_ok=True)
            if os.path.exists(self.folder_path()):
                if self.file_path().endswith('zip'):
                    zip_file = zipfile.ZipFile(self.file_path())
                    zip_file.extractall(self.folder_path())
                    zip_file.close()

                if self.file_path().endswith('tar.gz'):
                    tar = tarfile.open(self.file_path(), "r:gz")
                    tar.extractall(self.folder_path())
                    tar.close()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    def extract_zip(self):
        try:
            if self.file_path().endswith('zip'):
                zip_file = zipfile.ZipFile(self.file_path())
                zip_file.extractall(self.folder_path())
                zip_file.close()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    def extract_tar(self):
        try:
            if os.path.exists(self.folder_path()):
                if self.file_path().endswith('tar.gz'):
                    tar = tarfile.open(self.file_path(), "r:gz")
                    tar.extractall()
                    tar.close()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    def download(self, url):
        try:
            r = requests.get(url, stream=True)
            with open(self.file_path(), 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return self.file_path()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))

    def download_zip(self):
        '''Download the driver for Chrome or Gecko.'''
        try:
            if self.driver == 'chrome' or self.driver == 'Chrome' or self.driver == 'CHROME':
                if os.path.exists(self.folder_path()):
                    self.download(self.instance_driver().get_link())
                    self.extract_file()
            elif self.driver == 'gecko' or self.driver == 'Gecko' or self.driver == 'GECKO':
                if os.path.exists(self.folder_path()):
                    self.download(self.instance_driver().get_link())
                    self.extract_file()
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
