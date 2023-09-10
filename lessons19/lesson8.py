import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1

print(d)

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)

d = collections.defaultdict(int)
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)

d = collections.defaultdict(set)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
for k, v in s:
    d[k].add(v)

c = collections.Counter()
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    c[word] += 1
print(c)
print(c.most_common(1))
print(c.values())
print(sum(c.values()))

# このファイル内の一番多い文字数を調べる
import re
with open('lesson8.py', 'r') as f:
    words = re.findall(r'\w+', f.read().lower())
    print(collections.Counter(words).most_common(10))