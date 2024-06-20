## Algorithm Study 4회차 회의 (24.2.24.) 

### 🪙 회의개요
    가. 금일 일정 
        - 시간 : 2월 24일 토요일 10시
        - 장소 : 커피팀버 김해장유점

    나. 차주 예정 일정
        - 시간 : 3월 3일 일요일 9시
        - 방식 : 디스코드 통한 비대면 회의

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 10문제
    다. 난이도 : 최대 백준 골드 하위 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

###### 백준 IM 문제
    - 백준 IM 검색 참고

### 🏅 스터디 내용 
#### 🎈 백준 1012 유기농 배추 
> `BFS`를 이용하여 배추 있는 곳을 탐색하여 카운팅

```python
from collections import deque

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def BFS(i, j):
    Q = deque([[i, j]])
    while Q:
        i, j = Q.popleft()
        for di, dj in dr:
            ni = i + di
            nj = j + dj
            if (0 <= ni < N and 0 <= nj < M) and field[ni][nj]:
                field[ni][nj] = 0
                Q.append([ni, nj])
    field[i][j] = 0

for tc in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    cnt = 0

    # 배추 심기
    for _ in range(K):
        j, i = map(int, input().split())
        field[i][j] = 1

    # 배추흰지렁이 배치
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                BFS(i, j)
                cnt += 1

    print(cnt)
```

#### ⚽ 백준 1182 부분집합의 합
> 첫번째 방법 : 백트래킹 이용 
> 1. 반복문을 통한 `백트래킹`(`31120KB 336ms`)
> 2. 각 원소를 이진 트리 구조를 활용한 `백트래킹`(`31120KB 336ms`)
```python 
import sys
N,S = map(int,sys.stdin.readline().split())
integers = tuple(map(int,sys.stdin.readline().split()))
cnt=0
# 재귀함수 이용
def back(start,result):
    global cnt
    # 합이 S고, start가 0보다 크면(맨 처음이 포함되면 바로 cnt 1추가되는 경우 발생)
    # 부분집합의 개수 구하는 것과 동일하게 진행
    if result == S and start>0:
        cnt +=1
    # start부터 end까지 탐색하여, result값에 연산결과 저장
    for end in range(start,N):
        back(end+1,result+integers[end])
```
```python
def backtrack(idx, sum_v):
    if idx < N:
        sum_v += nums[idx]

        # 합이 조건을 만족한다면 카운트
        if sum_v == S:
            global cnt
            cnt += 1

        # 현재 인덱스의 숫자 포함
        backtrack(idx + 1, sum_v)
        # 현재 인덱스의 숫자 미포함
        backtrack(idx + 1, sum_v - nums[idx])
```
> 두번째 방법 : `combination` 라이브러리 이용 (`31120KB 360ms`)
```python
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

# 1 ~ N개의 부분집합 생성 후 합 계산
for i in range(1, N + 1):
    for j in combinations(nums, i):
        if sum(j) == S:
            cnt += 1

print(cnt)
```
> 세번째 방법 : `중첩 반복문`을 활용하여 모든 부분집합 도출 
> 1. 비트연산 미활용
```python
a, summary = map(int,input().split())       # a개의 정수와 목표 정수값을 받음

test_case = list(map(int,input().split()))  # 테케를 받고

count = 0                                   # 카운트를 설정

subset = [[]]                               # 부분집합 시작
for x in test_case :                        #
    size = len(subset)                      #
    for y in range(size) :                  #
        subset.append(subset[y] + [x])      # 비트 연산 없이 부분집합 만들기 

for i in subset :                           # 모든 부분집합의 리스트 중에서
    if sum(i) == summary and len(i) >= 1 :  # 길이가 1 이상이고, 합이 summary와 같다면
        count += 1                          # 카운트 +=1 
print(count)                         
```
> 2. 비트연산 활용
```python
import sys
N,S = map(int,sys.stdin.readline().split())
integers = tuple(map(int,sys.stdin.readline().split()))
cnt=0
# 부분집합의 모든 경우의수를 구함 ==> 결과가 S면 카운팅
for row in range(1,1<<N):
    result = 0
    for col in range(N):
        if row & (1<<col):
            result += integers[col]
    if result == S:
        cnt +=1
print(cnt)
```
#### 🧰 백준 1753 최단경로
> `Dijkstra` : 출발점부터  경로마다 발생되는 비용을 최소화하면서 도착점을 탐색하는 알고리즘 
```python
import math
import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
INF = math.inf
dist = [INF] * (V+1); dist[K] = 0

# 방향 그래프 제작 (가중치, 다음 노드)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

# Dijkstra
Q = []
heapq.heappush(Q, (0, K))

while Q:
    w, now = heapq.heappop(Q)

    # 현재 가중치보다 큰 가중치면 무시
    if dist[now] < w:
        continue

    for next_w, next in graph[now]:
        cost = w + next_w
        # 현재 노드를 거쳐, 다음 노드로 이동하는 비용이 더 적은 경우
        if dist[next] > cost:
            dist[next] = cost
            heapq.heappush(Q, (dist[next], next))

for i in dist[1:]:
    print(i if i != INF else 'INF')
```

