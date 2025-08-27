n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
for i in range(1, n + 1):
    if sum(a[:i]) > sum(a[i:]):
        print(i)
        exit()