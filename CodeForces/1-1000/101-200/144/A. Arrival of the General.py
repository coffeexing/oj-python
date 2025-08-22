n = int(input())
a = list(map(int, input().split()))

max_h = max(a)
i_max = a.index(max_h)
a.pop(i_max)
a.insert(0, max_h)

a_reverse = list(reversed(a))
min_h = min(a_reverse)
i_min = a_reverse.index(min_h)

print(i_max + i_min)

