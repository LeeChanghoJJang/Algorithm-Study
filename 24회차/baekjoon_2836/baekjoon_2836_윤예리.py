import sys
input = sys.stdin.readline
from heapq import *

n, m = map(int, input().split())   
arr, result = [], m
for _ in range(n):
    start, end = map(int, input().split())
    if start > end:
        heappush(arr, (end, start))

scope = [arr[0][0] if arr else 0, arr[0][1] if arr else 0]

while arr:
    left, right = scope
    cur_l, cur_r = heappop(arr)
    if left <= cur_l <= right:
        scope[1] = max(right, cur_r)
    else:
        result += ((right-left) * 2)
        scope = [cur_l, cur_r]

result += ((scope[1] - scope[0] * 2))
print(result)


# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())   

# taxi = []
# for i in range(n):
#     start, end = map(int, input().split())

#     if start < end : continue # 정주행 안 볼 거임
#     taxi.append((m-start, m-end))
# taxi.sort()
# t = len(taxi)

# answer = 0
# x = 0
# while x < t:
#     start, end = taxi[x]
#     nextTarget = x

#     while nextTarget + 1 < t and taxi[nextTarget+1][0] < end:
#         nextTarget += 1
#         end = max(end, taxi[nextTarget][1])
#     answer += (end-start)
#     x = nextTarget + 1

# print(m + sum * 2)