print('####################')

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j = ', j)
print('i = ', i)

x = [1, 2, 3, 4, 5]

# y = x.copy()
y = x[:]

y[0] = 100
print('y = ', y)
print('x = ', x)

# Pythonのリストは参照渡し
# 配列をコピーしたい場合、copy()メソッドを使うか、スライスを使う

X = 20
Y = X
print(id(X))
print(id(Y))
print(Y)
print(X)

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)

print('####################')