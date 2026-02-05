t = int(input())

for _ in range(t):
    n = int(input())
    s = ''
    for i in range(n):
        a = input
        if s == '':
            s = a
        elif a + s < s:
            s = a + S
        else:
            s = s + a
    
    print(s)
