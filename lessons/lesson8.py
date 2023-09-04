print('####################')

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

s[0] = 'X'
print(s)

print(s[2:5])

s[2:5] = ['C', 'D', 'E']
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)

print(n)

n.insert(0, 200)
print(n)

n.pop() # 最後の要素を削除

n.pop(0) # 指定した要素を削除

del n[0] # 指定した要素を削除

n.remove(3) # 指定した要素を削除


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(a + b)

a += b
print(a)

b.extend(a)

print('####################')