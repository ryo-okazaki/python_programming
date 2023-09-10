import contextlib
import os

try:
    os.remove('test.txt')
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):
    os.remove('test.txt')
    # tryで書く場合よりも簡潔に書ける