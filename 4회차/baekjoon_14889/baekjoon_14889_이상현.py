import sys
input = sys.stdin.readline

# 백준 14889번 스타트와 링크

# 두 팀을 나누어 규칙에 맞게 능력치를 계산했을 때 차이의 최솟값을 구하는 문제
def dfs(cnt, last):
    global min_

    # 만약 팀 인원이 N // 2 명이라면 각각 팀의 능력치를 계산 후 최솟값 갱신
    if cnt == N // 2:
        start = sum(list_[row][col] if visited[row] and visited[col] else 0
                    for row in range(N) for col in range(N))

        link = sum(list_[row][col] if not(visited[row] or visited[col]) else 0
                   for row in range(N) for col in range(N))

        min_ = min(min_, abs(start - link))
        return

    # 만약 남은 사람 중에서 팀에 속하지 않은 사람이 있다면
    # 그사람을 팀에 포함하는 경우와 포함하지 않는 경우 모두 탐색
    for i in range(last, N):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, i + 1)
            # 완전탐색
            visited[i] = 0

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
# 기본 최솟값을 float('inf')로 설정
min_ = float('inf')
visited = [0] * N
dfs(0, 0)
print(min_)