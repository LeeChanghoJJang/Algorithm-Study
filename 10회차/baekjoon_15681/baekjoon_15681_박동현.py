## 재귀
def Query(now):
    distance[now]= 1

    for next in tree[now]:
        if distance[next] == 0:
            Query(next)
            distance[now] += distance[next]


N,R,Q = map(int,input().split())

tree = [ [] for _ in range(N+1)]
distance = [0] * (N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

Query(R)
for _ in range(Q):
    num = int(input())
    print(distance[num])

##### python3 66492 KB / 460 ms
    
## 반복
# import sys
# input = sys.stdin.readline

# N,R,Q = map(int,input().split())

# tree = [ [] for _ in range(N+1) ]
# distance = [0] * (N+1)
# visit = [False] * (N+1)

# for _ in range(N-1):
#     a,b = map(int,input().split())
#     tree[a].append(b)
#     tree[b].append(a)

# stack = [R]
# visit[R] = True
# distance[R] = 1 

# while stack :
#     start = stack[-1]
#     check = True
#     for end in tree[start] :
#         if not visit[end]:
#             stack.append(end)
#             visit[end] = True
#             distance[end] = 1
#             check = False
#             break
#     if check :
#         stack.pop()
#         if stack :
#             parent = stack[-1]
#             distance[parent] += distance[start]

# for _ in range(Q):
#     num = int(input())
#     print(distance[num])

### python3 시간 초과 // pypy 시간 초과