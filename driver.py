from info import InfoGeckoDriver, InfoChromeDriver, Info
from download import Download
import logging
from pathlib import Path



class Driver:
	def __init__(self):
		self.InfoGeckoDriver = InfoGeckoDriver()
		self.InfoChromeDriver = InfoChromeDriver()
		self.Download = Download ()
		self.path = Path.home() + '/.Driver'
		self.instance()

	def instance(self):
		if isinstance(self.InfoGeckoDriver):
			self.Download.download_zip(self.InfoGeckoDriver.get_link())
		else:
			self.Download.download_zip(self.InfoChromeDriver.get_link())



