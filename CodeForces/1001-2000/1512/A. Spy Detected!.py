t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)
    a_min = min(a)
    a_sum = sum(a)

    if a_sum - a_max * (n - 1) == a_min:
        print(a.index(a_min) + 1)
    elif a_sum - a_min * (n - 1) == a_max:
        print(a.index(a_max) + 1)