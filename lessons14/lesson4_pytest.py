import os

import pytest

import lesson2

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = lesson2.Cal()
        cls.test_file_name = 'test.txt'

    def test_add_num_and_double(self): #fixtureを引数に入れる
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        print('##################')
        print(tmpdir)
        print('##################')
        self.cal.save(tmpdir, self.test_file_name)
        test_file = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file) is True