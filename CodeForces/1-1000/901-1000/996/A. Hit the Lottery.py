n = int(input())
cash = [100, 20, 10, 5, 1]
number = 0

for i in range(5):
    number += n // cash[i]
    n %= cash[i]

print(number)