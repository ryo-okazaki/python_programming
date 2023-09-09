import base64
import os
import hashlib

# print(hashlib.sha256(b'password').hexdigest())
# print(hashlib.sha256(b'password').hexdigest())

user_name = 'user1'
user_pass = 'password'
db = {}

salt = base64.b64encode(os.urandom(32))
print(salt)

def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(password).hexdigest()
    for _ in range(10):
        digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()

    return digest

# get_digestと同じことしている組み込みメソッド
digest1 = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 100000
)

db[user_name] = get_digest(user_pass)

def is_login(user_name, password):
    return db.get(user_name) == get_digest(password)

print(is_login(user_name, user_pass))