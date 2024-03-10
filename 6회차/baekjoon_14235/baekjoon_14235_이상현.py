# 백준 14235번 크리스마스 선물

from heapq import *

n = int(input())
value_heapq = []

for _ in range(n):
    a, *gift_list = list(map(int, input().split()))

    # a가 0이라면 가치가 가장 큰 선물을 pop한 후
    # 그 값을 출력
    # 만약 선물 상자가 비었다면 -1을 출력
    if a == 0:
        if value_heapq:
            print(-heappop(value_heapq))
        else:
            print(-1)
            
    # a가 0이 아니라면 선물을 충전하는 곳이므로
    # 선물의 가치를 저장하는데 최대힙을 이용하기 위해
    # 부호를 반대로 해줌
    else:
        for gift in gift_list:
            heappush(value_heapq, -gift)