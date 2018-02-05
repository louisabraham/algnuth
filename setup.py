#!/usr/bin/env python3

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='algnuth',
    version='0.0.0',
    author='Louis Abraham',
    author_email='louis.abraham@yahoo.fr',
    description='Algebraic Number Theory package',
    license='MIT',
    keywords='algebra',
    url='https://github.com/louisabraham/algnuth',
    packages=['algnuth'],
    long_description=read('README.md'),
    classifiers=[
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
)
