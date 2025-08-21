t = int(input())

for i in range(t):
    n = int(input())
    h = n // 2
    s = list()
    for j in range(2, 2 * h + 1, 2):
        s.append(j)
    for j in range(1, 2 * h - 1, 2):
        s.append(j)

    s1 = sum(s[0:h])
    s2 = sum(s[h:])
    result = s1 - s2

    if result % 2 == 1 and result > 0 and result not in s and len(s) == n - 1:
        s.append(result)
        print('YES')
        print(*s)
    else:
        print('NO')