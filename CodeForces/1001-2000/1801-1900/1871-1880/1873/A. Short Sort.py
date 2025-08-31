# t = int(input())
#
# table = {
#     'abc': 'YES',
#     'acb': 'YES',
#     'bac': 'YES',
#     'bca': 'NO',
#     'cab': 'NO',
#     'cba': 'YES',
# }
#
# for _ in range(t):
#     s = input()
#     print(table[s])

t = int(input())

for _ in range(t):
    s = input()
    if s[0] == 'a' or s[1] == 'b' or s[2] == 'c':
        print("YES")
    else:
        print("NO")