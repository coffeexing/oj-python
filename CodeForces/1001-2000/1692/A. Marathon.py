t = int(input())

for _ in range(t):
    dis = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 4):
        if dis[i] > dis[0]:
            cnt += 1

    print(cnt)