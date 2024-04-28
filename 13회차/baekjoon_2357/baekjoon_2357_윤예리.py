# 세그먼트 트리

import sys
input = sys.stdin.readline
import math

def makeTree(idx, start, end):
    if start == end: # 리프 노드
        graph[idx] = (arr[start], arr[start])
        return graph[idx]

    mid = (start + end) // 2

    left = makeTree(idx*2, start, mid)
    right = makeTree(idx*2+1, mid+1, end)

    graph[idx] = (min(left[0], right[0]), max(left[1], right[1]))

    return graph[idx]

def find(idx, start, end):
    if b < start or a > end:
        return (float('inf'), 0)

    if a <= start and b >= end:
        return graph[idx]

    mid = (start+end) // 2
    left = find(idx*2, start, mid)
    right = find(idx*2+1, mid+1, end)

    return (min(left[0], right[0]), max(left[1], right[1]))

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

h = math.ceil(math.log2(n)) + 1     # 노드 개수에 따른 그래프 depth 계산
num_of_nodes = 1 << h   # 2^h
graph = [0 for _ in range(num_of_nodes)]
makeTree(1, 0, len(arr)-1)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    result = find(1, 0, len(arr)-1)
    print(*result)