class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car): # Carを継承 引数を見る
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model
        super().__init__(model)
        self.enable_auto_run = enable_auto_run # tesra car だけの独自の引数
    def auto_tun(self):
        print('auto run')

    def run(self):
        print('super fast')

car = Car()
car.run()

print('###############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('###############')
# 継承

tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.auto_tun()
tesla_car.run()