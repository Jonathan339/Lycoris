import json
import subprocess

class Server:
    def __init__(self):
        self.process = ""

    def start_server(self, driver, port=5050):
        # Se verifica que el driver proporcionado sea válido
        if str.lower(driver) == "chrome" or str.lower(driver) == "gecko":
            # Se inicia el servidor utilizando el driver y el puerto especificado
            self.process = subprocess.Popen(driver + "--port=" + port)

    def kill_server(self):
        # Se detiene el proceso del servidor
        self.process.terminate()
