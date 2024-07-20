# 7432 디스크 트리
import sys
input = sys.stdin.read

data = input().strip().split()
N = int(data[0])
paths = data[1:N+1]
tree = {}

# 각 경로를 트리에 추가
for path in paths:
    parts = path.split("\\")
    current = tree

    # 경로의 각 부분을 순회
    for part in parts:
        # 현재 수준의 트리에 해당 부분이 없다면, 새로 추가
        if part not in current:
            current[part] = {}
        current = current[part]

# 깊이 우선 탐색을 사용하여 트리를 출력
def dfs(tree, depth):
    # 현재 수준의 트리 키를 정렬하여 순회
    for key in sorted(tree.keys()):
        print(" " * depth + key)
        dfs(tree[key], depth+1)

dfs(tree, 0)
