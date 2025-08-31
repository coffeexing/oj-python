t = int(input())

kth = [0] * 1005
i = 0
x = 0
while i < 1005:
    x += 1
    if str(x)[-1] != '3' and x % 3 != 0:
        kth[i] = x
        i += 1

for _ in range(t):
    k = int(input())
    print(kth[k - 1])