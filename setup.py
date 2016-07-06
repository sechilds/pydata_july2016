import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'pydata_july2016',
    version = '0.0.1',
    author = 'Stephen Childs',
    description = 'Sample package for PyData Calgary July 2016 meetup',
    long_description=read('README.md'),
    entry_points = {
        'console_scripts': ['pydata_july2016=pydata_july2016:main'],
    }
)


