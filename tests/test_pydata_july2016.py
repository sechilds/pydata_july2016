import pytest
from pydata_july2016 import pydata_july2016

def test_python_path():
    assert 'python' in pydata_july2016.python_path()

