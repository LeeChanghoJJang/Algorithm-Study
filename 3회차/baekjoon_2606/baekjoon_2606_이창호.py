# 2606 백준
import sys
sys.stdin = open('input.txt')

N = int(input())
connection = int(input())
board=[[] for _ in range(N+1)]
# 인접 리스트 구성
for i in range(connection):
    node1, node2 = map(int, input().split())
    board[node1].append(node2)
    board[node2].append(node1)
visited = [0] +[1] + [0]* (N-1)
stack = [1]
while stack:
    now = stack.pop()
    for next in board[now]:
        if visited[next] == 0:
            stack.append(next)
            visited[next] =1
print(sum(visited)-1)