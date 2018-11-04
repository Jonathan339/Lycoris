import logging
from pathlib import Path
import os
from driver.info import InfoChromeDriver
from driver.info import InfoGeckoDriver
import requests
import zipfile
class Driver:

    def __init__(self, driver: str) -> None:
        self.driver = driver
        self.InfoGeckoDriver = InfoGeckoDriver()
        self.InfoChromeDriver = InfoChromeDriver()
        self.download()

    def folder_path(self) -> str:
    	return os.path.normpath(str(Path.home())+'/'+ '.Driver')

    def local_filename(self) -> str:
    	'''return the filename'''
    	return self.InfoChromeDriver.get_link().split('/')[-1]

    def file_path(self) -> str:
    	return os.path.normpath(self.folder_path() + '/' + self.local_filename())

    def extract_file(self):
    	try:
    		zip_file = zipfile.ZipFile(self.file_path())
    		zip_file.extractall(self.folder_path())
    	except Exception as e:
    		logging.warning('[!] Error: {}'.format(e))
    	finally:
    		zip_file.close()
    	return zipfile.ZipFile(self.file_path())

    def download(self) -> None:
        """Downlaod and extract the browser."""
        try:
        	Path(self.folder_path()).mkdir(parents=True, exist_ok=True)
        	if os.path.exists(self.folder_path()):
        		self.download_zip(self.InfoChromeDriver.get_link())
        		self.extract_file()
        except Exception as e:
        	logging.warning('[!] Error: {}'.format(e))
        
    def download_zip(self, url):
        '''Download the driver for Chrome or Gecko.'''
        try:
        	if self.driver == 'chrome' or self.driver == 'CHROME':
        		# NOTE the stream=True parameter
        		r = requests.get(url, stream=True)
        		with open(self.file_path(), 'wb') as f:
        			for chunk in r.iter_content(chunk_size=1024):
        				if chunk: # filter out keep-alive new chunks
        					f.write(chunk)
        		return self.file_path()
        	else:
        		pass
        except Exception as e:
        	logging.warning('[!] Error: {}'.format(e))