def pytest_addoption(parser): # pytestはデフォルトでpytest.pyのtest_addoption()を呼び出す
    parser.addoption(
        '--os-name', action='store', default='linux', help='os name'
    )