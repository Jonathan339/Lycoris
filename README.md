# Driver

The idea is to create an app that downloads the necessary driver either chromium or gecko to facilitate its use.

## Usage

> **Note**: When you run first time, it downloads a recent version of Chromium or Gecko.

**Example**: Get the name of the file and the path of the driver.

```py
from driver.driver import Driver

#Example chrome driver.
a = Driver('chrome')

print(a.local_filename()) # Return the local file name.
print(a.executable()) # Return the path of the driver.

#---------------------------------
#output

chromedriver_win32.zip
C:\Users\x\.driver\chromedriver.exe

#----------------------------------
#Example firefox driver.
b = Driver('gecko')
print(b.file_path())
print(b.local_filename())
print(b.executable())
#-----------------------------------
#output

C:\Users\x\.driver\geckodriver-v0.23.0-win64.zip
geckodriver-v0.23.0-win64.zip
C:\Users\x\.driver\geckodriver.exe

```