import pytest
from pydata_july2016 import pydata_july2016
from pydata_july2016 import data_functions as dfn
import pandas as pd
import numpy as np
import numpy.testing as npt

def test_python_path():
    assert 'python' in pydata_july2016.python_path()

def test_site_packages():
    assert 'site-packages' in pydata_july2016.python_path()

@pytest.fixture(scope='module')
def action_data():
    d = {'emplid':        [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
         'adm_appl_nbr':  [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
         'appl_prog_nbr': [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         'prog_action':   ['APPL',
                           'COND',
                           'MATR',
                           'APPL',
                           'ADMT',
                           'MATR',
                           'APPL',
                           'APPL',
                           'ADMT',
                           'APPL',
                           'COND',
                           'APPL'],
         'effdt':         [pd.Timestamp('2016-01-01'),
                           pd.Timestamp('2016-01-02'),
                           pd.Timestamp('2016-01-03'),
                           pd.Timestamp('2016-02-01'),
                           pd.Timestamp('2016-02-02'),
                           pd.Timestamp('2016-02-03'),
                           pd.Timestamp('2016-03-01'),
                           pd.Timestamp('2016-03-01'),
                           pd.Timestamp('2016-03-02'),
                           pd.Timestamp('2016-04-01'),
                           pd.Timestamp('2016-04-02'),
                           pd.Timestamp('2016-04-03')],
         'effseq':        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    df2 = pd.DataFrame(d)
    df1 = dfn.most_recent_rows(df2)
    return df1, df2
    

def test_has_admt(action_data):
    df1, df2 = action_data
    npt.assert_array_equal(dfn.check_for_action(df1, df2, 'ADMT')['has_admt'].values,
                           [False, True, False, True, False])

def test_has_appl(action_data):
    df1, df2 = action_data
    npt.assert_array_equal(dfn.check_for_action(df1, df2, 'APPL')['has_appl'].values,
                           [True, True, True, True, True])

def test_appl_admt_order(action_data):
    df1, df2 = action_data
    npt.assert_array_equal(dfn.check_appl_admt_order(df2).values,
                           ['COND', 'ADMT', 'APPL', 'ADMT', 'APPL'])