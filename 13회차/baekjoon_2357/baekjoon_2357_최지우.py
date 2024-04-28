import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def maketree(node, start, end):
    if start == end:
        tree[node] = (num[start], num[start])
        return tree[node]

    mid = (start+end) // 2
    left = maketree(node*2, start, mid)
    right = maketree(node*2+1, mid+1, end)

    tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]


def find(node, start, end):
    if b < start or a > end:
        return (10**9 + 1, 0)

    if a <= start and b >= end:
        return tree[node]

    mid = (start+end) // 2
    left = find(node*2, start, mid)
    right = find(node*2+1, mid+1, end)

    return (min(left[0], right[0]), max(left[1], right[1]))


N, M = map(int, input().split())
num = [int(input()) for _ in range(N)]

h = int(math.ceil(math.log(N, 2)))
node_len = 1 << (h+1)
tree = [0 for _ in range(node_len)]
maketree(1, 0, N-1)
# print(tree)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    result = find(1, 0, N-1)
    print(result[0], result[1])
