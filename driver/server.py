import json
import subprocess


class Server:

    def __init__(self):
        self.process = ""

    def start_server(self, driver, port=5050):
        if str.lower(driver) == "chrome" or str.lower(driver) == "gecko":
            self.process = subprocess.Popen(driver + "--port=" + port)

    def kill_server(self):
        self.process.terminate()
