s = input() + '   '
l = len(s)
i = 0
f = True

while i < l:
    if s[i] == 'W' and s[i + 1] == 'U' and s[i + 2] == 'B':
        i += 3
        if not f:
            print(' ', end='')
            f = True
    else:
        print(s[i], end='')
        i += 1
        f = False
