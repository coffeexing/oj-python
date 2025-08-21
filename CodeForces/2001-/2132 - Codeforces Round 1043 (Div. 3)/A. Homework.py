t = int(input())


while t > 0:
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()

    t -= 1

    for i in range(m):
        if c[i] == 'D':
            a = a + b[i]
        elif c[i] == 'V':
            a = b[i] + a

    print(a)