import subprocess


class Server:
    def __init__(self):
        self.process = None

    def start_server(self, driver, port=5050):
        driver_name = str(driver).lower()
        if driver_name in {'chrome', 'gecko'}:
            self.process = subprocess.Popen([driver_name, f'--port={port}'])
            return self.process
        raise ValueError("driver must be either 'chrome' or 'gecko'")

    def kill_server(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None
