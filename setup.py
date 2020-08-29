#!/usr/bin/env python

from os import path

import setuptools

root = path.abspath(path.dirname(__file__))


def read_files(filename):
    with open(path.join(root, filename), 'r', encoding='utf-8') as f:
        data = f.read()
        return data


classifiers = [
    'Development Status :: 2 - Pre-Alpha',

    'Programming Language :: Python :: 3',

    'License :: OSI Approved :: MIT License',

    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',

    'Topic :: Database :: Database Engines/Servers',
]


setuptools.setup(
    name='Zadigo',
    version=exec(open(path.join(root, 'version.py')).read()),
    author='John Pendenque',
    author_email='pendenquejohn@gmail.com',
    description='This package provides functionnalities for aviation',
    license='MIT',
    long_description=read_files('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Zadigo/django_no_sql',
    classifiers=classifiers,
    keywords=['django', 'flask', 'nosql', 'database'],
    python_requires='>=3.7'
)
