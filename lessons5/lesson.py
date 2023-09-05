#f = open('test.txt', 'w')
# ファイルを作成し、文字を入れる
f = open('test.txt', 'a')
f.write('testestest\n')
print('test', file=f)
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()


s = """\
AAA
BBB
CCC
DDD
"""

# withは、インデント内の処理が終わったら勝手にcloseしてくれる
with open('test.txt', 'w') as f:
    f.write('testestest\n')
    print('test', file=f)
    print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
    f.write(s)

with open('test.txt', 'r') as f:
    # print(f.read())

    # while True:
    #     line = f.readline()
    #     print(line, end='')
    #     if not line:
    #         break

    # while True:
    #     chunk = 2 # 2文字ずつ読み込む
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break
    print(f.tell()) # ファイルのどこを読んでいるか
    print(f.read(1)) # 1文字読む
    f.seek(5) # ファイルのどこを読むか指定
    print(f.read(3))
    f.seek(15) # ファイルのどこを読むか指定
    print(f.read(3))