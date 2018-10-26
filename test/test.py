#-----------------------------
# add the file to the path
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))

#--------------------------

from driver.regedit import Registry_windows
from driver.browserInstalled import Windows
from driver.info import Info, InfoChromeDriver, InfoGeckoDriver


print(Registry_windows().ListaApps())
print('-------------------------------------')
print(Windows().browser())
print('-------------------------------------')
print(InfoGeckoDriver().info_driver())
print('-------------------------------------')
print(InfoChromeDriver().info_driver())
print('-------------------------------------')
