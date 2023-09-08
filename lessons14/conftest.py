import os.path

import pytest

@pytest.fixture
def csv_file(tempdir): # ここのfixtureは予め定義されているもの
    with open(os.path.join(tempdir, 'test.csv'), 'w+') as f:
        print('before')
        yield f
        print('after')

def pytest_addoption(parser): # pytestはデフォルトでpytest.pyのtest_addoption()を呼び出す
    parser.addoption(
        '--os-name', action='store', default='linux', help='os name'
    )