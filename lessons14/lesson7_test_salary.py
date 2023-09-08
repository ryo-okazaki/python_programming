import unittest
from unittest.mock import MagicMock

import lesson7_salary

class TestSalary(unittest.TestCase):

    def test_calculation_salary(self):
        s = lesson7_salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1) # モックを作成 return_valueは返り値
        self.assertEqual(s.calculation_salary(), 101) # 101が返ってくるかテスト