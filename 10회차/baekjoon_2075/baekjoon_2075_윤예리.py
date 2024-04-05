import sys
input = sys.stdin.readline
from heapq import *

'''
n 개 짜리 heap을 만들어서
heap의 최소값을 반환하면 됨.
'''

n = int(input())
heap = []
for i in range(n):
    arr = list(map(int, input().split()))

    # input list인 arr을 순회할거임.
    for j in range(n):
        if len(heap) == n:
            # heap 에서 제일 작은 값과 현재 값 비교
            a = heappop(heap)
            # 둘 중 큰 값을 힙에 추가
            if a < arr[j]:
                heappush(heap, arr[j])
            else:
                heappush(heap, a)

        else:
            heappush(heap, arr[j])

print(heappop(heap))