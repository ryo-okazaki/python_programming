days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# zip関数を使うと、複数のリストを同時にループ処理できる
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)