import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)

class ToyotaCar(Car): # Carを継承 引数を見る
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 enable_auto_run2=False,
                 passwd='123'):
        # self.model = model
        super().__init__(model)
        self.__enable_auto_run2 = None
        self._enable_auto_run = enable_auto_run # tesra car だけの独自の引数
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run # 外部からアクセス可能

    @property
    def enable_auto_run2(self):
        return self.__enable_auto_run2 # 外から見えないようにする クラス内からアクセス可能

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def auto_tun(self):
        print('auto run')

    def run(self):
        print('super fast')
        print(self.__enable_auto_run2)

car = Car()
car.run()

print('###############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('###############')
# 継承

tesla_car = TeslaCar('Model S', passwd='456')
print(tesla_car.model)
# print(tesla_car.enable_auto_run)
print(tesla_car.enable_auto_run)
tesla_car.enable_auto_run = True
tesla_car.auto_tun()
tesla_car.run()

# 新しいメンバ変数として追加されてしまう
tesla_car.__enable_auto_run2 = True


class T(object):
    pass

t = T()
t.name = 'test'
t.age = 20
print(t.name, t.age)