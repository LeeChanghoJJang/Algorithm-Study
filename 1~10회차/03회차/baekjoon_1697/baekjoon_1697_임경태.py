# 1697 숨바꼭질

from collections import deque

# N: 수빈 위치 / K: 동생 위치
N, K = map(int, input().split())
# 거리 저장
dist = [0] * 100001

# 수빈 위치 > 동생 위치*(3/4) -> 차이만큼 시간 계산
if N >= 3*K//4:
    print(abs(N-K))
# 수빈 위치 < 동생 위치 -> BFS로 최단시간 탐색
else:
    Q = deque([N])
    while Q:
        X = Q.popleft()
        # 동생을 찾았다면 종료
        if X == K:
            print(dist[K])
            break
        # 동생을 찾지 못했다면 다음 지점 탐색
        for next in (X-1, X+1, 2*X):
            if 0 <= next <= 100000 and not dist[next]:
                dist[next] = dist[X] + 1
                Q.append(next)

'''
34196KB / 124ms
'''