from collections import Counter

y = int(input())

for i in range(y + 1, 10000):
    s = str(i)
    c = Counter(s)
    if not any(x > 1 for x in c.values()):
        print(i)
        break


# concise
#
# y = int(input())
#
# for i in range(y + 1, 10000):
#     s = str(i)
#     if len(s) == len(set(s)):  # 没有重复数字
#         print(i)
#         break