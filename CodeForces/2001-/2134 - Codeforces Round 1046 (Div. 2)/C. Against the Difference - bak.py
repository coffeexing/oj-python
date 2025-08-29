import sys
sys.setrecursionlimit(300000)
from functools import lru_cache

@lru_cache(maxsize=200000)
def dp(a_tuple, n, pos, last_val, last_count):
    if pos == n:
        if last_count == 0 or last_count == last_val:
            return 0
        else:
            return -float('inf')

    result = dp(a_tuple, n, pos + 1, last_val, last_count)
    
    if last_count == 0:
        if a_tuple[pos] == 1:
            result = max(result, 1 + dp(a_tuple, n, pos + 1, 0, 0))
        else:
            result = max(result, dp(a_tuple, n, pos + 1, a_tuple[pos], 1))
    elif last_val == a_tuple[pos] and last_count < last_val:
        if last_count + 1 == last_val:
            result = max(result, last_val + dp(a_tuple, n, pos + 1, 0, 0))
        else:
            result = max(result, dp(a_tuple, n, pos + 1, last_val, last_count + 1))
    
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = dp(tuple(a), n, 0, 0, 0)
    print(max(0, result))
