import os

import pytest

import lesson2

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = lesson2.Cal()
        cls.test_dir = 'tmp/test_dir'
        cls.test_file_name = 'test.txt'

    def teardown_class(cls):
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_add_num_and_double(self, csv_file): #fixtureを引数に入れる
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        print('##################')
        print(tmpdir)
        print('##################')
        self.cal.save(tmpdir, self.test_file_name)
        test_file = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file) is True

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = lesson2.Cal()
            cal.add_num_and_double('1', '1')

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file) is True