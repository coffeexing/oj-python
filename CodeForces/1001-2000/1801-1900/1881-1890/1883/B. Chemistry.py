from collections import Counter

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = input()
    c = Counter(a)
    cnt = sum(i % 2 == 1 for i in c.values())

    if cnt <= k + 1:
        print("YES")
    else:
        print("NO")
