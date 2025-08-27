p = input()
s = ['H', 'Q', '9']

for ch in s:
    if ch in p:
        print('YES')
        exit()

print('NO')