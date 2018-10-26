#-----------------------------
# add the file to the path
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))

#--------------------------

from driver.regedit import *

print(Registry_windows().ListaApps())
#print(InfoChromeDriver())