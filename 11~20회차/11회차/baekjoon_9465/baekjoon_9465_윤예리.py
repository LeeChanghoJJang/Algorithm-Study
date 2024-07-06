'''
DP
1과 2 중 더 나은 것 계산
1. 한 칸 뒤 대각선
2. 두 칸 뒤 대각선
'''
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())

    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    if n == 1:
        print(*max(arr))
        continue

    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]

    for i in range(2, n):
        arr[0][i] += max(arr[1][i-1], arr[1][i-2])
        arr[1][i] += max(arr[0][i-1], arr[0][i-2])

    print(max(arr[0][n-1], arr[1][n-1]))