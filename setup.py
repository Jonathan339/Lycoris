from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent
README = (BASE_DIR / 'README.md').read_text(encoding='utf-8')

setup(
    name='lycoris-driver',
    version='0.2.0',
    description='Download and expose ChromeDriver and GeckoDriver executables.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Jonathan David Dominguez',
    packages=find_packages(exclude=('test', 'tests')),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4>=4.8',
        'lxml>=4.6',
        'requests>=2.23',
    ],
    python_requires='>=3.10',
)
