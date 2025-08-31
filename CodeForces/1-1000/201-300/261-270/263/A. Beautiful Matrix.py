matrix = [[int(x) for x in input().split()] for _ in range(int(5))]
result = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            result = abs(i - 2) + abs(j - 2)
            break

print(result)