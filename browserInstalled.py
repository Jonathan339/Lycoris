from winreg import HKEY_LOCAL_MACHINE, OpenKey, ConnectRegistry, EnumKey,QueryInfoKey

browser_name = ['Opera Software', 'Mozilla', 'Google']

class RegWindows:
    
    def __init__(self) -> None:
        self.reg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        
    def openkey(self):
        """Open the key registry"""
        akey = OpenKey(self.reg, r"SOFTWARE")
        return akey
    
    def list_programs(self) -> list:
        """
        Devuelve una lista de aplicaciones instaladas
        """
        self.lista_apps=[]
        for i in range(0, QueryInfoKey(self.openkey())[0]):
            self.lista_apps.append(EnumKey(self.openkey(), i))
            #print  (EnumKey(self.openkey(), i))
        return self.lista_apps

    def browser_installed(self):
        '''
        Devuelve una lista de los navegadores instalados.
        '''
        nav = []
        for browser in self.list_programs():
            if browser in browser_name:
                nav.append(browser)
        return nav

        
if __name__ == '__main__':
    c = RegWindows()
    #print(c.ListaApps())
    print(c.browser_installed())