#### 🖌 백준 1891 사분면
> 첫번째 : 사분면과 좌표값의 `규칙성` 이용 
```python
import sys
# N은 objective의 길이
N, objective = map(int,sys.stdin.readline().split())
# objective에서 이동한 좌표 길이 
x,y = map(int,sys.stdin.readline().split())
# 좌표를 사분면 값으로 변환(밑에 함수의 역산)
def find_number(x,y,N):
    result = ''
    while N:
        # 4사분면에 있는 경우
        if x >= 2 ** (N - 1) and y >= 2 ** (N - 1):
            result += '4'
            x -= 2 ** (N - 1)
            y -= 2 ** (N - 1)
        # 3사분면에 있는 경우
        elif x >= 2 ** (N - 1) and y < 2 ** (N-1):
            result += '3'
            x -= 2 ** (N - 1)
        # 2사분면에 있는 경우
        elif x < 2 ** (N - 1) and y < 2 ** (N-1):
            result += '2'
        # 1사분면에 있는 경우
        elif x < 2 ** (N - 1) and y >= 2 ** (N-1):
            result += '1'
            y -= 2 ** (N - 1)
        # 범위르 초과한 경우 
        if x<0 or y<0:
            return -1
        N-=1
    return result

# 사분면 값을 좌표로 변환
def divided(objective,x,y,depth):
    # objective를 한자리씩 축출하여 위치이동 
    while objective:
        k, v = divmod(objective,10)
        # 맨 뒷자리가 1인경우에는 y의 좌표가 젤 작은 사분면의 길이의 반만큼 늘어남 (처음에는 거즘 1)
        if v == 1:
            y += 2 ** (depth - 1)
        elif v== 2:
            pass
        elif v==3:
            x += 2 ** (depth - 1)
        elif v==4:
            x += 2 ** (depth - 1)
            y += 2 ** (depth - 1)
        depth+=1
        objective=k
    return [x,y]
# 주어진 사분면 위치의 좌표값 도출 
location_x,location_y = divided(objective,0,0,1)
# 거기서 이동한 좌표값
x_adj = location_x - y
y_adj = location_y + x
# 만일 이동했을 때 범위를 초과한 경우에는 -1 출력
if x_adj < 0 or x_adj >= 2**N or y_adj < 0 or y_adj >= 2**N:
    print(-1)
else:
    # 그 외에는 좌표값을 사분면의 위치로 변환 
    print(find_number(x_adj,y_adj,N))
```   
> 두번째 : 위 규칙성을 `분할과 정복` 알고리즘으로 풀어내어 각 경우에 해당되는 재귀함수 호출
```python
def get_idx(n, i=0, r=0, c=0):
    if n < 1: return r-y, c+x
    if num[i] == '1': return get_idx(n//2, i+1, r, c+n)
    elif num[i] == '2': return get_idx(n//2, i+1, r, c)
    elif num[i] == '3': return get_idx(n//2, i+1, r+n, c)
    elif num[i] == '4': return get_idx(n//2, i+1, r+n, c+n)

# 사분면 번호 제작
def make_num(n, r, c, ans=''):
    if n < 1: print(ans)
    elif r < n and c >= n: make_num(n//2, r, c-n, ans+'1')
    elif r < n and c < n: make_num(n//2, r, c, ans+'2')
    elif r >= n and c < n: make_num(n//2, r-n, c, ans+'3')
    elif r >= n and c >= n: make_num(n//2, r-n, c-n, ans+'4')

d, num = input().split(); n = 2**(int(d)-1)
x, y = map(int, input().split())
row, col = get_idx(n)

if 0 <= row < 2*n and 0 <= col < 2*n:
    make_num(n, row, col)
else:
    print(-1)
```
#### 🎙 백준 2644 촌수계산
> BFS나 DFS 이용
> - 인접 리스트에 해당되는 경우 촌수 1씩 가산

```python
# BFS (`34068KB / 60ms`)
from collections import deque

N = int(input())  # 사람 수
p1, p2 = map(int, input().split())  # 목표 관계
M = int(input())  # 관계 수
rel = [[] for _ in range(N+1)]  # 관계
dist = [0] * (N+1)  # 촌수

# 무방향 그래프 제작
for _ in range(M):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

Q = deque([p1])
while Q:
    now = Q.popleft()
    if now == p2:
        break
    for next in rel[now]:
        if not dist[next]:
            dist[next] = dist[now] + 1
            Q.append(next)
else:
    dist[p2] = -1
print(dist[p2])
```
> 아래는 DFS 이용(`31120KB 40ms`)
```python
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
```

