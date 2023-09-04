def say_something(word, *args):
    print('word =', word)
    print(args) # タプル型入れられる
    for arg in args:
        print(arg)

say_something('Hi', 'Mike', 'Nancey', 'Steve', 'John')


# ほとんど使わない
t = ('Mike', 'Nancey', 'Steve', 'John')
say_something('Hi', *t) # *tでタプルを展開して渡す