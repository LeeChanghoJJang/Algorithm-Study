from collections import deque

size = int(input())                      # 전체 사람 수

start,end = map(int,input().split())     # 구해야 하는 관계

t = int(input())
tree = [[] for _ in range(size+1)]       # 트리는 아닌데 가계도가 family tree라..
for _ in range(t):
    s,e = map(int,input().split())       # 촌수는 양방향 관계
    tree[s].append(e)
    tree[e].append(s)


# 또또또 BFS
visit = [0] * (size+1)
q = deque([start])
while q :
    tc = q.popleft()

    if tree[tc] :
        for item in tree[tc]:
            if visit[item] == 0:
                q.append(item)
                visit[item] = visit[tc] +1
                if item == end :
                    print(visit[item])
                    break

if visit[end] == 0:
    print(-1)
# 34044kb / 64ms