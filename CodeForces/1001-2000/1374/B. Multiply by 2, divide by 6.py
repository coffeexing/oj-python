t = int(input())

for _ in range(t):
    n = int(input())
    a = n
    cnt1 = 0
    cnt2 = 0
    while a % 3 == 0:
        a //= 3
        cnt1 += 1
    while a % 2 == 0:
        a //= 2
        cnt2 += 1    
    if cnt1 < cnt2 or a != 1:
        print(-1)
        continue
    cnt = 0
    while n != 1:
        if n % 6 == 0:
            n //= 6
        else:
            n *= 2
        cnt += 1
    print(cnt)
