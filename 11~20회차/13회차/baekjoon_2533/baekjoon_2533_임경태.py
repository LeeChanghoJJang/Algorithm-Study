# 2533 사회망 서비스

N = int(input())
visit = [1, 1] + [0] * (N-1)
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DP[i][j] : i -> 정점 / j -> 0: 어답터x, 1: 어답터
DP = [[0, 1] for _ in range(N+1)]

def DFS(now):
    for next in tree[now]:
        if visit[next]: continue
        visit[next] = 1
        # DFS로 제일 끝 점까지 간 후 작업하며 거슬러 올라기는 형태
        DFS(next)
        # 본인이 얼리어답터가 아니라면 주변 사람들 모두 얼리어답터여야 함
        DP[now][0] += DP[next][1]
        # 본인이 얼리어답터라면 주변 사람들의 여부가 상관 없으므로 최솟값을 선택
        DP[now][1] += min(DP[next])

DFS(1)
print(min(DP[1]))

'''
    Tree DP 문제는 재귀로 내려간 후 올라가면서 할 task를 잘 살펴보자
'''