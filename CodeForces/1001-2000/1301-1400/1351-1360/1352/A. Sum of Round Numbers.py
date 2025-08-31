t = int(input())

for _ in range(t):
    n = input()[::-1]
    s = list()
    for i in range(len(n)):
        if n[i] != '0':
            s.append(int(n[i]) * (10 ** i))

    print(len(s))
    print(*s)