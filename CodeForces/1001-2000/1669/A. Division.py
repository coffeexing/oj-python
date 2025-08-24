t = int(input())

for _ in range(t):
    rating = int(input())
    if 1900 <= rating:
        print('Division 1')
    if 1600 <= rating <= 1899:
        print('Division 2')
    if 1400 <= rating <= 1599:
        print('Division 3')
    if rating <= 1399:
        print('Division 4')