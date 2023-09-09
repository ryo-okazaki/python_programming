import string
import random

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode('utf-8')
print(key)
# 暗号化するにはブロックごとに暗号化する 16文字の暗号キーでないといけない(なので、AES.block_size)

# 初期ベクトル 一番初めのブロックをXORを使って暗号化する
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode('utf-8')
print(iv)

plaintext = 'gnairfgnafgawerkt'
cipher = AES.new(key, AES.MODE_CBC, iv)
padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) * padding_length
plaintext = plaintext.encode('utf-8')

cipher_text = cipher.encrypt(plaintext)

print(cipher_text)

# 復号化
cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher2.decrypt(cipher_text)
print(decrypted[:-decrypted[-1]])


# ファイルのエンコーディング
with open('plaintext', 'r') as f, open('enc.dat', 'wb') as e:
    plaintext = f.read().encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += bytes([padding_length]) * padding_length
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)

with open('enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher2.decrypt(f.read())
    print(decrypted[:-decrypted[-1]].decode('utf-8'))