a, b = map(int, input().split())

diff = min(a, b)
same = (a + b - diff * 2) // 2
print(diff, same)