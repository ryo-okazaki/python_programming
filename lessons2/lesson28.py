w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 辞書内包表記
d = {x: y for x, y in zip(w, f)}
print(d)