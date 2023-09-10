import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)


m = c = collections.ChainMap(a, b, c)
print(m)
print(m.maps)
print(m['c'])

m.maps.reverse()

m.maps.insert(0, {'c': 'cccc'})
print(m['c'])

m['b'] = 'BBBBBB'
print(m.maps)

class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return
        self.maps[0][key] = value

m = DeepChainMap(a, b, c)
m['num'] = -1
m['new_num'] = -1
print(m['num'])
print(m['new_num'])