n, h = map(int, input().split())
a = [int(x) for x in input().split()]

count = sum(1 for x in a if x > h)
print(count + n)