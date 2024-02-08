#!/usr/bin/env python3
import setuptools
from setuptools import setup, Extension

setup(
    name='fastlz',
    version='0.0.2',
    description='Python wrapper for FastLZ, a lightning-fast lossless '
                'compression library.',
    author='Jared Suttles',
    url='https://github.com/jaredsuttles/python-fastlz',
    license='BSD License',
    setup_requires=['wheel'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving :: Compression',
        'Topic :: Utilities'
    ],
    ext_modules = [
        Extension(
            'fastlz',
            sources=['fastlz.c', 'fastlz/fastlz.c'],
            include_dirs=['fastlz']
        )
    ]
)
