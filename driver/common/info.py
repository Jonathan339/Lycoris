import logging
import platform
import sys

import requests
from bs4 import BeautifulSoup

from driver.common.constants import *





class Info:

    def __init__(self, url: str):
        self._url = url
        self._name = None
        self._version = None
        self._link = None
        self._size = None
        self._driver_data = {}

    def connection(self):
        '''Connect to the website'''
        try:
            headers = {
                'user-agent': '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu 
                Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'''}
            response = requests.get(self._url, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
        return soup



    def info_driver(self) -> dict:
        self._driver_data = {'Name: ': self.get_name(),
                             'Version: ': self.get_version(),
                             'Link: ': self.get_link(),
                             'Size: ': self.get_size(),
                             'System: ': self.get_system()}
        return self._driver_data


class InfoGeckoDriver(Info):

    def __init__(self, url: str = LINK_GECKODRIVER):
        super().__init__(url)

    def get_name(self) -> str:
        self._name = 'geckodriver'
        return self._name

    def get_version(self) -> str:
        try:
            self._version = self.connection().find(
                'div', {'class': 'f1 flex-auto min-width-0 text-normal'}).get_text("/", strip=True)
        except ConnectionError as e:
            logging.warning('[!] Error: {}'.format(e))
        return str(self._version)

    # def get_size(self):
    #   soup = self.connection().find('li',{'class': 'd-block py-1 py-md-2'})
    #   return soup.find('small', {'class': 'text-gray flex-shrink-0'}).text

    def get_link(self):
        return download_urls_firefox[self.get_system()].format(self.get_version(), self.get_version(),
                                                               self.get_system())


class InfoChromeDriver(Info):

    def __init__(self, url=LINK_CHROMEDDRIVER_LAST_RELASE):
        super().__init__(url)

    def get_name(self) -> str:
        self._name = 'chromedriver'
        return self._name

    def get_version(self) -> str:
        try:
            response = requests.get(self._url)
            soup = BeautifulSoup(response.content, 'lxml')
            self._version = soup.get_text(strip=True)
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
        return self._version

    def get_link(self) -> str:
        return download_urls_chromium[self.get_system()].format(self.get_version())
