import logging

import requests
from bs4 import BeautifulSoup
from driver.common.constants import LINK_GECKODRIVER, download_urls_firefox
from driver.common.info import Info

class Firefox(Info):

    def __init__(self, url: str=LINK_GECKODRIVER):
        super().__init__(url)

    def get_name(self) -> str:
        self._name = 'geckodriver'
        return self._name

    def get_version(self)->str:
        try:
            self._version = self.connection().find(
                'div', {'class': 'f1 flex-auto min-width-0 text-normal'}).get_text("/", strip=True)
        except ConnectionError as e:
            logging.warning('[!] Error: {}'.format(e))
        return str(self._version)

    def get_size(self):
        soup = self.connection().find('li',{'class': 'd-block py-1 py-md-2'})
        return soup.find('small', {'class': 'text-gray flex-shrink-0'}).text

    def get_link(self):
        return download_urls_firefox[self.get_system()].format(self.get_version(), self.get_version(), self.get_system())