s = set()

for i in range(10):
    s.add(i)

print(s)

# set内包表記、集合内包表記
s = {i for i in range(10)}
print(s)