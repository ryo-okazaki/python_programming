import tempfile # I/Oバッファ上で行うので、勝手に消してくれる

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# I/Oバッファ上ではなく、tempfileを実際に作成する場合
with tempfile.NamedTemporaryFile(delete=False) as t: # delete=Falseで、一時ファイルを削除しない
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())
        print(t.name)
        # C:\Users\yoshi\AppData\Local\Temp\tmp1q2q3q4q5

# 一時ディレクトリを作成する場合
with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)