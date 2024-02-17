# 2606 백준 : 바이러스
import sys
sys.stdin = open('input.txt')
# 바이러스 숫자
N = int(input())
# 네트워크 상에 연결된 컴퓨터 정보
connection = int(input())
# 여기에 연결정보를 각 인덱스를 시작점으로 저장할거야
board=[[] for _ in range(N+1)]
# 인접 리스트 구성
for i in range(connection):
    node1, node2 = map(int, input().split())
    board[node1].append(node2)
    board[node2].append(node1)
# 1번은 처음에 방문처리 해논거임. 의미 없음 
visited = [0] +[1] + [0]* (N-1)
stack = [1]
# DFS 스택으로 돌림
while stack:
    now = stack.pop()
    for next in board[now]:
        if visited[next] == 0:
            stack.append(next)
            visited[next] =1
# 1번 컴퓨터는 제외해야 하므로 -1 해줌 
print(sum(visited)-1)
'''
31120KB 48ms
'''
