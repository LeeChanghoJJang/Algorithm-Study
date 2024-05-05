from itertools import combinations

# 40 / DFS
def dfs(lst):
    length = len(lst)
    stack = [lst[0]] 
    visit = [0] * (N+1)

    while stack :
        now = stack.pop()
        if not visit[now] and now in lst :
            visit[now] = 1
            for next in graph[now]:
                stack.append(next)

    if sum(visit) == length:
        temp[lst] = True
        return
    temp[lst] = False
    return

# N : 구역의 수
N = int(input())

# 각 구역의 인구 수
citys = [0] + list(map(int,input().split()))

# 각 줄(1~)에 이어져있는 줄의 수와 구역의 정보
graph = [[]]
for _ in range(N):
    _,*node = map(int,input().split())
    graph.append(list(node))

temp = {}

for i in range(1,N):
    # 가능한 조합에 대한 완전 탐색
    comb = list(combinations(list(range(1,N+1)),i))
    # dfs를 통해 모든 선거구가 붙어 있는지 확인 후 , temp 에 각 조합에 대한 가능성 저장
    for cas in comb:
        dfs(tuple(cas))

ans = float('inf')

for original_case in temp:
    # 1. temp 에서 꺼낸 값이 True인가? (선거구가 이어져 있는가?)
    if temp[original_case] :
        original_tmp = 0
        reversed_tmp = 0 
        reversed_case = tuple(sorted(set(range(1,N+1))-set(original_case)))
        # 2. 반대로 뒤집은 선거구 또한 이어져 있는가?
        if temp[reversed_case]:
            # 둘다 이어져 있는 경우 서로의 인구수를 더해 값을 비교 
            for idx in original_case:
                original_tmp += citys[idx]
            for rdx in reversed_case:
                reversed_tmp += citys[rdx]
            
            ans = min(ans,abs(original_tmp - reversed_tmp))


print(-1 if ans == float('inf') else ans)