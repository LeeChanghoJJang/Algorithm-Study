import sys
import heapq

input = sys.stdin.readline

N,K = map(int,input().split())

jewel = []

for _ in range(N):
    heapq.heappush(jewel, list(map(int,input().split())))    # 무게 최소힙

bags = []

for _ in range(K):
    bags.append(int(input()))

bags.sort()                                                  # 작은 가방부터 순회

ans = 0
tmp = []                                                     # 최소 무게부터 tmp에 담기고, 최대 가치부터 빠져나감
for bag in bags :                                            # 작은 가방부터 bag이 담을 수 있는 최대 보석을 담아서 더함
    while jewel and bag >= jewel[0][0] :
        heapq.heappush(tmp, -heapq.heappop(jewel)[1])        # 가치 최대힙
    if tmp :                                                 # tmp에 담은 보석이 남아있으면 그 중 가장 가치가 높은 보석을 가방에 담음
        ans -= heapq.heappop(tmp)
    elif not jewel:                                          # 보석이 더 없다면 순회 종료
        break

print(ans)