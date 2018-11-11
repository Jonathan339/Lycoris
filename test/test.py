#-----------------------------
# add the file to the path
import sys

from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))

#--------------------------

from driver.browserInstalled import Windows
from driver.driver import Driver
from driver.info import Info
from driver.info import InfoChromeDriver
from driver.info import InfoGeckoDriver
from driver.regedit import Registry_windows

print(Registry_windows().ListaApps())
print('-------------------------------------')
print(Windows().browser())
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
a = Driver('chrome')
a.excutable()

b = Driver('gecko')
