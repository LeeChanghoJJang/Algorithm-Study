import sys
input = sys.stdin.readline

N = int(input())

link = {i: [] for i in range(1, N+1)}

for _ in range(N-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

visited = [0] * (N+1)
start = []
for i in link:
    if len(link[i]) == 1:
        start.append(i)

while start:
    v = start.pop()
    for x in link[v]:
        for y in link[x]:
            link[y].remove(x)
            if len(link[y]) == 1:
                start.append(y)
        visited[x] = 1
        link[x] = []
print(visited.count(1))
'''
트리가 주어졌을 때,
가장 최소한의 노드만 선택해서
모든 사람이 얼리어답터가 되게 ?

자신의 모든 친구가 얼리어답터일 때만 얼리어답터가 된다.
링크 몇갠지 세고,
제일 많은 사람부터 선택
많은 사람 선택을 안하면 얼리어답터 되기가 힘들다
연결된 곳에서 1씩 빼주고,
0되면 얼리어답터 된거로 판단
'''