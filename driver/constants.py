#--------------last relase---------------------
LINK_GECKODRIVER = 'https://github.com/mozilla/geckodriver/releases'
LINK_CHROMEDDRIVER_LAST_RELASE = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
#-----------------------
from pathlib import Path

DOWNLOADS_FOLDER = Path.home() / '.Driver' / 'local-browser'
#-----------------------
DEFAULT_DOWNLOAD_HOST = 'https://chromedriver.storage.googleapis.com'
downloadURLs = {
	'linux32': f'{DEFAULT_DOWNLOAD_HOST}/'+'{0}'+'/chromedriver_linux32.zip',
	'linux64': f'{DEFAULT_DOWNLOAD_HOST}/'+'{0}'+'/chromedriver_linux64.zip',
	'mac': f'{DEFAULT_DOWNLOAD_HOST}/'+'{0}'+'/chromedriver_mac32.zip',
	'win32': f'{DEFAULT_DOWNLOAD_HOST}/'+'{0}'+'/chromedriver_win32.zip',
	'win64': f'{DEFAULT_DOWNLOAD_HOST}/'+'{0}'+'/chromedriver_win32.zip',
}

#--------------------------------------------------------

