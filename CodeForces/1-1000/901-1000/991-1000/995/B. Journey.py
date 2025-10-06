t = int(input())

for _ in range(t):
    n, a, b, c = map(int, input().split())
    s = a + b + c
    days = n // s * 3
    miles = n % s

    if miles == 0:
        pass
    elif miles <= a:
        days += 1
    elif miles <= a + b:
        days += 2
    else:
        days += 3
    
    print(days)