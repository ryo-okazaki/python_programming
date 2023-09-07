"""
REST

HTTPメソッド クライアントが行いたい処理をサーバに伝える

GET データの参照
POST データの新規登録
PUT データの更新
DELETE データの削除

"""

import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

# url = 'https://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# with urllib.request.urlopen(url) as f:
#     r = print(json.loads(f.read().decode('utf-8')))
#     print('#####################')

req = urllib.request.Request(
    'https://httpbin.org/post',
    json.dumps(payload).encode('utf-8'),
    method='POST'
)

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
    print('#####################')

req = urllib.request.Request(
    'https://httpbin.org/put',
    json.dumps(payload).encode('utf-8'),
    method='PUT'
)

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
    print('#####################')

req = urllib.request.Request(
    'https://httpbin.org/delete',
    json.dumps(payload).encode('utf-8'),
    method='DELETE'
)

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
    print('#####################')