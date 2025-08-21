s = input()
t = set()

for c in s:
    if c.isalpha():
        t.add(c)

print(len(t))