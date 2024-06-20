import sys
import heapq
sys.stdin = open('input.txt')

T= int(input())
heap = []
for tc in range(T):
    N, *gifts = map(int,input().split())
    # N이 0이면 크리스마스 선물을 줘야함
    if N == 0:
        # 줄게 있다면? 순차적으로 꺼내서 줌(단 가치가 큰것부터(최대힙))
        if heap:
            print(heapq.heappop(heap)[1])
        # 없으면 뭐 -1이지
        else:
            print(-1)
    # N이 0이 아니면 기프트에 추가되는 거임
    else:
        # 한개가 아닐 수 있으므로 반복문을 통해 최대힙으로 저장 
        for i in gifts:
            heapq.heappush(heap,(-i,i))
