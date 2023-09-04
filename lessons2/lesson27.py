t = (1, 2, 3, 4, 5)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# リスト内包表記
r = [i for i in t if i % 2 == 0]
print(r)

t2 = (5, 6, 7, 8, 9, 10)
r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]