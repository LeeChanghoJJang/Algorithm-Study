import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(100001)

'''
1. 그래프 그림
2. 루트 노드는 무조건 1이므로 1의 자식(a) 확인
3. a에게 부모가 없으면 부모로 1을 넣고
4. a의 자식, b로 이동
5. b에게 부모가 있는지 확인한 후 없으면 a로 부모를 넣고 또 b의 자식에게로 이동
6. graph 순회하며 모두 부모를 찾아줌
'''

def mktr(i):
    for j in graph[i]:
        if par[j] == 0:
            par[j] = i
            mktr(j)

n = int(input())
par = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

par = [0] * (n+1)

# 만약 부모가 없는 노드가 있다면 다시 한번 더 확인
# 함수로 뺌
# for i in range(1, n+1):
#     if par[i] == 0:
#         for j in ls:
#             if j[0] == i or j[1] == i:
#                 mktr(j[0], j[1])

# 트리의 루트는 1
mktr(1)
for i in range(2, n+1):
    print(par[i])