class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car): # Carを継承 引数を見る
    def run(self):
        print('fast')

class TeslaCar(Car):
    def auto_tun(self):
        print('auto run')

    def run(self):
        print('super fast')

car = Car()
car.run()

print('###############')
toyota_car = ToyotaCar()
toyota_car.run()
print('###############')
# 継承

tesla_car = TeslaCar()
tesla_car.auto_tun()
tesla_car.run()