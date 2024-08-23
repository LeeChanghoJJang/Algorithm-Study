import sys
input = sys.stdin.readline
N = int(input())
parent_list = list(map(int, input().split()))
child_list = [list() for _ in range(N)]

for child in range(1, N) :
  parent = parent_list[child]
  child_list[parent].append(child)

def dfs(node) :
  if not child_list[node] :
    return 0
  result = list()
  for child in child_list[node] :
    result.append(dfs(child))
  result.sort( reverse = True)
  result = [ result[i] + i + 1 for i in range(len(child_list[node])) ]
  return max(result)

print(dfs(0))
