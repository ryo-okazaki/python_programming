import io # インメモリストリーム
import zipfile

# 実際のファイルのストリームに書かなくても、インメモリでファイルを扱える
import requests

with open('/tmp/a.txt', 'w') as f:
    f.write('Hello, world!')

with open('/tmp/a.txt', 'r') as f:
    print(f.read())

# f = io.StringIO() # インメモリストリームを作成
f = io.BytesIO()
# f.write('string io')
f.write(b'string io')
f.seek(0) # ファイルの先頭に移動
print(f.read())

url = 'http://www.nomadworks.co.jp/htmlsample/archive/win/sec2/info01.zip'

f = io.BytesIO()
r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('info01.txt') as f:
        print(f.read().decode())