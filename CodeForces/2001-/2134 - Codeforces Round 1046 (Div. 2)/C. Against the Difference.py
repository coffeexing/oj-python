t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    key = []
    nums = []

    key.append(a[0])
    nums.append(1)

    for i in range(1, len(a)):
        if a[i] == key[-1]:
            if key[-1] > nums[-1]:
                nums[-1] += 1
            else:
                key.append(a[i])
                nums.append(1)
        else:
            key.append(a[i])
            nums.append(1)

    for i in range(len(key)):
        print(f"{key[i]}:{nums[i]}", end=' ')
    print('\n')
