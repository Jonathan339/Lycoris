import tempfile
import unittest
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

    def test_local_filename_uses_driver_link(self):
        manager = Driver('gecko', auto_download=False)
        with mock.patch.object(Firefox, 'get_link', return_value='https://example.com/geckodriver.zip'):
            self.assertEqual(manager.local_filename(), 'geckodriver.zip')

    def test_download_writes_archive(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = Driver('chrome', auto_download=False)
            with mock.patch.object(manager, 'folder_path', return_value=tmpdir):
                with mock.patch.object(manager, 'local_filename', return_value='chromedriver.zip'):
                    response = mock.Mock()
                    response.iter_content.return_value = [b'abc', b'def']
                    response.raise_for_status.return_value = None
                    with mock.patch('driver.lycoris.requests.get', return_value=response):
                        file_path = manager.download('https://example.com/chromedriver.zip')
                        self.assertEqual(Path(file_path).read_bytes(), b'abcdef')

    def test_invalid_driver_raises_value_error(self):
        with self.assertRaises(ValueError):
            Driver('safari', auto_download=False)


if __name__ == '__main__':
    unittest.main()
