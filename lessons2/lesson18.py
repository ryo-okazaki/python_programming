def test_func(x, l=()):
    l.append(x)
    return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# Pythonはリストはデフォルト引数で与えない
r = test_func(100)
print(r)

r = test_func(100)
print(r)
# 参照渡しなので、2回目は[100, 100]となる

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l