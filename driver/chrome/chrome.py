import logging

import requests

from common.constants import LINK_CHROMEDRIVER_LATEST_RELEASE
from common.constants import download_urls_chromium
from common.info import Info
from common.info import REQUEST_TIMEOUT_SECONDS


class Chrome(Info):
    def __init__(self, url: str = LINK_CHROMEDRIVER_LATEST_RELEASE):
        super().__init__(url)

    def get_name(self) -> str:
        self._name = 'chromedriver'
        return self._name

    def get_version(self) -> str:
        try:
            response = requests.get(self._url, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()
            self._version = response.text.strip()
        except requests.RequestException as exc:
            logging.warning('[!] Error: %s', exc)
            raise
        return self._version

    def get_link(self) -> str:
        return download_urls_chromium[self.get_system()].format(self.get_version())