#### 👔 백준 7662 이중 우선순위 큐
> `heapq` 라이브러리를 활용
> 1. 최소힙과 최대힙 각각 정의
> 2. 값이 추가될 때마다 같이 추가
> 3. 값을 뺄 때마다 `visited`를 활용하여 중복된 값도 동시 삭제 
```python

```
---
#### 📀 백준 10226 적록색약
> `BFS` 이용하여 'R','G','B' 영역 탐색
> - replace를 활용하여 색약이 보는 경우에 'R'과 'G'를 같게 해주는게 포인트
```python
import sys
sys.stdin = open("input.txt")
from collections import deque

# 색 영역 체크
def BFS(pic, visited, i, j, color):
    Q = deque([[i, j]])
    visited[i][j] = 1

    while Q:
        ci, cj = Q.popleft()
        for di, dj in dr:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and pic[ni][nj] == color:
                    visited[ni][nj] = 1
                    Q.append([ni, nj])

# 영역 개수 세기
def count_area(pic):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(pic, visited, i, j, pic[i][j])
                cnt += 1
    
    return cnt

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
pic = [input() for _ in range(N)]

n_cnt = count_area(pic)  # 일반인
pic = [pic[i].replace('G', 'R') for i in range(N)]  # 변환
w_cnt = count_area(pic) # 적록색약

print(n_cnt, w_cnt)
```
#### 🧏‍♀️ 백준 11725 트리의 부모 찾기
> 첫번째 : `DFS`나 `BFS` 이용
```python
# DFS
N = int(input()) # 노드 개수
link = [[] for _ in range(N+1)]  # 연결 노드
prnt = [0] * (N+1)  # 부모 노드

# 무방향 그래프 제작
for _ in range(N-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

# DFS - 트리의 루트 1을 시작으로 탐색
stack = [1]
while stack:
    now = stack.pop()
    # 다음 노드에 부모 노드로 자신 입력
    for next in link[now]:
        if not prnt[next]:
            prnt[next] = now
            stack.append(next)

for i in prnt[2:]:
    print(i)
```
```python
def bfs(vertex, graph):
    q = deque()
    q.append(vertex)

    # 인덱싱을 편하게 해주기 위해 (N + 1) 개의 요소
    # 방문여보 + 부모 노드의 번호를 저장하는 리스트
    result = [1, 1] + [0] * (N - 1)
    
    while q:
        # temp는 현재 정점의 위치
        temp = q.popleft()
        
        # 만약 인근 정점 중에 방문하지 않은 곳이 있다면
        # 그 정점은 현재 정점의 자식 노드이므로 result에 반영
        for v in graph[temp]:
            if not result[v]:
                result[v] = temp
                q.append(v)
            
    # 문제의 조건에 따라 1번 노드는 제외하고 반환
    return result[2:]
    
N = int(input())
graph = [[] for _ in range(N + 1)]

# 양 방향 간선
for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
[print(i) for i in bfs(1, graph)]
```
#### ❤️‍🔥 백준 14889 스타트와 링크
> `백트래킹` 활용
> 1. 한 쪽팀이 우선 완성되면 되므로, 팀원의 숫자가 N//2일 때를 정지조건
> 2. 정지 시, 각 팀원들의 합을 구하여 최소값을 저장 
```python
import sys 
sys.stdin = open('input.txt')

def create_comb(arr, idx):
    global min_v
    # 능력치 차이의 최솟값이 0 or 팀원이 부족하면 고려 안함
    if min_v == 0 or idx - len(arr) > N//2:
        return

    # 팀이 완성되면 능력치 계산
    if len(arr) == N//2:
        opp_arr = [i for i in range(0, N) if i not in arr]
        stat_diff = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                a = arr[i]; b = arr[j]
                c = opp_arr[i]; d = opp_arr[j]
                stat_diff += S[a][b] + S[b][a] - (S[c][d] + S[d][c])
        min_v = min(min_v, abs(stat_diff))
        return

    # 팀원 포함 여부 결정
    if idx < N:
        create_comb(arr + [idx], idx+1)
        create_comb(arr, idx+1)

N = int(input())  # 사람 수
S = [tuple(map(int, input().split())) for _ in range(N)]  # 능력치

# 팀 능력치 배열 완성
min_v = 100
create_comb([0], 1)
print(min_v)
```
#### 👽 백준 19185 육십갑자
> `원형큐`의 순환방식을 이용.
> `%` 연산을 사용하여 원하는 시점의 결과값을 손쉽게 도출
```python
for tc in range(int(input())):
    N, M = map(int, input().split())  # 문자 개수
    s1, s2 = input().split(), input().split()  # 문자열
    # 알고 싶은 년도 개수로 년도를 입력받음 - 년도를 각각의 문자개수로 나눔 - 문자열로 변환하여 출력
    print(f"#{tc+1} {' '.join([f'{s1[Y % N]}{s2[Y % M]}' for Y in [int(input()) - 1 for _ in range(int(input()))]])}")
```

