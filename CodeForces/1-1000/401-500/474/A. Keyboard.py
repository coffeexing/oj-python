keyboard = ["qwertyuiop", "asdfghjkl;", "zxcvbnm,./"]

bias = 1 if input() == 'L' else -1

s = input()

for ch in s:
    row = 0
    for i in range(3):
        if ch in keyboard[i]:
            row = i
    
    col = keyboard[row].index(ch)
    print(keyboard[row][col + bias], end='')
