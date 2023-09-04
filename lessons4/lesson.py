class Person(object):
    def __init__(self, name):
        self.name = name
        print('first')

    def say_something(self):
        print('I am {} hello'.format(self.name))
        self.run()

    def run (self):
        print('run')

    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

def person(name):
    if name == 'A':
        print('hello')