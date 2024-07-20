import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
dic = defaultdict(list)
# 각 노드는 자식노드들의 리스트 가짐
for _ in range(N):
    lst = input().strip().split('\\')
    for i in range(len(lst) - 1):
        if lst[i] not in dic:
            dic[lst[i]] = []
        if lst[i + 1] not in dic[lst[i]]:
            dic[lst[i]].append(lst[i + 1])

# 트리 구조를 출력하는 함수
def print_tree(node, depth):
    print(' ' * depth + node)
    if node in dic:
        for child in sorted(dic[node]):
            print_tree(child, depth + 1)

# 최상위 노드들을 찾아서 트리를 출력
root_nodes = sorted([node for node in dic if all(node not in dic[parent] for parent in dic)])

for root in root_nodes:
    print_tree(root, 0)
