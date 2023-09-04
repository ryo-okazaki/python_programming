from lesson_package.tools import utils

def sing():
    return 'aaaaasing'

def cry():
    return utils.say_twice('bbbbbcry')

print(sing())

print('animal:', __name__)

if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)
    print(cry())