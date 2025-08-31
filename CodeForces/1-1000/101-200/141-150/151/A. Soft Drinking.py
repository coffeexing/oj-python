n, k, l, c, d, p, nl, np = map(int, input().split())

toast = k * l // nl
slices = c * d
portions = p // np
times = min(toast, slices, portions)
print(times // n)