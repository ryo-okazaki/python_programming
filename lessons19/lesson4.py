import contextlib
import logging
import sys

# x = input('Enter: ')
# print(x)

for line in sys.stdin:
    print(line)

print('hello')
sys.stdout.write('hello')

logging.error('Error!')
sys.stderr.write('Error!')

with open('stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        print('test')

with open('stderr.log', 'w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('Error!')