s = 'nfghafgafjio3vherv'

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)


from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)
print(d['f'])