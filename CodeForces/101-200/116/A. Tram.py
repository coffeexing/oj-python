n = int(input())
minimum = 0
cap = 0

for i in range(n):
    a, b = map(int, input().split())
    cap += b - a
    minimum = max(minimum, cap)

print(minimum)