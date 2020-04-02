import json
import subprocess


class Server:

    def __init__(self):
        self.process = ""

    def open_server(self, driver, port=5050):
        if str.lower(driver) == "chrome" or str.lower(driver) == "gecko":
            self.process = subprocess.Popen(driver + "--port=" + port)

    def close_server(self):
        self.process.terminate()
