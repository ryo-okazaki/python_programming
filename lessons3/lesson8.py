# 標準ライブラリ
import collections
import os
import sys

# サードパーティライブラリ
# import termcolor

# 自作モジュール
import lesson_package

# ローカルのファイル
import config

print(collections.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)