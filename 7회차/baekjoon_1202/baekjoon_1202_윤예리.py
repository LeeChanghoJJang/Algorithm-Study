# pypy

import heapq
n, k = map(int, input().split())

jewels = []
for _ in range(n):
    w, p = map(int, input().split())
    heapq.heappush(jewels, (w, p))
jewels.sort()       # 가벼운 순으로, 가벼우면 싼 순으로

bags = []
for _ in range(k):
    bags.append(int(input()))

stolen = []
result = 0
for bag in sorted(bags):
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(stolen, -jewels[0][1])       # stolen에 가치가 가장 큰 보석을 넣음
        heapq.heappop(jewels)                       # 이미 순회한 애들은 다음 가방에 넣을 필요 없으므로 pop해줌
    if stolen:      
        result += -heapq.heappop(stolen)            # 일단 stolen에 다 담아놓고 제일 비싼거 result에 저장

print(result)




# 시간초과
# n, k = map(int, input().split())
#
# jewels = []
# for _ in range(n):
#      jewels.append(list(map(int, input().split())))
#
# bags = []
# for _ in range(k):
#     bags.append(int(input()))
#
# jewels.sort(key=lambda x:(-x[1], x[0]))     # 가격이 큰 순으로 정렬, 가격이 같다면 무게가 가벼운 순으로 정렬
# bags.sort()
#
# i = 0
# result = 0
# while i < k:
#     for j in range(len(jewels)):
#         if bags[i] >= jewels[j][0]:
#             result += jewels.pop(j)[1]
#             i += 1
#             break
#     else:
#         i += 1
#
# print(result)
