n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = set().union(a[1:], b[1:])

if len(c) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')