import logging

from common.constants import LINK_GECKODRIVER
from common.constants import download_urls_firefox
from common.info import Info


class Firefox(Info):

    def __init__(self, url: str = LINK_GECKODRIVER):
        super().__init__(url)

    def get_name(self) -> str:
        self._name = 'geckodriver'
        return self._name

    def get_version(self) -> str:
        try:
            self._version = self.connection().find(
                'span', {'class': 'css-truncate-target'}).get_text()
        except ConnectionError as e:
            logging.warning('[!] Error: {}'.format(e))
        return str(self._version)

    def get_size(self):
        soup = self.connection().find('li', {'class': 'd-block py-1 py-md-2'})
        return soup.find('small', {'class': 'text-gray flex-shrink-0'}).text

    def get_link(self):
        return download_urls_firefox[self.get_system()].format(self.get_version(), self.get_version(),
                                                               self.get_system())
