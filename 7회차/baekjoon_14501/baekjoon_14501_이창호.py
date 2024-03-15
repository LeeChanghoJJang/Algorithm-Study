import sys
import heapq
sys.stdin = open('input.txt')
# 힙을 이용한 그리디 알고리즘 : 실패
# N =int(input())
# result = 0
# heap =[]
# visited = [0]*(N+1)
# for i in range(N):
#     cost, profit = map(int,input().split())
#     heapq.heappush(heap,(-round(profit/cost),-profit,-cost,i))
#
# while heap and sum(visited) < N:
#     flg = 0
#     portion, profit, cost, i = heapq.heappop(heap)
#     if not visited[i] and i -cost <= N:
#         for j in range(i,i-cost):
#             if visited[j]:
#                 flg =1
#                 break
#         if not flg:
#             visited[i:i-cost]=[1]*-cost
#             result += -profit
# print(result)

# DP를 이용한 문제 풀이
N = int(input())
consultation= [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1,-1,-1):
    cost, profit = consultation[i]
    if i + cost > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + cost] + profit)
print(dp[0])

