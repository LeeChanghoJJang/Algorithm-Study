import sys
input = sys.stdin.readline
from heapq import *

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapify(arr)

# 계산을 할 수록 수가 커지므로 가장 큰 수를 나중에 더해줘야 한다.
for i in range(m):
    result = 0
    for j in range(2):
        result += heappop(arr)
    heappush(arr, result)
    heappush(arr, result)

print(sum(arr))