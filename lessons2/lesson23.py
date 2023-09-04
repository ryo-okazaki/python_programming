def outer(a, b):

    def inner():
        return a + b

    return inner
    # 関数の実行結果を返しているのではなく、関数型を返している
    # 実行にはinner()とする必要がある

f = outer(1, 2)
r = f()
print(r)
# inner関数を返すようにする


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

# 初めに設定した引数から用途によって使い分けたいときに使う