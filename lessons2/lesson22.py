def outer(a, b):

    def plus(c, d):
        return c + d
    # plus関数は、outer関数の中でしか使えない
    # outer関数内だけで繰り返し関数を使える
    # inner関数は、outer関数の中でしか使えない

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)