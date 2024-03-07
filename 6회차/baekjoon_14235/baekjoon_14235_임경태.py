# 14235 크리스마스 선물
import heapq

gift = []  # 최대 힙 생성
for _ in range(int(input())):
    n = list(map(int, input().split()))
    if n.pop(0):
        for i in n:
            heapq.heappush(gift, -i)
    else:
        if gift: print(-heapq.heappop(gift))
        else: print(-1)

'''
40920KB / 124ms
'''