import pytest

import lesson2

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = lesson2.Cal()

    def test_add_num_and_double(self, request): #fixtureを引数に入れる
        # os_name = 'mac'
        os_name = request.config.getoption('--os-name')
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        # 実際にlsコマンドの出力結果を表示するには、
        # pytest lesson3_pytest.py --os-name=mac -s
        assert self.cal.add_num_and_double(1, 1) == 4