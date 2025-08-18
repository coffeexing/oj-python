s = [int(x) for x in input().split('+')]
s.sort()
result = '+'.join(str(x) for x in s)
print(result)