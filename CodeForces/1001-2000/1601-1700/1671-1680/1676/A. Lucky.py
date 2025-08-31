t = int(input())

for _ in range(t):
    s = input()
    first = sum(list(map(int, list(s[0:3]))))
    second = sum(list(map(int, list(s[3:6]))))
    if first == second:
        print('YES')
    else:
        print('NO')