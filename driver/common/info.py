import logging
import platform
import sys
<<<<<<< HEAD

import requests
from bs4 import BeautifulSoup

from driver.common.constants import *





=======
import requests
from bs4 import BeautifulSoup
from driver.common.constants import *

>>>>>>> created packeges chrome and firefox.
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
<<<<<<< HEAD
                'user-agent': '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu 
                Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'''}
=======
                'user-agent': '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'''}
>>>>>>> created packeges chrome and firefox.
            response = requests.get(self._url, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
        return soup


<<<<<<< HEAD
=======
    def match(self,  filter: str, other: str) -> str:
        return filter in other

    def get_size(self, filename=None) -> int:
        """ Get size of the file in bytes."""
        if filename:
            try:
                import os
                st = os.stat(filename)
                self._size = st.st_size
            except Exception as e:
                logging.warning('[!] Error: {}'.format(e))
            return self._size
        else:
            self._size

    def get_system(self) -> str:
        try:
            if sys.platform.startswith('linux'):
                if platform.processor() == 'x86_64':
                    return 'linux64'
                else:
                    return 'linux32'
            elif sys.platform.startswith('darwin'):
                return 'mac64'
            elif sys.platform.startswith('win'):
                if sys.maxsize > 2 ** 31 - 1:
                    return 'win64'
                return 'win32'
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
>>>>>>> created packeges chrome and firefox.

    def info_driver(self) -> dict:
        self._driver_data = {'Name: ': self.get_name(),
                             'Version: ': self.get_version(),
                             'Link: ': self.get_link(),
<<<<<<< HEAD
                             'Size: ': self.get_size(),
=======
                             # 'Size: ': self.get_size(),
>>>>>>> created packeges chrome and firefox.
                             'System: ': self.get_system()}
        return self._driver_data


<<<<<<< HEAD
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
=======


>>>>>>> created packeges chrome and firefox.
