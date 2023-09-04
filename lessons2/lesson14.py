d = {'x': 100, 'y': 200}

print(d.items())
# dict_items([('x', 100), ('y', 200)])
# d.items()は、dict_items型のオブジェクトを返す
# リストの中にタプルが入っている

for k, v in d.items(): # k, vはアンパック
    print(k, ':', v)
    # kがvalue
    # vがkey