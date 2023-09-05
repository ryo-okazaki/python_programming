class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car): # Carを継承 引数を見る
    pass

class TeslaCar(Car):
    def auto_tun(self):
        print('auto run')

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