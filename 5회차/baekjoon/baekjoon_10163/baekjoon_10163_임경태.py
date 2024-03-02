import sys
sys.stdin = open('input.txt')

arr = [[0] * 1001 for _ in range(1001)]

N = int(input())
for idx in range(N):
    i, j, w, h = map(int, input().split())
    
    for nj in range(j, j+h):
        arr[nj][i:i+w] = [idx+1]*w

for idx in range(N):
    ans = 0
    for j in arr:
        ans += j.count(idx+1)
    print(ans)