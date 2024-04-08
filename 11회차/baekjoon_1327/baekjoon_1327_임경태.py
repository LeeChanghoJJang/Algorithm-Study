# 1327 소트 게임

from collections import deque

N, K = map(int, input().split())
nums = tuple(map(int, input().split()))

# 정렬된 순열 및 방문 순열 저장
sorted_nums = tuple(sorted(nums))
visit = {nums}

# BFS
Q = deque([[nums[:], 0]])
while Q:
    now, dist = Q.popleft()
    # 정렬된 순열과 같다면 종료
    if now == sorted_nums: exit(print(dist))
    # 각 자리마다 뒤집은 배열 생성
    for i in range(N-K+1):
        next = now[:i] + now[i:i+K][::-1] + now[i+K:]
        if next in visit: continue
        Q.append([next, dist+1])
        visit.add(next)

# Q가 빌 때까지 종료가 안 되었다면 정렬이 불가능한 것
print(-1)