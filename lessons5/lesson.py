#f = open('test.txt', 'w')
# ファイルを作成し、文字を入れる
f = open('test.txt', 'a')
f.write('testestest\n')
print('test', file=f)
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()

# withは、インデント内の処理が終わったら勝手にcloseしてくれる
with open('test.txt', 'w') as f:
    f.write('testestest\n')
    print('test', file=f)
    print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)