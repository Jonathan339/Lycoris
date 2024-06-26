import logging

import requests

from bs4 import BeautifulSoup
from common import LINK_CHROMEDDRIVER_LAST_RELASE
from common import download_urls_chromium
from common import Info


class Chrome(Info):

    def __init__(self, url: str = LINK_CHROMEDDRIVER_LAST_RELASE):
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
