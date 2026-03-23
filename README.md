# Lycoris Driver

Lycoris is a small Python package that downloads the browser driver you need
(`chromedriver` or `geckodriver`) and returns the local executable path.

## Features

- Detects the current operating system.
- Resolves the latest ChromeDriver or GeckoDriver download URL.
- Lets you pin an explicit driver version when you need reproducible installs.
- Downloads the archive into `~/.driver` by default.
- Skips re-downloading when the executable already exists, unless you force it.
- Extracts archives with path-validation safeguards.
- Persists installation metadata in a JSON file for each driver.

## Installation

```bash
pip install .
```

## Usage

> **Note**: The first time you create a driver manager it downloads the latest
> supported archive for your platform.

```python
from driver import Driver

chrome = Driver('chrome')
print(chrome.local_filename())
print(chrome.executable())
print(chrome.installed_version())
```

### Pin a specific version

```python
from driver import Driver

chrome = Driver('chrome', version='114.0.5735.90')
print(chrome.archive_path())
print(chrome.executable())
```

### Inspect metadata without downloading immediately

```python
from driver import Lycoris

manager = Lycoris('gecko', auto_download=False)
print(manager.driver_url())
print(manager.metadata_path())
```

### Force a fresh download

```python
from driver import Driver

manager = Driver('chrome', auto_download=False)
manager.install(force=True)
```

## Running tests

```bash
python -m unittest discover -s test -p 'test*.py'
```
