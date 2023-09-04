def say_something():
    print('Hello')

say_something()
print(type(say_something))

def say_something2():
    s = 'hi'
    return s

result = say_something2()
print(result)

def what_is_this(color):
    print(color)
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)