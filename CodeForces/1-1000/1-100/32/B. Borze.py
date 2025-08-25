code = input()
l = len(code)
i = 0
while i < l:
    if code[i] == '.':
        i += 1
        print(0, end='')
    elif code[i] == '-':
        if code[i + 1] == '.':
            print(1, end='')
        elif code[i + 1] == '-':
            print(2, end='')
        i += 2