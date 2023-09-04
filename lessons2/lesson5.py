# is_ok = True
is_ok = 1 # 1はTrueとして扱われる
is_ok = '' # No
is_ok = [] # No
is_ok = set() # 集合

if is_ok: # len(is_ok) > 0と行わなくて良い
    print('OK')
else:
    print('No')


is_empty = None # NoneはFalseとして扱われる
if is_empty is None: # == ではなく、isを使う
    print('None!!!')

print(1 == True) #
print(1 is True) # False
print(True is True)
print(None is None) # True
# Noneの場合はisを使う