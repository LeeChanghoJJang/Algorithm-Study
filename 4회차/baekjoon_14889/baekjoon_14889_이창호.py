# 14889 스타트와 링크
# 백트래킹으로 풀어보기
import sys
def solution(idx, depth):
    global answer

    # 한 팀의 구성이이 완료 경우
    if depth == n // 2:
        start = 0
        link = 0
        # 반복문을 통해 팀 능력치 조사
        for i in range(n):
            for j in range(n):
                # 스타트 팀 능력치
                if visited[i] and visited[j]:
                    start += graph[i][j]

                # 링크 팀 능력치
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]

        # 스타트 팀의 능력치와 링크 팀의 능력치의 최소 값을 구한다.
        answer = min(answer, abs(start - link))
        return

    # 반복문과 백트래킹을 통해 통해 팀을 구성할 수 있는 경우의 수 확인
    for x in range(idx, n):
        if not visited[x]:
            visited[x] = True
            solution(x + 1, depth + 1)
            visited[x] = False

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False] * n
answer = 1e9
solution(0, 0)
print(answer)