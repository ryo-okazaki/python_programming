import contextlib

# def tag(name):
#     def _tag(f):
#         def _wrapper(*args, **kwargs):
#             print('<{}>'.format(name))
#             r = f(*args, **kwargs)
#             print('</{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag
#
# @tag('h1')
# def f(msg):
#     print(msg)
#
# # f = tag('h1')(f)
# f('test')

@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))

# デコレータとしても使える
# @tag('h1')
# def f(msg):
#     print(msg)

# ネストに対応している
with tag('h1'):
    print('test')
    with tag('h2'):
        print('test2')
        with tag('h3'):
            print('test3')
    with tag('h2'):
        print('test4')