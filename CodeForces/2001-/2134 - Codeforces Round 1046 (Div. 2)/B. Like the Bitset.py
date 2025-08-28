t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())
    l = len(s)

    if '1' in s:
        first = s.index('1')
        last = l - 1 - s[::-1].index('1')

        print(first, last)
    else:
        print('YES')

