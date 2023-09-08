import unittest
from unittest.mock import MagicMock

import lesson7_salary

class TestSalary(unittest.TestCase):

    def test_calculation_salary(self):
        s = lesson7_salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1) # モックを作成 return_valueは返り値
        self.assertEqual(s.calculation_salary(), 101) # 101が返ってくるかテスト

        s.bonus_api.bonus_price.assert_called() # メソッドが呼ばれたかテスト
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1) # メソッドが呼ばれた回数をテスト

    def test_calculation_salary_no_salary(self):
        s = lesson7_salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=1) # モックを作成 return_valueは返り値
        self.assertEqual(s.calculation_salary(), 101) # 101が返ってくるかテスト
        s.bonus_api.bonus_price.assert_not_called() # メソッドが呼ばれたかテスト