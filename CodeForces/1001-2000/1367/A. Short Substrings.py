t = int(input())

for _ in range(t):
    s = input()
    print(s[0], end='')
    for i in range(1, len(s), 2):
        print(s[i], end='')
    print()