import logging
import requests
from bs4 import BeautifulSoup
from driver import *
from info import *
from pathlib import Path

print(str(Path.home()) +'\.Driver')

a = Driver('chrome')
print(a.download())