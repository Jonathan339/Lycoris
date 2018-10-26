from setuptools import setup

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup
import sys

basedir = path.dirname(path.abspath(__file__))
extra_args = {}

if (3, 6) > sys.version_info >= (3, 5):
    in_dir = path.join(basedir, 'webdriver')
    out_dir = path.join(basedir, '.webdriver')
    packages = ['webdriver']
    package_dir = {'webdriver': '.webdriver'}
    if not path.exists(out_dir):
        if path.exists(in_dir):
            try:
                from py_backwards.compiler import compile_files
            except ImportError:
                import subprocess
                subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', 'py-backwards']
                )
                from py_backwards.compiler import compile_files
            target = (sys.version_info[0], sys.version_info[1])
            compile_files(in_dir, out_dir, target)
        else:
            raise Exception('Could not find package directory')
else:
    packages = ['webdriver']
    package_dir = {'webdriver': 'webdriver'}


setup(

name=”WebDriver”,
version="0.0.1",
description=”Este paquete descarga los webdrivers de chrome y firefox.”,
author=”Jonathan David Dominguez”,
author_email=”jonathan.d.dominguez@hotmail.com”,
url=””,

scripts=[], # Si queremos integrar scripts dentro del paquete, Ejemplo: scripts[‘script.py’]
packages=packages,
package_dir=package_dir,
#packages=[“driver”,”test”] # Indicar los paquetes que van a formar parte de él, Paquete + Subpaquetes
test_suite='tests'
)