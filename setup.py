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

    'Environment :: Console',

    'License :: OSI Approved :: MIT License',

    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows :: Windows 10',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',

    'Natural Language :: English',

    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',

    'Topic :: Scientific/Engineering :: Physics',
]

install_requires = [
    'pandas>=1.1.5',
    'numpy==1.19.3',
]


setuptools.setup(
    name='pyaviation',
    version='1.0.1',
    author='John Pendenque',
    author_email='pendenquejohn@gmail.com',
    description='This package provides functionnalities for aviation',
    license='MIT',
    long_description=read_files('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Zadigo/pyaviation',
    classifiers=classifiers,
    keywords=['python', 'aviation'],
    python_requires='>=3.9'
)
