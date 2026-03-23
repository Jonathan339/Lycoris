import io
import json
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

from driver import Driver
from driver.chrome.chrome import Chrome
from driver.firefox.firefox import Firefox


class DriverTests(unittest.TestCase):
    def test_driver_alias_extends_lycoris_behavior(self):
        manager = Driver('chrome', auto_download=False)
        self.assertEqual(manager.driver, 'chrome')

    def test_executable_uses_platform_mapping(self):
        manager = Driver('chrome', auto_download=False)
        with mock.patch.object(Chrome, 'get_system', return_value='linux64'):
            self.assertTrue(manager.executable().endswith('chromedriver'))

    def test_local_filename_uses_pinned_version_url(self):
        manager = Driver('gecko', version='v0.34.0', auto_download=False)
        with mock.patch.object(Firefox, 'get_system', return_value='linux64'):
            self.assertEqual(manager.local_filename(), 'geckodriver-v0.34.0-linux64.tar.gz')

    def test_download_writes_archive(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = Driver('chrome', auto_download=False, install_dir=tmpdir)
            with mock.patch.object(manager, 'driver_url', return_value='https://example.com/chromedriver.zip'):
                response = mock.Mock()
                response.iter_content.return_value = [b'abc', b'def']
                response.raise_for_status.return_value = None
                with mock.patch('driver.lycoris.requests.get', return_value=response):
                    file_path = manager.download('https://example.com/chromedriver.zip')
                    self.assertEqual(Path(file_path).read_bytes(), b'abcdef')

    def test_install_skips_download_when_binary_exists(self):
        manager = Driver('chrome', auto_download=False)
        with mock.patch.object(manager, 'exists', return_value=True):
            with mock.patch.object(manager, 'write_metadata') as write_metadata:
                with mock.patch.object(manager, 'download') as download:
                    manager.install()
        download.assert_not_called()
        write_metadata.assert_called_once()

    def test_install_forces_download_when_requested(self):
        manager = Driver('chrome', auto_download=False)
        with mock.patch.object(manager, 'exists', return_value=True):
            with mock.patch.object(manager, 'driver_url', return_value='https://example.com/chromedriver.zip'):
                with mock.patch.object(manager, 'download') as download:
                    with mock.patch.object(manager, 'extract_file'):
                        with mock.patch.object(manager, 'write_metadata'):
                            manager.install(force=True)
        download.assert_called_once_with('https://example.com/chromedriver.zip')

    def test_write_metadata_persists_install_info(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = Driver('chrome', version='123.0', auto_download=False, install_dir=tmpdir)
            with mock.patch.object(Chrome, 'get_system', return_value='linux64'):
                with mock.patch.object(manager, 'driver_url', return_value='https://example.com/chromedriver_linux64.zip'):
                    metadata = manager.write_metadata()

            saved = json.loads(Path(manager.metadata_path()).read_text(encoding='utf-8'))
            self.assertEqual(saved['version'], '123.0')
            self.assertEqual(saved['url'], metadata['url'])
            self.assertTrue(saved['executable_path'].endswith('chromedriver'))

    def test_safe_zip_extraction_rejects_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = Driver('chrome', auto_download=False, install_dir=tmpdir)
            archive = Path(tmpdir) / 'malicious.zip'
            with zipfile.ZipFile(archive, 'w') as zip_file:
                zip_file.writestr('../evil.txt', 'bad')
            with self.assertRaises(ValueError):
                manager._safe_extract_zip(str(archive), tmpdir)

    def test_safe_tar_extraction_rejects_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = Driver('gecko', auto_download=False, install_dir=tmpdir)
            archive = Path(tmpdir) / 'malicious.tar.gz'
            with tarfile.open(archive, 'w:gz') as tar:
                data = io.BytesIO(b'bad')
                info = tarfile.TarInfo(name='../evil.txt')
                info.size = len(data.getvalue())
                tar.addfile(info, data)
            with self.assertRaises(ValueError):
                manager._safe_extract_tar(str(archive), tmpdir)

    def test_invalid_driver_raises_value_error(self):
        with self.assertRaises(ValueError):
            Driver('safari', auto_download=False)


if __name__ == '__main__':
    unittest.main()
