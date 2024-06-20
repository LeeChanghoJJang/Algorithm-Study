'''
[ DP ]
현재 위치까지 최소 비용 저장.
[ 비트마스킹 ]
방문 도시 정보를 배열로 저장하는 것 보다 메모리가 훨씬 절약됨.

1. DFS
2. 모든 도시를 방문했다면 비용 계산
3. dp에 저장
'''

def dfs(now, visited):
    if visited == (1 << n)-1:
        # 출발점으로 갈 수 있다면 비용 return
        if arr[now][0]:
            return arr[now][0]
        # 못 가면 inf
        else:
            return float('inf')

    # dp에 있다면 dp 반환
    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = float('inf')
    for next_ in range(1, n):
        # 못 가거나 이미 갔던 길이라면 continue
        if arr[now][next_] == 0 or visited & (1 << next_):
            continue

        cost = dfs(next_, visited | (1 << next_)) + arr[now][next_]
        min_cost = min(cost, min_cost)

    # 지금까지 최소 비용 dp에 저장
    dp[(now, visited)] = min_cost
    return min_cost

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = {}
# now = 0, visited[0] = 1
print(dfs(0, 1))
# print(dp)
