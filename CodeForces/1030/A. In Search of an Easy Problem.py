n = int(input())
a = [int(x) for x in input().split()]

c = a.count(1)
if c > 0:
    print('HARD')
else:
    print('EASY')