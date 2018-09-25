import logging
from download import Download
from info import InfoChromeDriver
from info import InfoGeckoDriver
from pathlib import Path


class Driver:

    def __init__(self, driver: str) -> None:
        self.driver = driver
        self.InfoGeckoDriver = InfoGeckoDriver()
        self.InfoChromeDriver = InfoChromeDriver()
        self.Download = Download()
        self.path = str(Path.home()) + '\.Driver'
        self.download()

    def download(self):
        '''Download the driver for Chrome or Gecko.'''
        if self.driver == 'chrome' or self.driver == 'CHROME':
            self.Download.download_zip(self.InfoChromeDriver.get_link())
            
        else:
            self.Download.download_zip(self.InfoGeckoDriver.get_link())
