import sys
from heapq import *
sys.stdin = open('input.txt')  # input.txt 파일을 표준 입력으로 사용

N = int(input())  # 리스트의 크기 N을 입력받습니다.
heap = []  # 최소 힙을 사용하기 위한 리스트를 초기화합니다.

# N개의 정수 리스트를 입력받아 힙에 추가합니다.
for i in range(N):
    nums = list(map(int, input().split()))  # 정수 리스트를 입력받습니다.
    for j in nums:
        if len(heap) >= N:  # 힙의 크기가 N보다 크거나 같으면,
            if heap[0] < j:  # 힙의 최솟값보다 새로운 값이 더 크다면,
                heappop(heap)  # 힙의 최솟값을 제거합니다.
                heappush(heap, j)  # 새로운 값을 힙에 추가합니다.
        else:  # 힙의 크기가 N보다 작으면,
            heappush(heap, j)  # 새로운 값을 그냥 힙에 추가합니다.

print(heappop(heap))  # 힙에서 가장 작은 값을 꺼내어 출력합니다.
