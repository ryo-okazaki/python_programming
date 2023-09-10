import contextlib

def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception:
        return False

def clean_up():
    print('clean up')

def clean_up2():
    print('clean up')


# try:
#     is_ok = is_ok_job()
#     print('more task')
# except Exception:
#     if not is_ok:
#         clean_up()

with contextlib.ExitStack() as stack:
    stack.callback(clean_up) # stack.pop_all()が実行されない場合、clean_up()を実行する
    stack.callback(clean_up2) #スタックとして積まれる

    @stack.callback
    def clean_up3():
        print('clean up3')

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.pop_all()