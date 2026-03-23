import os
from pathlib import Path


class Resource:
    def folder_path(self) -> str:
        return os.path.normpath(str(Path.home() / '.driver'))

    def local_filename(self) -> str:
        """Return the local archive file name for the resolved driver."""
        return self.instance_driver().get_link().split('/')[-1]

    def file_path(self) -> str:
        """Return the local path of the downloaded archive."""
        return os.path.normpath(os.path.join(self.folder_path(), self.local_filename()))


# Backwards compatible alias for the original public name.
resource = Resource
