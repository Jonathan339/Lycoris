
class Connection:

    def __init__(self, url):
        super(Connection, self).__init__()
        self._url = url
        self._header = {}

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @url.deleter
    def del_url(self, arg):
        del self._url

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, key, value):
        self._header[key] = value

    @header.deleter
    def header(self, key):
        self._header.pop(key)