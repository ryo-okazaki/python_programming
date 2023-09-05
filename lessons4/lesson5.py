class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a)
print(a.what_is_your_kind())

b = Person
print(b) # この段階ではクラスオブジェクトではない

# インスタンスを生成しなくてもクラスメソッドを呼び出せる
print(Person.kind)
print(Person.what_is_your_kind())

Person.about(1999)