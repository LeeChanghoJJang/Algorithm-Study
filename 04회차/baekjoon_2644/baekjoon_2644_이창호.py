import sys
# 촌수를 계산하기 위한 DFS 함수
def DFS(start,end,visited):
    # target1부터 target2를 탐색해나감
    stack =[start]
    visited[start]=1
    while stack:
        now = stack.pop()
        # target2를 찾은 경우 함수 종료 
        if now == end:
            return visited[now]-1
        # 인접리스트 탐색
        for next in connection[now]:
            if not visited[next]:
                # 이어진 관계를 탐색했을 때 그 관계는 현재 촌수 +1
                visited[next] = visited[now] + 1
                stack.append(next)
    return -1

n = int(sys.stdin.readline())
# 찾고자 하는 두 사람의 촌수 
target1, target2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
# 인접리스트 저장 위함 
connection = [[] for _ in range(n+1)]
# 인접리스트 저장
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    connection[x].append(y)
    connection[y].append(x)
print(DFS(target1,target2,[0]*(n+1)))
