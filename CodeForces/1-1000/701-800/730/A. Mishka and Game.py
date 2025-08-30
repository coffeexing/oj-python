n = int(input())
M = 0
C = 0

for _ in range(n):
    m, c = map(int, input().split())
    if c < m:
        M += 1
    elif c > m:
        C += 1

if M > C:
    print('Mishka')
elif M < C:
    print('Chris')
else:
    print('Friendship is magic!^^')
