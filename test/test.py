#---------------------PPadd the file to the path
import sys

from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from driver import Lycoris
from driver import Chrome
from driver import Firefox



print('-------------------------------------')
#print(Windows().browser())
print('-------------------------------------')
#print(Firefox().info_driver())
print('-------------------------------------')
print(Chrome().info_driver())
print('-------------------------------------')
print(Chrome().get_link())
print(Chrome())
print('https://chromedriver.storage.googleapis.com/2.43/chromedriver_win32.zip')
# https://storage.googleapis.com/Win_x64/2.43/chrome-win32.zip
# https://chromedriver.storage.googleapis.com/2.43/chromedriver_win32.zip
print('-------------------------------------')
a = Lycoris('chrome')
print(a.local_filename())
print(a.executable())
print('-------------------------------------')
#b = Lycoris('gecko')

#print(b.file_path())
#print(b.local_filename())
#print(b.executable())
#print(Chrome().info_driver())
#print(Firefox().info_driver())