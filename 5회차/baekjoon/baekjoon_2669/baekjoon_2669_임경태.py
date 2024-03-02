import sys
sys.stdin = open("input.txt")

arr = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for r in range(y1, y2):
        arr[r][x1:x2] = [1] * (x2 - x1)

ans = 0
for r in range(101):
    ans += arr[r].count(1)
print(ans)
