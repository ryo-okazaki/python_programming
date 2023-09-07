"""
ウェルノウンポート番号（0-1023）
登録済みポート番号（1024-49151）
動的・プライベートポート番号（49152-65535）
"""
import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     s.listen(1)
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print('data: {}, addr: {}'.format(data, addr))
#                 conn.sendall(b'Received: ' + data)

# まずはpython lesson3_socket_server.pyを実行しておく
# その後にpython lesson3_socket_client.pyを実行する

# UDPの場合
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('127.0.0.1', 50007))
    while True:
        msg = input('メッセージを入力してください: ')
        data, addr = s.recvfrom(1024)
        print("data: {}, addr: {}".format(data, addr))