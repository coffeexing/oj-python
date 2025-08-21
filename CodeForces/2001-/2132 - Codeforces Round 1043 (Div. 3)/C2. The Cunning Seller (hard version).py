t = int(input())
INF = 10**18
cost = [3, 10, 33, 108, 351, 1134, 3645, 11664, 37179, 118098, 373977, 1180980, 3720087, 11691702, 36669429, 114791256, 358722675, 1119214746, 3486784401, 10847773692, 33705582543]
number = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401]


for _ in range(t):
    n, k = map(int, input().split())

    if k >= 30:
        temp_n = n
        deals = 0
        for i in range(len(number) - 1, -1, -1):
            x = temp_n // number[i]
            temp_n %= number[i]
            deals += x

        if deals <= k:
            temp_n = n
            coin = 0
            for i in range(len(number) - 1, -1, -1):
                x = temp_n // number[i]
                temp_n %= number[i]
                coin += x * cost[i]
            print(coin)
            continue

    max_reachable = min(n, k * max(number[:10]))

    INF = float('inf')
    dp = {}
    dp[(0, 0)] = 0

    for i in range(1, k + 1):
        new_dp = {}
        for (prev_deals, watermelons), prev_cost in dp.items():
            if prev_deals == i - 1:
                key = (i, watermelons)
                if key not in new_dp:
                    new_dp[key] = INF
                new_dp[key] = min(new_dp[key], prev_cost)

                for x in range(min(15, len(cost))):
                    new_watermelons = watermelons + number[x]
                    if new_watermelons <= n:
                        key = (i, new_watermelons)
                        if key not in new_dp:
                            new_dp[key] = INF
                        new_dp[key] = min(new_dp[key], prev_cost + cost[x])

        dp.update(new_dp)

    result = INF
    for deals in range(k + 1):
        key = (deals, n)
        if key in dp:
            result = min(result, dp[key])

    if result != INF:
        print(result)
    else:
        print(-1)