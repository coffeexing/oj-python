s = input()
ch = ''
cnt = 0

for chi in s:
    if ch != chi:
        ch = chi
        cnt = 1
    else:
        cnt += 1

    if cnt >= 7:
        print('YES')
        exit()

print('NO')