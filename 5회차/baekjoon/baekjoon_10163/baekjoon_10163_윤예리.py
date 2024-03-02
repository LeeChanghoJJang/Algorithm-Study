# import sys
# sys.stdin = open('input.txt')

arr = [[0] * 1001 for _ in range(1001)]
result = [0] * 101

n = int(input())
for i in range(1, n+1):
    a, b, w, h = map(int, input().split())
    for r in range(a, a+w):
        for c in range(b, b+h):
            arr[r][c] = i

for i in range(1001):
    for j in range(1001):
        if arr[i][j] != 0:
            result[arr[i][j]] += 1

for i in range(1, n+1):
    print(result[i])