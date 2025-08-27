t = int(input())
a = [int(pow(2, k)) for k in range(0, 50)]

for _ in range(t):
    n = int(input())
    if n not in a:
        print('YES')
    else:
        print('NO')