t = int(input())
for _ in range(t):
    s = input()
    cnt_0 = 0
    cnt_1 = 0
    for ch in s:
        if ch == "0":
            cnt_0 += 1
        elif ch == "1":
            cnt_1 += 1

    if min(cnt_0, cnt_1) % 2 == 1:
        print("DA")
    else:
        print("NET")
