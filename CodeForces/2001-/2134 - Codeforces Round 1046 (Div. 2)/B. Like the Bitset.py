t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    p = []
    h = '1' * k
    no = False
    
    for i in range(n - k + 1):
        if s[i:i + k] == h:
            no = True
    
    if no:
        print('NO')
    else:
        print('YES')

        l = 1
        r = len(s)

        for ch in s:
            if ch == '0':
                p.append(r)
                r -= 1
            else:
                p.append(l)
                l += 1
        print(*p)
