n = int(input())

for i in range(n):
    s = str(input())
    if len(s) <= 10:
        print(s)
    else:
        first = s[0]
        last = s[-1]
        length = len(s) - 2
        result = f"{first}{length}{last}"
        print(result)
