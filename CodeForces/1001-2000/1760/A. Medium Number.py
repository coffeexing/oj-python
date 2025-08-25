t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    s = [a, b, c]
    print(sum(s) - min(s) - max(s))