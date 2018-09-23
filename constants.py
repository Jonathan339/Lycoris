#--------------last relase---------------------
LINK_GECKODRIVER = 'https://github.com/mozilla/geckodriver/releases'
LINK_CHROMEDDRIVER_LAST_RELASE = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
#----------------------
from pathlib import Path

DOWNLOADS_FOLDER = Path.home() / '.Driver' / 'local-browser'

DEFAULT_DOWNLOAD_HOST = 'https://storage.googleapis.com'
downloadURLs = {
	'linux64': f'{DEFAULT_DOWNLOAD_HOST}/Linux_x64/'+'{0}'+'/chrome-linux64.zip',
	'mac': f'{DEFAULT_DOWNLOAD_HOST}/Mac/'+'{0}'+'/chrome-mac.zip',
	'win32': f'{DEFAULT_DOWNLOAD_HOST}/Win/'+'{0}'+'/chrome-win32.zip',
	'win64': f'{DEFAULT_DOWNLOAD_HOST}/Win_x64/'+'{0}'+'/chrome-win32.zip',
}

#--------------------------------------------------------

