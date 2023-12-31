import requests

class ThirdPartyBonusRestApi(object):
    def get_api_name(self):
        return 'bonuses for 2017'

    def bonus_price(self, year):
        r = requests.get('http://localhost/bonus', params={'year': year})
        return r.json()['price']
    # mockという疑似的にデータを作ることができるライブラリを使う

class Salary(object):
    def __init__(self, base=100, year=2017):
        self.bonus_api = ThirdPartyBonusRestApi()
        self.base = base
        self.year = year

    def get_from_boss(self):
        return 0

    def calculation_salary(self):
        bonus = 0
        if self.year < 2020:
            try:
                bonus = self.bonus_api.bonus_price(year=self.year)
            except ConnectionError:
                bonus = 0
        return self.base + bonus