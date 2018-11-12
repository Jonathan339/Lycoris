#--------------last relase---------------------
LINK_GECKODRIVER = 'https://github.com/mozilla/geckodriver/releases'
LINK_CHROMEDDRIVER_LAST_RELASE = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'

#-------------------------------------------------------

DEFAULT_DOWNLOAD_HOST_GITHUB = 'https://github.com/mozilla/geckodriver/releases/download'
download_urls_firefox = {
    'linux32': f'{DEFAULT_DOWNLOAD_HOST_GITHUB}/' + '{}' + '/geckodriver-{}-{}.tar.gz',
    'linux64': f'{DEFAULT_DOWNLOAD_HOST_GITHUB}/' + '{}' + '/geckodriver-{}-{}.tar.gz',
    'mac': f'{DEFAULT_DOWNLOAD_HOST_GITHUB}/' + '{}' + '/geckodriver-{}-{}.tar.gz',
    'win32': f'{DEFAULT_DOWNLOAD_HOST_GITHUB}/' + '{}' + '/geckodriver-{}-{}.zip',
    'win64': f'{DEFAULT_DOWNLOAD_HOST_GITHUB}/' + '{}' + '/geckodriver-{}-{}.zip',
}
#-------------------------------------------------------
DEFAULT_DOWNLOAD_HOST = 'https://chromedriver.storage.googleapis.com'
download_urls_chromium = {
    'linux32': f'{DEFAULT_DOWNLOAD_HOST}/' + '{0}' + '/chromedriver_linux32.zip',
    'linux64': f'{DEFAULT_DOWNLOAD_HOST}/' + '{0}' + '/chromedriver_linux64.zip',
    'mac': f'{DEFAULT_DOWNLOAD_HOST}/' + '{0}' + '/chromedriver_mac32.zip',
    'win32': f'{DEFAULT_DOWNLOAD_HOST}/' + '{0}' + '/chromedriver_win32.zip',
    'win64': f'{DEFAULT_DOWNLOAD_HOST}/' + '{0}' + '/chromedriver_win32.zip',
}

#--------------------------------------------------------

chromium_executable = {
    'linux32': "{}/chromedriver",
    'linux64': "{}/chromedriver",
    'mac64': "({}/chrome-mac/Chromium.app/Contents/MacOS/Chromium)",
    'win64': "{}/chromedriver.exe"
}
#---------------------------------------------------------

firefox_executable = {
    'linux32': "{}/geckodriver",
    'linux64': "{}/geckodriver",
    'mac64': "({}/firefox-mac/Firefox.app/Contents/MacOS/Firefox)",
    'win64': "{}/geckodriver.exe"
}
