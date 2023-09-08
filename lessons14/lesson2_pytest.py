import pytest

import lesson2

# def test_add_num_and_double():
#     cal = lesson2.Cal()
#     assert cal.add_num_and_double(1, 1) == 4

release_name = 'lesson'

class TestCal(object):

    @classmethod
    def setup_class(cls): # クラスが呼ばれたら実行
        print('start')
        cls.cal = lesson2.Cal()

    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method): # メソッドが呼ばれたら実行 クラスにメソッドが複数ある場合、毎回インスタンスを作成することになる
        print('method={}'.format(method.__name__))
        # self.cal = lesson2.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        cal = lesson2.Cal()
        assert cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skip(reason='skip!') # PyCharmのpytestの実行構成でoptionのところに-rsを入力する
    @pytest.mark.skipif(release_name=='lesson', reason='skip!!') # 条件付きスキップ
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = lesson2.Cal()
            cal.add_num_and_double('1', '1')
#
#     # @unittest.skip('skip!') # スキップ
#     @unittest.skipIf(release_name=='lesson', 'skip!!') # 条件付きスキップ
#     def test_add_num_and_double(self):
#         cal = lesson2.Cal()
#         self.assertEquals(
#             cal.add_num_and_double(1, 1), 4
#         )
#         """
#         assertEqual(a, b)   a == b
#         assertNotEqual(a, b)    a != b
#         assertTrue(x)   bool(x) is True
#         assertFalse(x)  bool(x) is False
#         assertIs(a, b)  a is b
#         assertIsNot(a, b)   a is not b
#         assertIsNone(x) x is None
#         assertIsNotNone(x)  x is not None
#         assertIn(a, b)  a in b
#         assertNotIn(a, b)   a not in b
#         assertIsInstance(a, b)  isinstance(a, b)
#         assertNotIsInstance(a, b)   not isinstance(a, b)
#         """
#
#
# if __name__ == '__main__':
#     unittest.main()