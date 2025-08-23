n = int(input())
s = list(map(int, input().split()))

crimes = 0
police = 0

for i in range(n):
    if s[i] == -1:
        if police > 0:
            police -= 1
        else:
            crimes += 1
    else:
        police += s[i]

print(crimes)