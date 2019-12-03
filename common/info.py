import logging
import platform
import sys
import requests
from bs4 import BeautifulSoup


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
                'user-agent': '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'''}
            response = requests.get(self._url, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
        return soup


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

    def info_driver(self) -> dict:
        self._driver_data = {'Name: ': self.get_name(),
                             'Version: ': self.get_version(),
                             'Link: ': self.get_link(),
                             # 'Size: ': self.get_size(),
                             'System: ': self.get_system()}
        return self._driver_data




