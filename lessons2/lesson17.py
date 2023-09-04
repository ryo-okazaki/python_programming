def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('beef', 'ice', 'beer')

# キーワード引数を使うと、引数の順番を気にしなくて良くなる
menu(entree='beef', dessert='ice', drink='beer')
menu('beef', dessert='ice', drink='beer')

def menu2(entree = 'beef', drink = 'wine', dessert = 'ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)
    
menu2('chicken', 'beer')