import dbm

# with dbm.open('cache', 'c')as db: # c: create
#     db['key1'] = 'value1'
#     db['key2'] = 'value2'
# byteかstringのみ対応

with dbm.open('cache', 'r')as db: # r: read
    print(db.get('key1'))