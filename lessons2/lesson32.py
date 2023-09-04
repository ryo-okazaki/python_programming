l = [1, 2, 3]
i = 5
del l

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}" . format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other: {}' . format(ex))
else: # 例外が発生しなかった場合に実行される
    print('done')
finally: # 例外が発生してもしなくても実行される
    print('clean up')

print("last")