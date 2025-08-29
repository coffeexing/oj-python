import sys

def solve():
    n = int(input())
    anchors = []
    for _ in range(n):
        x, y = map(int, input().split())
        anchors.append((x, y))
    
    print("? U 0")
    sys.stdout.flush()
    d0 = int(input())
    if d0 == -1:
        return
    
    if d0 == 0:
        for x, y in anchors:
            print(f"! {x} {y}")
            sys.stdout.flush()
            return
    
    print("? R 1000000000")
    sys.stdout.flush()
    d1 = int(input())
    if d1 == -1:
        return
    
    print("? U 1000000000")
    sys.stdout.flush()
    d2 = int(input())
    if d2 == -1:
        return
    
    for ax, ay in anchors:
        for dx in range(-d0, d0 + 1):
            dy = d0 - abs(dx)
            if dy < 0:
                continue
            for sign in [1, -1]:
                test_x = ax + dx
                test_y = ay + sign * dy
                
                min_dist = min(abs(test_x - bx) + abs(test_y - by) for bx, by in anchors)
                if min_dist != d0:
                    continue
                
                min_dist = min(abs(test_x + 1000000000 - bx) + abs(test_y - by) for bx, by in anchors)
                if min_dist != d1:
                    continue
                
                min_dist = min(abs(test_x + 1000000000 - bx) + abs(test_y + 1000000000 - by) for bx, by in anchors)
                if min_dist != d2:
                    continue
                
                print(f"! {test_x} {test_y}")
                sys.stdout.flush()
                return

t = int(input())
for _ in range(t):
    solve()
