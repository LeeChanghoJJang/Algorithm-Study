import sys
import heapq
sys.stdin = open('input.txt')
N, K = map(int, input().split())
# 보석과 가방 모음
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]
# 비싼거부터 담기 위해 정렬
jewels.sort(reverse=True)  
# 작은것부터 채워나가자
bags.sort()    

result = 0

candidates = []  # 선택 가능한 보석 후보들을 담을 리스트
# 가방 공간은 점차점차 커짐 
for bag in bags:
    # 보석이 가방의 무게보다 작으면
    while jewels and jewels[-1][0] <= bag:  
        # 보석 후보에 담는다.
        heapq.heappush(candidates, -jewels[-1][1])  # 가치의 부호를 바꿔서 최대 힙처럼 사용
        # 후보군에 옮겨담았으므로 보석들에서도 뺀다
        jewels.pop()
    # 가방공간은 점차커지므로, 여러개를 담은 후보군중에 매번 비교해서 젤 가치 높은것만 결과에 더해도 됨
    if candidates: 
        result -= heapq.heappop(candidates)  

print(result)
