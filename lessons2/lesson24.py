def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs) # inner関数の中でprint_infoを実行(引数の関数)
        print('end')
        return result
    return wrapper
# デコレータ

# デコレータ関数を指定
@print_info
def add_num(a, b):
    return a + b
# 関数の前後に何かしたい場合は@デコレータ関数を指定する

# f = print_info(add_num)
r = add_num(10, 20)
print(r)

@print_info
def sub_num(a, b):
    return a - b

# デコレータを使わない場合
# print('start')
# r = add_num(10, 20)
# print('end')
# 関数の処理はじめと処理終わりに


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs) # inner関数の中でprint_infoを実行(引数の関数)
        print('result:', result)
        return result
    return wrapper

@print_info
@print_more
def add_num2(a, b):
    return a + b

r2 = add_num2(10, 20)

# デコレータは何かを包み込む
f = print_info(print_more(add_num2))