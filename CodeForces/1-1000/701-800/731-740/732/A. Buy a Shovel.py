k, r = map(int, input().split())

for i in range(1, 10):
    if (k * i - r) % 10 == 0 or k * i % 10 == 0:
        print(i)
        break


# concise
# 
# k, r = map(int, input().split())
#
# for i in range(1, 10):
#     if (k * i) % 10 in [0, r]:
#         print(i)
#         break