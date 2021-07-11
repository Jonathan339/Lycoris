from pathlib import Path


class resource:

    def __init__(self, resource_path):
        self.resource_path = resource_path
    
    def run(self):
        pass

    def folder_path(self) -> str:
        return os.path.normpath(str(Path.home()) + '/' + '.driver')
    
    def local_filename(self) -> str:
        """ Return the file name."""
        return self.instance_driver().get_link().split('/')[-1]

    def file_path(self) -> str:
        """ Returns the path of the file."""
        return os.path.normpath(self.folder_path() + '/' + self.local_filename())