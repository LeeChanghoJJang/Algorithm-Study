import sys
import heapq
sys.stdin = open('input.txt')
N, K = map(int, input().split())

jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

jewels.sort(reverse=True)  # 가치순으로 정렬
bags.sort()    # 용량순으로 정렬

result = 0

candidates = []  # 선택 가능한 보석 후보들을 담을 리스트

for bag in bags:
    while jewels and jewels[-1][0] <= bag:  # 현재 가방의 용량보다 작거나 같은 보석들을 후보에 추가
        heapq.heappush(candidates, -jewels[-1][1])  # 가치의 부호를 바꿔서 최대 힙처럼 사용
        jewels.pop()  # 선택한 보석은 후보에서 제거
    if candidates:  # 후보가 있으면
        result -= heapq.heappop(candidates)  # 가치가 가장 높은 보석을 선택하여 결과에 더함

print(result)
