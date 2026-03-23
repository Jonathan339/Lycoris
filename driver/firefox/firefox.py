import logging

import requests

from common.constants import LINK_GECKODRIVER
from common.constants import download_urls_firefox
from common.info import Info
from common.info import REQUEST_TIMEOUT_SECONDS


class Firefox(Info):
    def __init__(self, url: str = LINK_GECKODRIVER):
        super().__init__(url)

    def get_name(self) -> str:
        self._name = 'geckodriver'
        return self._name

    def get_version(self) -> str:
        try:
            latest_release = requests.get(
                self._url,
                allow_redirects=True,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
            latest_release.raise_for_status()
            self._version = latest_release.url.rstrip('/').split('/')[-1]
        except requests.RequestException as exc:
            logging.warning('[!] Error: %s', exc)
            raise
        return str(self._version)

    def get_size(self):
        soup = self.connection().find('li', {'class': 'd-block py-1 py-md-2'})
        if not soup:
            return None
        size = soup.find('small', {'class': 'text-gray flex-shrink-0'})
        return size.text if size else None

    def get_link(self, version: str | None = None):
        resolved_version = self.resolve_version(version)
        system = self.get_system()
        return download_urls_firefox[system].format(
            resolved_version,
            resolved_version,
            system,
        )
