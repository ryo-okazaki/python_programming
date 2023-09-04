# In と Notの使い方

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

if not a == b:
    print('Not equal')
# この書き方はあまり好ましくない

if a != b:
    print('Not equal')

is_ok = True

if is_ok: # is_ok == True bool型の場合は省略する
    print('hello')

if not is_ok:
    print('hello')