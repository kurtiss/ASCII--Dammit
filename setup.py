#!/usr/bin/env python
# encoding: utf-8
"""
setup.py
"""

from setuptools import setup, find_packages
import os

execfile(os.path.join('src', 'AsciiDammit', 'version.py'))

setup(
    name = 'AsciiDammit',
    version = VERSION,
    description = 'Stupid library to turn MS chars (like smart quotes) and ISO-Latin chars into ASCII, dammit.',
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = 'https://github.com/kurtiss/ASCII--Dammit',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires = [],
    zip_safe = False
)