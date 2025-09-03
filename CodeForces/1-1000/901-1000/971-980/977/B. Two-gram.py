from collections import defaultdict

n = int(input())
s = input()
d = defaultdict(int)

for i in range(len(s) - 1):
    sub = s[i] + s[i + 1]
    d[sub] += 1

r = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(next(iter(r)))
