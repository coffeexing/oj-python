t = int(input())

for i in range(t):
    n = int(input())
    a = list()
    k = 1

    while 1 + 10 ** k <= n:
        s = 1 + 10 ** k
        if n % s == 0:
            x = n // s
            a.append(x)
        k += 1

    result = [int(x) for x in sorted(a)]
    if len(result) == 0:
        print(0)
    else:
        print(len(result))
        print(*result)