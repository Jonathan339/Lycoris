import math
import logging 
from winreg import HKEY_LOCAL_MACHINE, OpenKey, ConnectRegistry, EnumKey,QueryInfoKey

class Registry_windows:
    
    def __init__(self):
        self.reg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        self.browser = ['Opera Software', 'Mozilla', 'Google']
        
    def openkey(self):
        """Open the key registry"""
        #akey = OpenKey(self.reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        akey = OpenKey(self.reg, r"SOFTWARE")
        return akey
    
    def ListaApps(self) -> list:
        """devuelve una lista de aplicaciones instaladas"""
        self.lista_apps=[]
        for i in range(0, QueryInfoKey(self.openkey())[0]):
            self.lista_apps.append(EnumKey(self.openkey(), i))
            #print  (EnumKey(self.openkey(), i))
        return self.lista_apps
                    
    def equal(self, otro):
        if self.browser.__eq__(otro): 
            return  True 
        else: 
            return False
            
    def __str__(self):
        return self.ListaApps()
                   
        
if __name__ == '__main__':
    c = Registry_windows()
    print(c.ListaApps())