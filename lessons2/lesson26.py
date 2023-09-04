l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('#############')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

g = greeting()
print(next(g))
print('@@@@@')
print(next(g))
print('@@@@@')
print(next(g))
print('@@@@@')

print('#############')

def counter(num=10):
    for _ in range(num):
        yield 'run'
# Pythonはyieldを使うと、関数がジェネレーターになる
# 状態を保持している
# 重たい処理を一気に行うのではなく、小分けにして実行するなど

c = counter()
print(next(c))