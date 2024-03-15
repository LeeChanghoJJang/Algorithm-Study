# import sys
# sys.stdin = open('input.txt')
# from collections import deque
#
# N = int(input())
# trees = [-1 for _ in range(N+1)]
# adjacency_list = [[] for _ in range(N+1)]
#
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     adjacency_list[u].append(v)
#     adjacency_list[v].append(u)
#
# queue = deque([1])
# visited = [False] * (N+1)
#
# while queue:
#     parent = queue.popleft()
#     visited[parent] = True
#
#     for child in adjacency_list[parent]:
#         if not visited[child]:
#             trees[child] = parent
#             queue.append(child)
# M = int(input())
# for i in range(M):
#     A,B =map(int,input().split())
#     temp_A, temp_B = set(), set()
#     temp_A.add(A)
#     temp_B.add(B)
#     while A+B>2:
#         ans = temp_A & temp_B
#         if ans:
#             print(*ans)
#             break
#         else:
#             if A != 1:
#                 A = trees[A]
#                 temp_A.add(A)
#             if B != 1:
#                 B = trees[B]
#                 temp_B.add(B)
#     else:
#         print(1)

import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
trees = [-1 for _ in range(N+1)]
depth = [0] * (N+1)
adjacency_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

queue = deque([1])
visited = [False] * (N+1)

while queue:
    parent = queue.popleft()
    visited[parent] = True

    for child in adjacency_list[parent]:
        if not visited[child]:
            trees[child] = parent
            depth[child] = depth[parent] + 1
            queue.append(child)

M = int(input())
for i in range(M):
    A, B = map(int, input().split())

    # 조상 노드를 같은 높이까지 올려줌
    while depth[A] > depth[B]:
        A = trees[A]
    while depth[B] > depth[A]:
        B = trees[B]

    # 높이를 같게 만들고 공통 조상을 찾음
    while A != B:
        A = trees[A]
        B = trees[B]

    print(A)



