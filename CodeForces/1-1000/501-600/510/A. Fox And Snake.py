n, m = map(int, input().split())

for i in range(n):
    j = i % 4
    match j:
        case 0 | 2:
            print('#' * m)
        case 1:
            print('.' * (m - 1) + '#')
        case 3:
            print('#' + '.' * (m - 1))