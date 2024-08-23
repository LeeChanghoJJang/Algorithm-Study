# 1135 뉴스 전하기
N = int(input())
parent_list = list(map(int, input().split()))
child_list = [[] for _ in range(N)]

# 부하 직원의 리스트를 채워 넣음
for child in range(1, N):
    parent = parent_list[child]
    child_list[parent].append(child)

# 특정 직원이 뉴스를 전파하는데 걸리는 시간을 계산
def dfs(node):
    if not child_list[node]:
        return 0

    result = []
    # 현재 직원의 각 부하 직원에 대해 재귀적으로 뉴스를 전파하는 데 걸리는 시간 계산
    for child in child_list[node]:
        result.append(dfs(child))

    # 부하 직원들이 뉴스를 전파하는 시간을 내림차순으로 정렬
    result.sort(reverse=True)
    # 각 부하 직원에게 뉴스를 전파하는 데 걸리는 시간에 순차적으로 1을 더해 최종 시간을 계산
    result = [result[i]+i+1 for i in range(len(child_list[node]))]
    return max(result)

print(dfs(0))
