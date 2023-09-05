import string

# s = """\
# Hi $name.
#
# $contents
#
# Have a good day
# """

# t = string.Template(s) # 完全に読み込み用
# contents = t.substitute(name='Mike', contents='How are you?')

with open('../design/email_template.txt') as f:
    t = string.Template(f.read())
    # tはwithの外でも使える

contents = t.substitute(name='Mike', contents='How are you?')

print(contents)