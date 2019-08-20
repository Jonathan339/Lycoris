import platform
import sys
import logging


def match(_filter: str, other: str) -> bool:
    return _filter in other


def get_size(filename=None) -> int:
    """ Get size of the file in bytes."""
    size = None
    if filename:
        try:
            import os
            st = os.stat(filename)
            size = st.st_size
        except Exception as e:
            logging.warning('[!] Error: {}'.format(e))
        return size
    else:
        size


def get_system() -> str:
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
