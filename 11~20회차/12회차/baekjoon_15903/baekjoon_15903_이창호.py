import sys
from heapq import heapify, heappush, heappop

# 표준 입력을 'input.txt'에서 읽도록 재지정
sys.stdin = open('input.txt')

# 입력 받기
n, m = map(int, input().split())  # 카드의 개수와 합체 연산의 수 입력
heap = list(map(int, input().split()))  # 카드의 가치 입력
heapify(heap)  # 카드의 가치를 최소 힙으로 변환

# 합체 연산 수행
for i in range(m):
    a = heappop(heap)  # 가장 가치가 작은 카드 꺼내기
    b = heappop(heap)  # 두 번째로 가치가 작은 카드 꺼내기
    heappush(heap, a + b)  # 두 카드를 합친 가치를 다시 최소 힙에 추가
    heappush(heap, a + b)  # 합친 결과를 다시 최소 힙에 추가하여 중복해서 더할 수 있도록 함

# 최종 결과 출력
print(sum(heap))  # 합체 연산을 모두 수행한 후 카드들의 가치의 합 출력
