import logging
import os
import stat
import sys
from constants import *
from info import *
from io import BytesIO
from pathlib import Path
from urllib import request
from zipfile import ZipFile


class Download:

    def download_zip(self, url: str) -> bytes:
        """Download data from url."""
        logger.warning('start download.\n'
            'Download may take a few minutes.')
        with request.urlopen(url) as f:
            data = f.read()
            logger.warning('Download done.')
            return data

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

    def download(self) -> None:
        """Downlaod and extract the browser."""
        extract_zip(self.download_zip(self.get_url()), DOWNLOADS_FOLDER / VERSION)

    def excutable(self) -> Path:
        """Get path of the executable."""
        return Executable[self.get_system()]

    def check(self) -> bool:
        """Check if browser is placed at correct path."""
        return self.excutable().exists()
