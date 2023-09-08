import xmlrpc.client

with xmlrpc.client.ServerProxy('http://localhost:8001/') as proxy:
    print(proxy.add_num(10, 20))
# 社内インフラなどでソースコードを違うサーバーに分けて使いたい時など