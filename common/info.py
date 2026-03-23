import logging
import platform
import sys

import requests
from bs4 import BeautifulSoup

REQUEST_TIMEOUT_SECONDS = 15
DEFAULT_HEADERS = {
    'user-agent': (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    )
}


class Info:
    def __init__(self, url: str):
        self._url = url
        self._name = None
        self._version = None
        self._link = None
        self._size = None
        self._driver_data = {}

    def connection(self):
        """Connect to the website and return a parsed HTML document."""
        response = requests.get(
            self._url,
            headers=DEFAULT_HEADERS,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return BeautifulSoup(response.content, 'lxml')

    def match(self, filter: str, other: str) -> bool:
        return filter in other

    def get_size(self, filename=None) -> int:
        """Get size of the file in bytes."""
        if filename:
            try:
                import os

                st = os.stat(filename)
                self._size = st.st_size
            except OSError as exc:
                logging.warning('[!] Error: %s', exc)
            return self._size
        return self._size

    def get_system(self) -> str:
        machine = platform.machine().lower()
        is_64_bit = machine in {'x86_64', 'amd64', 'arm64', 'aarch64'} or sys.maxsize > 2**31 - 1

        if sys.platform.startswith('linux'):
            return 'linux64' if is_64_bit else 'linux32'
        if sys.platform.startswith('darwin'):
            return 'mac64'
        if sys.platform.startswith('win'):
            return 'win64' if is_64_bit else 'win32'

        raise RuntimeError(f'Unsupported platform: {sys.platform}')

    def info_driver(self) -> dict:
        self._driver_data = {
            'Name': self.get_name(),
            'Version': self.get_version(),
            'Link': self.get_link(),
            'System': self.get_system(),
        }
        return self._driver_data
