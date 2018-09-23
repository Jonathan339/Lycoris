from info import *
import requests
from bs4 import BeautifulSoup
import logging


LINK_GECKODRIVER = 'https://github.com/mozilla/geckodriver/releases'
LINK_CHROMEDDRIVER_LAST_RELASE = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'

headers = {'user-agent' : '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'''}
response = requests.get('https://github.com/mozilla/geckodriver/releases', headers = headers)
#print (response.headers['Content-length'])
soup = BeautifulSoup(response.content, 'lxml')

#print(soup.find('div',{'class':'f1 flex-auto min-width-0 text-normal'}).text)

DOWNLOADS_FOLDER = Path.home() / '.pyppeteer' / 'local-chromium'
DEFAULT_DOWNLOAD_HOST = 'https://storage.googleapis.com'
DOWNLOAD_HOST = os.environ.get(

    'PYPPETEER_DOWNLOAD_HOST', DEFAULT_DOWNLOAD_HOST)
import logging
import os
BASE_URL = f'{DOWNLOAD_HOST}/chromium-browser-snapshots'
logger = logging.getLogger(__name__)
#print(logger)
def get_size(url):
		r = requests.get(url)
		sf = r.headers['Content-Length']
		print(sf)
		kb = 2**10
		mb = 2**20
		gb = 2**30
		tb = 2**40
		if int(sf) >= kb and int(sf) <= mb:
			size_file = round(int(sf) / kb, 1)
		elif int(sf) >= mb and int(sf) <= gb:
			size_file = round(int(sf) / mb, 1)
		elif int(sf) >= gb and int(sf) <= tb:
			size_file = round(int(sf) / gb, 1)
		return size_file



BASE_URL = f'{DOWNLOAD_HOST}/chromium-browser-snapshots'
a = InfoGeckoDrive()
#print(a.info_driver())
print(a.get_system())
print(a.get_version())
print(a.get_link())
print(a.get_name())
print(a.info_driver())

