s = input()
t = input()
ls = len(s)
lt = len(t)
l = min(ls, lt)

if ls != lt:
    print('NO')
    exit()

for i in range(l):
    if s[i] != t[l - 1 - i]:
        print('NO')
        exit()

print('YES')

# concise
#
# s = input()
# t = input()
# print("YES" if s[::-1] == t else "NO")