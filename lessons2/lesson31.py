"""
Test
"""

animal = 'cat'

def f():
    """
    test func
    :return:
    """
    global animal
    animal = 'dog'
    animal2 = 'dog'
    print('after:', animal)
    print(locals())

    print(f.__doc__)
    print(f.__name__)

f()
print('global:', animal)
print('global:', globals())