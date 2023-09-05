s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'w+') as f: # w+は、書き込んだ後に読み込みもできる
    # print(f.read()) # 何も書き込んでいないので、何も読み込めない 書き込み用に新しいファイルを作るので、空ファイルになってしまう
    f.write(s)
    f.seek(0) # 一番初めに戻る作業が必要
    print(f.read())

with open('test.txt', 'r+') as f: # r+は、読み込んだ後に書き込みもできる ファイルが無い場合はエラーになる
    f.write(s)
    f.seek(0)
    print(f.read())