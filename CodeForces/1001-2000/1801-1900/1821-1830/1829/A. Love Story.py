pattern = "codeforces"
t = int(input())
for _ in range(t):
    string = input()
    cnt = 0
    for s, p in zip(string, pattern):
        if p != s:
            cnt += 1
    print(cnt)