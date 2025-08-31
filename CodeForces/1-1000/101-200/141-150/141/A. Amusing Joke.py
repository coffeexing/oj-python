from collections import Counter

s = input()
t = input()
u = Counter(input())
v = Counter(s + t)

if u == v:
    print("YES")
else:
    print("NO")
