# Lycoris Driver

Lycoris is a small Python package that downloads the browser driver you need
(`chromedriver` or `geckodriver`) and returns the local executable path.

## Features

- Detects the current operating system.
- Resolves the latest ChromeDriver or GeckoDriver download URL.
- Downloads the archive into `~/.driver`.
- Extracts the archive automatically.
- Exposes the archive name and executable path.

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

firefox = Driver('gecko')
print(firefox.local_filename())
print(firefox.executable())
```

If you want to inspect metadata without downloading the archive immediately,
you can disable the automatic download.

```python
from driver import Lycoris

manager = Lycoris('chrome', auto_download=False)
print(manager.driver_url())
```

## Running tests

```bash
python -m unittest discover -s test -p 'test*.py'
```
