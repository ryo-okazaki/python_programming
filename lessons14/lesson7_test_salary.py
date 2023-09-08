import unittest
from unittest.mock import MagicMock
from unittest import mock

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

    # @mock.patch('lesson7_salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    @mock.patch('lesson7_salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = lesson7_salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    # withの外ではMockとして扱いたくないときに使用する
    def test_calculation_salary_patch_with(self):
        with mock.patch('lesson7_salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = lesson7_salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def setUp(self):
        self.patcher = mock.patch('lesson7_salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    # def test_calculation_salary_patch_patcher(self):
    #     patcher = mock.patch('lesson7_salary.ThirdPartyBonusRestApi.bonus_price')
    #     mock_bonus = patcher.start()
    #     mock_bonus.return_value = 1
    #
    #     s = lesson7_salary.Salary(year=2017)
    #     salary_price = s.calculation_salary()
    #
    #     self.assertEqual(salary_price, 101)
    #     mock_bonus.assert_called()
    #     patcher.stop()

    def test_calculation_salary_patch_patcher(self):
        self.mock_bonus.return_value = 1

        s = lesson7_salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

    def test_calculation_salary_patch_side_effect(self):
        def f(year):
            return year * 2

        # self.mock_bonus.side_effect = lambda year: f(year)
        # self.mock_bonus.side_effect = ConnectionError

        self.mock_bonus.side_effect = [
            1,
            2,
            3,
            ConnectionError('ConnectionError'),
        ]

        s = lesson7_salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)

        s = lesson7_salary.Salary(year=2018)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)

        s = lesson7_salary.Salary(year=2019)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 103)

        s = lesson7_salary.Salary(year=200)
        with self.assertRaises(ValueError):
            s.calculation_salary()