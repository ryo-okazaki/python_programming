num_list = [0, 1, 2, 3, 4]

for i in num_list:
    print(i)

for i in range(10): # 0から9まで範囲を指定
    print(i)

for i in range(2, 10): # 2から9まで
    print(i)

for i in range(2, 10, 3): # 2から9まで3つ飛ばし
    print(i)

for _ in range(10): # 何も使わない場合は_を使う
    print('hello')