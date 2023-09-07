"""
ウェルノウンポート番号（0-1023）
登録済みポート番号（1024-49151）
動的・プライベートポート番号（49152-65535）
"""
import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     s.sendall(b'Hello')
#     data = s.recv(1024)
#     print(repr(data))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello UDP', ('127.0.0.1', 50007))