import logging
from download import Download
from info import InfoChromeDriver
from info import InfoGeckoDriver
from pathlib import Path
import os


class Driver:

    def __init__(self, driver: str) -> None:
        self.driver = driver
        self.InfoGeckoDriver = InfoGeckoDriver()
        self.InfoChromeDriver = InfoChromeDriver()
        self.Download = Download()
        self.path = os.path.normpath(str(Path.home()) + '\.Driver')
        self.download()

    def download(self):
        if isinstance(InfoGeckoDriver(), __class__):
            self.Download.download_zip(self.InfoChromeDriver.get_link())
            
        else:
            self.Download.download_zip(self.InfoGeckoDriver.get_link())

    def download2(self):
        '''Download the driver for Chrome or Gecko.'''
        if self.driver == 'chrome' or self.driver == 'CHROME':
            self.Download.download_zip(self.InfoChromeDriver.get_link())
            
        else:
            self.Download.download_zip(self.InfoGeckoDriver.get_link())

a = Driver('chrome')
