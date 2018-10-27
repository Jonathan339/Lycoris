import logging
from pathlib import Path
import os
from driver.download import Download
from driver.info import InfoChromeDriver
from driver.info import InfoGeckoDriver

class Driver:

    def __init__(self, driver: str) -> None:
        self.driver = driver
        self.InfoGeckoDriver = InfoGeckoDriver()
        self.InfoChromeDriver = InfoChromeDriver()
        self.Download = Download()
        self.path = os.path.normpath(str(Path.home()) + '\.Driver')
        self.download()

    def download(self) -> None:
        """Downlaod and extract the browser."""
        extract_zip(self.download_zip(self.InfoChromeDriver.get_url()), self.path)

    def download(self):
        '''Download the driver for Chrome or Gecko.'''
        if self.driver == 'chrome' or self.driver == 'CHROME':
            self.Download.download_zip(self.InfoChromeDriver.get_link())
            
        else:
            self.Download.download_zip(self.InfoGeckoDriver.get_link())

    def extract_zip(self, data: bytes, path: Path) -> None:
        """Extract zipped data to path."""
        if self.curret_platform() == 'mac':
            import subprocess
            import shutil
            zip_path = path
            if not path.exists():
                path.mkdir(parents=True)
                with zip_path.open('wb') as f:
                    f.write(data)
            if not shutil.which('unzip'):
                raise OSError('Failed to automatically extract zip.'
                              f'Please unzip {zip_path} manually.')
                subprocess.run(['unzip', str(zip_path)], cwd=str(path))
            if self.excutable().exists() and zip_path.exists():
                zip_path.unlink()
        else:
            with ZipFile(BytesIO(data)) as zf:
                zf.extractall(str(path))
        exec_path = self.excutable()
        if not exec_path.exists():
            raise IOError('Failed to extract file.')
        exec_path.chmod(exec_path.stat().st_mode | stat.S_IXOTH | stat.S_IXGRP |
                        stat.S_IXUSR)
        logger.warning(f'extracted to: {path}')