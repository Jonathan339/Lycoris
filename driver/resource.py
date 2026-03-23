import json
import os
from pathlib import Path


class Resource:
    def folder_path(self) -> str:
        base_path = Path(self.install_dir) if getattr(self, 'install_dir', None) else Path.home() / '.driver'
        return os.path.normpath(str(base_path))

    def archive_path(self) -> str:
        """Return the local path of the downloaded archive."""
        return os.path.normpath(os.path.join(self.folder_path(), self.local_filename()))

    def file_path(self) -> str:
        """Backwards-compatible alias for the archive path."""
        return self.archive_path()

    def metadata_path(self) -> str:
        return os.path.normpath(os.path.join(self.folder_path(), f'{self.driver}.json'))

    def local_filename(self) -> str:
        """Return the local archive file name for the resolved driver."""
        return self.driver_url().split('/')[-1]

    def executable_exists(self) -> bool:
        return os.path.exists(self.executable())

    def metadata(self):
        metadata_file = Path(self.metadata_path())
        if not metadata_file.exists():
            return {}
        return json.loads(metadata_file.read_text(encoding='utf-8'))


# Backwards compatible alias for the original public name.
resource = Resource
