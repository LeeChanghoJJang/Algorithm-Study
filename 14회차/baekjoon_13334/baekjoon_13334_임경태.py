# 13334 철로
import heapq

N = int(input())
bulidings = sorted([sorted(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
D = int(input())
Q = []; ans = 0

# 끝점을 기준으로 정렬된 건물들 순회
for building in bulidings:
    # 건물의 끝점을 기준으로 철로 설정
    left, right = building
    heapq.heappush(Q, left)

    # 시작점이 철로 범위 밖에 있는 경우 제거
    while Q and Q[0] < right - D:
        heapq.heappop(Q)
    
    # 시작점이 철로 범위 안에 있는 경우 카운트
    ans = max(ans, len(Q))

print(ans)