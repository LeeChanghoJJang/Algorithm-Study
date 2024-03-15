
# N, M = int(input()), int(input())

# city = [list(map(int,input().split())) for _ in range(N)]

# schedule = deque(map(lambda x : int(x)-1, input().split()))

# start = schedule.popleft()
# q = deque([start])

# goal = schedule.popleft()
# visit = [[0] * (N+1) for _ in range(N+1)]
# while q :
#     s = q.popleft()
#     city[start][s] = 1
#     city[s][start] = 1

#     if s == goal:
#         q=deque([goal])
#         start = goal
#         visit = [[0] * (N+1) for _ in range(N+1)]
#         if schedule: 
#             goal = schedule.popleft()
#         else :
#             exit(print("YES"))
    
#     for i in range(N):
#         if city[s][i] == 1 :
#             visit[s][i] == 1
#             q.append(i)
# else :
    # print("NO")

### 시간 초과 + 메모리 초과 쌍으로 맞음
    

## 세트로 풀이하기

# N, M = int(input()), int(input())

# city = [list(map(int,input().split())) for _ in range(N)]
# schedule = set(map(lambda x : int(x)-1, input().split()))
# visit = [] 

# for i in range(N-1):
#     for j in range(i,N):
#         if city[i][j] == 1:
#             if visit :
#                 for item in visit :
#                     if item & {i,j} :
#                         item.update({i,j})
#                     else:
#                         visit.append({i,j})
#             else:
#                 visit.append({i,j})
# for i in visit :
#     if schedule.issubset(i) :
#         exit(print("YES"))
# else :
#     print("NO")

### 이것도 메모리 초과 ㅋㅋㅋㅋㅋ

import sys 
from collections import deque

input = sys.stdin.readline

# 입력단계
N,M = int(input()), int(input())
adj_lst = [list(map(int,input().split())) for _ in range(N)]
city = list(map(lambda x : int(x)-1, input().split()))


visit = [0] * N

q = deque([city[0]])

visit[city[0]] = 1

while q :                                       # 그냥 단순 bfs로 풀리는 문제였음
    s = q.popleft()

    for idx, item in enumerate(adj_lst[s]):
        if item and not visit[idx] :
            visit[idx] = 1
            q.append(idx)

for i in city:
    if not visit[i] :
        exit(print("NO"))
else :
    print("YES")