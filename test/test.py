#-----------------------------
# add the file to the path
import sys

from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))

#--------------------------

from driver.driver import Driver
from driver.info import Info
from driver.info import InfoChromeDriver
from driver.info import InfoGeckoDriver

print('-------------------------------------')
#print(Windows().browser())
print('-------------------------------------')
print(InfoGeckoDriver().info_driver())
print('-------------------------------------')
print(InfoChromeDriver().info_driver())
print('-------------------------------------')
print(InfoChromeDriver().get_link())
print(InfoChromeDriver())
print('https://chromedriver.storage.googleapis.com/2.43/chromedriver_win32.zip')
# https://storage.googleapis.com/Win_x64/2.43/chrome-win32.zip
# https://chromedriver.storage.googleapis.com/2.43/chromedriver_win32.zip
print('-------------------------------------')
a = Driver('chrome')
print(a.local_filename())
print(a.executable())
print('-------------------------------------')
b = Driver('gecko')

print(b.file_path())
print(b.local_filename())
print(b.executable())
