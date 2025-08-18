x = int(input())
s1 = x // 5
s2 = x % 5 // 4
s3 = x % 5 % 4 // 3
s4 = x % 5 % 4 % 3 // 2
s5 = x % 5 % 4 % 3 % 2
result = s1 + s2 + s3 + s4 + s5
print(result)

# concise
# x = int(input())
# print((x + 4) // 5)