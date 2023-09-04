def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)


def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana', 'apple', 'orange', entree='beef', drink='coffee')
# **kwargsは、辞書型で受け取る