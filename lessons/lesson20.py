my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
# 共通の友達を見つけるなどで、集合が使える

print(my_friends & A_friends)


# リストをセットに型変換できる

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)

# セットは重複を許さない
# 集合を使って型変換して重複を削除することができる