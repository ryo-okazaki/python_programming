a = {1, 2, 2, 3, 4, 4, 4, 5, 6}

print(a)
print(type(a))

b = {2, 3, 6, 7}

print(a - b)
# aに入っているものからbを取り除く

print(b - a)
# bに入っているものからaを取り除く

print(a & b)
# aとbの共通部分を取り出す

print(a | b)
# aとbの全ての要素を取り出す

print(a ^ b)
# aとbの共通部分を除いた要素を取り出す