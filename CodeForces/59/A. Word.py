s = str(input())
lower = 0
upper = 0

for i in range(len(s)):
    if s[i].islower():
        lower += 1
    elif s[i].isupper():
        upper += 1

if lower >= upper:
    print(s.lower())
else:
    print(s.upper())