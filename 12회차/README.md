## Algorithm Study 12회차 회의 (24.4.21.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 4월 21일 일요일 아침 9시  
        - 방식 : 비대면 디스코드 

    나. 차주 예정 일정
        - 시간 : 4월 28일 일요일 저녁 7시  
        - 방식 : 김해 커피팀버

    다. 변경사항 요약 (4월 28일 부터)
        1. 각자 선정한 1문제 리뷰(모두 앞에서 바로 풀 수 있을 만큼) 
            - 요청있거나, 말하고 싶은 사람은 자기 문제 아니라도 추가 리뷰 가능
        2. 각자 1문제씩만 선정(총 7문제)
        3. 일정 기본값: 매주 토요일 9시 반 → 매주 일요일 저녁 7시
            - 일정 변경 시, 사전협의하여 변경. 변경불가 시 불참비 지출 要.

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 각자 리뷰할 문제 선정 
    나. 문제수 : 인당 1문제, 총 7문제
    다. 난이도 : 최대 백준 골드 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 이번 주의 새로운 문제 : 세그먼트 트리
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

### 🎁 이번회차 풀이 문제
   ###### 1. 창호
    - 백준 2357 최소값과 최댓값(골드 1) - 세그먼트 트리
   ###### 2. 예리
    - 백준 1727 커플만들기(골드 2) - DP
   ###### 3. 경태
    - 백준 1199 오일러 경로(플래티넘 4) - 오일러 경로
   ###### 4. 동현
    - 백준 16946 벽 부수고 이동하기 4(골드 2) - BFS, DFS
   ###### 5. 상현
    - 백준 1062 가르침(골드 4) - 백트래킹
   ###### 6. 지우
    - 백준 2638 치즈(골드 3) - 탐색 구현
   ###### 7. 권민
    - 백준 2533 사회망서비스(골드 3) - 트리를 이용한 DP

### 🤢 문제 선정
   ###### 1. 창호
    - 백준 1197 최소 스패닝 트리(골드 4)
    - 백준 1991 트리 순회(실버 1)
   ###### 2. 예리
    - 백준 2252 줄 세우기 (골드3)
    - 백준 11729 하노이탑 이동 순서 (골드5)
   ###### 3. 경태
    - 백준 1799 비숍 (골드1)
    - 백준 17626 Four Squares (실버3)
   ###### 4. 동현
    - 백준 1987 알파벳 (골드4)
    - 백준 15903 카드 합체 놀이 (실버1)
   ###### 5. 상현
    - 백준 14427 수열과 쿼리 15(골드 3) - 세그먼트 트리
    - 백준 5567 결혼식(실버 2)  

### 🏅 스터디 내용 
#### 🎈 백준 1197 최소 스패닝 트리
> `Kruskal` 이용한 문제 풀이(복습) 
> 1. find : 대표 노드 찾기(젤 루트노드)
> 2. union : 다른 두 무리가 있을 때, 하나의 무리로 합쳐줌(대표 노드 동일화)
> 3. graph를 가중치 오름차순으로 정렬
> 4. 순회하면서 다른 무리일 경우, 대표노드를 더하고, 가중치를 더해줌

```python
# 부모 노드를 찾는 함수
def find(x):
    if parent[x] != x:  # 루트 노드가 아니면
        parent[x] = find(parent[x])  # 루트 노드를 찾을 때까지 재귀적으로 호출하고 경로 압축
    return parent[x]

# 두 집합을 합치는 함수
def union(x, y):
    root_x = find(x)  # x의 루트 노드를 찾음
    root_y = find(y)  # y의 루트 노드를 찾음
    if root_x < root_y:  # x의 루트 노드가 y의 루트 노드보다 작으면
        parent[root_y] = root_x  # y가 속한 집합을 x가 속한 집합에 포함시킴
    else:  # 그렇지 않으면
        parent[root_x] = root_y  # x가 속한 집합을 y가 속한 집합에 포함시킴

# 입력 받기
input = sys.stdin.readline
V, E = map(int, input().split())  # 정점의 개수와 간선의 개수 입력
parent = list(range(V + 1))  # 각 정점의 부모 노드를 자기 자신으로 초기화
graph = [list(map(int, input().split()))[::-1] for i in range(E)]  # 간선 정보 입력 후 역순으로 저장 (가중치, 정점1, 정점2)
graph.sort()  # 가중치 순으로 정렬

result = 0  # 결과값 초기화
for wei, now, next in graph:  # 가중치 순서대로 간선을 확인
    if find(now) != find(next):  # 현재 간선의 양 끝 정점이 같은 집합에 속하지 않으면 (사이클이 생성되지 않으면)
        result += wei  # 결과값에 현재 간선의 가중치 추가
        union(now, next)  # 현재 간선의 양 끝 정점을 하나의 집합으로 합침

print(result)  # 최소 신장 트리의 가중치 합 출력
```

> `Prim` 이용한 문제 풀이(복습) 
> 1. link에 각 간선의 정보를 양방향으로 저장한다.
> 2. `heap` 구조를 활용하여 방문안한 곳 중 가장 작은 가중치의 정점을 탐색한다.(그리디 로직)

```py
from heapq import heappush, heappop

def MST(start):
    pq = []
    heappush(pq, (0, start))
    mst = [0] * (V + 1)
    weight_sum = 0
    while pq:
        weight, now = heappop(pq)
        if mst[now]:
            continue
        mst[now] = 1
        weight_sum += weight
        for to in link[now]:
            next_w, nxt = to
            if mst[nxt]:
                continue
            else:
                heappush(pq, (next_w, nxt))
    print(weight_sum)
V, E = map(int, input().split())
link = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    A, B, C = map(int, input().split())
    link[A].append([C, B])
    link[B].append([C, A])
MST(1)
```

#### 🧰 백준 1799 비숍
> `백트래킹`을 통해 푸나, 핵심은 검은판과 하얀판을 나누기
> 1. 대각선 순으로 탐색 
>   - diag : 같은 대각선(우하향) 상에 놓여있을 때, True 표시
>   - open : 착수 가능한 부분(우상향) 즉, 행과 열정보 저장
> 2. 검은 판과 하얀 판을 각 비교하기 위해 k+2하면서 탐색
```python
def BT(k, cnt):
    global ans
    # 마지막 대각선에 다다르면 종료
    if k == 2*N-1:
        ans = max(ans, cnt); return

    # 가지치기
    if ans >= (cnt + (2*N-k)//2): return

    # 가능한 부분 순회
    for i, j in open[k]:
        # 착수 후 다음 대각선 탐색
        if not diag[i-j]:
            diag[i-j] = True
            BT(k+2, cnt+1)
            diag[i-j] = False

    # 미착수 후 다음 대각선 탐색
    BT(k+2, cnt)

N = int(input())
grid=[list(map(int, input().split())) for _ in range(N)]
diag = [False] * (2*N-1)

# 착수 가능한 부분 저장
open = [[] for _ in range(2*N-1)]
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            open[i+j].append([i, j])

# 홀수번째 대각선과 짝수번째 대각선을 분리하여 백트래킹 진행
ans = 0
BT(0, 0)
BT(1, ans)
print(ans)
```
> 2. 행,열 순으로 탐색
```py
import sys
import copy
input =sys.stdin.readline

# 대각선 방향 정의
dr = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# 색깔에 따라 보드의 색을 변환하는 함수
def exceptcolor(arr, color):
    for i in range(N):
        for j in range(N):
            if color == 'white':
                if (i + j) % 2 == 0:  # 흰색 영역에 있는 칸을 0으로 설정
                    arr[i][j] = 0
            if color == 'black':
                if (i + j) % 2 != 0:  # 검은색 영역에 있는 칸을 0으로 설정
                    arr[i][j] = 0

# 해당 위치에 말을 놓을 수 있는지 확인하는 함수
def is_possible(x, y, arr):
    for i in range(4):
        dx, dy = dr[i]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == -1:  # 해당 방향으로 퀸이 있으면 놓을 수 없음
                return False
            nx += dx;ny += dy
    return True

# 백트래킹을 이용한 재귀적 탐색 함수
def back(x, y, arr, cnt):
    global max_cnt

    if x >= N:
        max_cnt = max(cnt, max_cnt)  # 최대 퀸의 개수 업데이트
        return

    if y >= N:
        back(x + 1, 0, arr, cnt)
        return

    if arr[x][y] == 1 and is_possible(x, y, arr):
        arr[x][y] = -1  # 퀸을 놓은 곳을 -1로 표시
        back(x, y + 1, arr, cnt + 1)  # 다음 열로 이동하여 탐색 계속
        arr[x][y] = 1  # 백트래킹

    back(x, y + 1, arr, cnt)  # 해당 칸에 퀸을 놓지 않고 다음 칸으로 이동하여 탐색

# 보드의 크기 입력
N = int(input())

# 보드 상태 입력
board = [list(map(int, input().split())) for i in range(N)]

white_board = copy.deepcopy(board)
black_board = copy.deepcopy(board)

exceptcolor(white_board,'black')
exceptcolor(black_board,'white')
result = 0  # 결과값 초기화

# 흰색과 검은색 영역에 대해 각각 탐색
for board_ in [copy.deepcopy(board), copy.deepcopy(board)]:
    max_cnt = 0  # 각 색깔별 최대 퀸의 개수 초기화
    back(0, 0, board_, 0)  # 백트래킹을 이용한 탐색 시작
    result += max_cnt  # 최대 퀸의 개수를 결과값에 더함

# 결과 출력
print(result)

```
#### ⚽ 백준 1987 알파벳
> `백트래킹` 이용
> 기존 백트래킹과 다른 점 : visited의 범위를 26으로 제한(알파벳 수)

```python
# 이동 방향 정의 (아래, 오른쪽, 위, 왼쪽)
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# DFS를 이용하여 탐색하는 함수
def back(x, y, visited, cnt):
    global max_cnt
    if max_cnt < cnt:  # 현재까지의 최대 칸 수 업데이트
        max_cnt = cnt

    for i in range(4):  # 네 방향에 대해서
        nx = x + dr[i][0]
        ny = y + dr[i][1]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(arr[nx][ny]) - ord('A')]:
            # 배열 범위를 벗어나지 않고, 방문하지 않은 알파벳인 경우
            visited[ord(arr[nx][ny]) - ord('A')] = True  # 방문 표시
            back(nx, ny, visited, cnt + 1)  # DFS 재귀 호출
            visited[ord(arr[nx][ny]) - ord('A')] = False  # 방문 해제 (백트래킹)

# 행과 열의 수 입력
R, C = map(int, input().split())

# 보드 상태 입력
arr = [input() for _ in range(R)]

# 알파벳 방문 여부를 나타내는 리스트 초기화
visited = [False] * 26  # 알파벳은 총 26개

max_cnt = 0  # 최대 칸 수 초기화
visited[ord(arr[0][0]) - ord('A')] = True  # 시작 지점 알파벳 방문 표시

# DFS 시작
back(0, 0, visited, 1)

# 결과 출력
print(max_cnt)
```
> visited 대신 memoization을 활용하여 최대 cnt를 구함
```py   
import sys

# 이동 방향 정의 (아래, 오른쪽, 위, 왼쪽)
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# DFS를 이용하여 탐색하는 함수
def back(x, y, visited, cnt):
    global max_cnt
    if max_cnt < cnt:  # 현재까지의 최대 칸 수 업데이트
        max_cnt = cnt

    for i in range(4):  # 네 방향에 대해서
        nx = x + dr[i][0]
        ny = y + dr[i][1]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(arr[nx][ny]) - ord('A')]:
            # 배열 범위를 벗어나지 않고, 방문하지 않은 알파벳인 경우
            visited[ord(arr[nx][ny]) - ord('A')] = True  # 방문 표시
            back(nx, ny, visited, cnt + 1)  # DFS 재귀 호출
            visited[ord(arr[nx][ny]) - ord('A')] = False  # 방문 해제 (백트래킹)

# 행과 열의 수 입력
R, C = map(int, input().split())

# 보드 상태 입력
arr = [input() for _ in range(R)]

# 알파벳 방문 여부를 나타내는 리스트 초기화
visited = [False] * 26  # 알파벳은 총 26개

max_cnt = 0  # 최대 칸 수 초기화
visited[ord(arr[0][0]) - ord('A')] = True  # 시작 지점 알파벳 방문 표시

# DFS 시작
back(0, 0, visited, 1)

# 결과 출력
print(max_cnt)
```

#### 🖌 백준 1991 트리 순회 
> 전위, 중위, 후위 순회를 각각 정의하는데 `재귀`로 구현

```python
import sys

# 표준 입력을 'input.txt'에서 읽도록 재지정
sys.stdin = open('input.txt')

# 트리의 노드 수 입력
N = int(input())

# 전위 순회 함수
def preorder(now):
    if trees.get(now):  # 현재 노드에 자식이 있는 경우
        print(now, end='')  # 현재 노드 출력
        preorder(trees[now][0])  # 왼쪽 자식을 기준으로 재귀 호출
        preorder(trees[now][1])  # 오른쪽 자식을 기준으로 재귀 호출

# 중위 순회 함수
def inorder(now):
    if trees.get(now):  # 현재 노드에 자식이 있는 경우
        inorder(trees[now][0])  # 왼쪽 자식을 기준으로 재귀 호출
        print(now, end='')  # 현재 노드 출력
        inorder(trees[now][1])  # 오른쪽 자식을 기준으로 재귀 호출

# 후위 순회 함수
def postorder(now):
    if trees.get(now):  # 현재 노드에 자식이 있는 경우
        postorder(trees[now][0])  # 왼쪽 자식을 기준으로 재귀 호출
        postorder(trees[now][1])  # 오른쪽 자식을 기준으로 재귀 호출
        print(now, end='')  # 현재 노드 출력

# 트리 구성
trees = {}
for i in range(N):
    now, left, right = input().split()
    trees[now] = [left, right]

# 전위 순회 출력
preorder('A')
print()
# 중위 순회 출력
inorder('A')
print()
# 후위 순회 출력
postorder('A')

``` 

#### 🎙 백준 2252 줄 세우기
> 첫번째, `위상정렬`을 이용(단방향 그래프)
> 1. 연결정보를 `연결리스트` 형태로 담는다(딕셔너리에 값이 리스트인 형태)
> 2. 그래프를 연결정보를 바탕으로 각 진입차수를 계산한다.
> 3. 진입차수가 0인것부터 queue에 초기값으로 담는다.
> 4. 각 큐를 순회하면서 연결된 곳의 진입차수를 하나씩 깎는다.
> 5. 그 다음 진입차수가 0인 것을 순회하면서 정렬한 정보를 result에 담는다.

```python
from collections import defaultdict, deque
def topological_sort(graph):
    # 진입 차수 계산
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    # 진입 차수가 0인 노드를 큐에 삽입
    queue = deque([node for node in graph if in_degree[node] == 0])
    # 결과를 담을 리스트
    result = []
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 꺼내 결과에 추가
        node = queue.popleft()
        result.append(node)
        # 해당 노드와 연결된 모든 노드의 진입 차수를 감소시키고, 0이 되면 큐에 추가
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    # 사이클이 있는 경우에는 모든 노드를 방문하지 못하므로 None 반환
    if len(result) != len(graph):
        return None
    return result

# 그래프 정의 (인접 리스트 형태)
N,M = map(int,input().split())
graph = {i: [] for i in range(1,N+1)}
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)

# 위상 정렬 수행
result = topological_sort(graph)
print(*result)
```
> 두번째, `DFS` 활용
> 1. 그래프를 단방향으로 제작
> 2.  `DFS`를 통해 stack에 쌓는다.
> 3. stack에서 역순으로 조회한다. 
```py
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
stack = []

# 그래프 제작
for _ in range(M):
    f, b = map(int, input().split())
    graph[f].append(b)

def DFS(now):
    visit[now] = True
    # 그래프 순회
    for next in graph[now]:
        if not visit[next]:
            DFS(next)
    # 제일 우선순위가 낮은 것부터 스택에 저장
    stack.append(now)

# 각 번호 순회하며 방문하지 않았으면 DFS 가동
for i in range(1, N+1):
    if not visit[i]: DFS(i)

# 우선순위가 높은 것부터 출력
while stack:
    print(stack.pop(), end=' ')
```

#### 👔 백준 5567 결혼식
> `depth`가 2인 `BFS` 구현
```python
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [1, 1] + [0] * (n-1)
Q = deque([1])
cnt = 0

# 그래프 제작
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 너비우선탐색
while Q:
    now = Q.popleft()

    # 친구의 친구까지만 허용
    if dist[now] == 3:
        continue

    # 그래프 순회
    for next in graph[now]:
        if not dist[next]:
            dist[next] = dist[now] + 1
            Q.append(next)
            cnt += 1

print(cnt)
```
> 두번째 방법 : `중첩반복문` 활용
> 1. 양방향 그래프로 친구 관계 형성
> 2. 순차적으로 방문한 곳을 체크하면서 친구와 친구의 친구 찾기
> 3. 전체 길이에서 본인을 제외한 친구들 갯수 출력
```py
n = int(input())
m = int(input())
visited = [0, 1] + [0] * (n-1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 친구 찾기
for i in graph[1]:
    if not visited[i]:
        visited[i] = 1
    
    # 친구의 친구 찾기
    for j in graph[i]:
        if not visited[j]:
            visited[j] = 1

print(sum(visited)-1)
``` 
---
#### 📀 백준 11729 하노이탑 이동 순서
> 목표 : n개의 원판을 A 에서 C로 옮기는 것이 목표
> 1. A : n-1개의 원판 → B로 옮김 (A : 1개 / B: n-1개 / C: 0개)
> 2. A : 1개의 원판(젤 큰 원판) → C로 옮김 (A : 0개 / B: n-1개 / C: 1개)
> 3. B : n-1개의 원판 → C로 옮김 (A : 0개 / B: 0개 / C : n개)
>   > → n-1개를 1개로 치환하면 쉽게 생각할 수 있음.
>   > → n개부터 시작했을 때, 재귀함수를 이용하면 n-1, n-2 ... 1개까지 내려와서 이동을 하게 됨

```python
# 하노이 탑 문제를 해결하는 재귀 함수
def hanoi(n, start, end):
    # 기본 경우: 디스크가 하나만 있는 경우, 시작 기둥에서 끝 기둥으로 이동
    if n == 1:
        print(start, end)  # 시작 기둥에서 끝 기둥으로 디스크 이동
        return

    # 시작 기둥에서 남은 n-1개의 디스크를 보조 기둥으로 이동
    hanoi(n - 1, start, 6 - start - end)

    # 시작 기둥에서 가장 큰 디스크를 끝 기둥으로 이동
    print(start, end)

    # 보조 기둥에서 남은 n-1개의 디스크를 끝 기둥으로 이동
    hanoi(n - 1, 6 - start - end, end)

# 표준 입력에서 디스크의 개수를 읽음
n = int(input())

# 문제를 해결하는 데 필요한 총 이동 횟수를 계산하고 출력
print(2 ** n - 1)

# 하노이 함수를 호출하여 하노이 탑 문제를 해결
hanoi(n, 1, 3)

```

#### 🧏‍♀️ 백준 14427 수열과 쿼리 15
> `세그먼트 트리` 활용
> 1. 이진 트리 자료구조를 활용하여 각 초기값을 설정한다.
>   - init함수는 리프노드일 경우에는 그 인덱스에 매칭되는 수 자체를 반환한다.
>   - 점차 올라가면서 두 자식노드 간의 최소값을 부모노드에 저장한다.
> 2. 값을 갱신하면 그 노드부터 부모노드에 이르기까지 영향을 미치기 때문에 전부 변경이 필요
> ex) 5 4 3 2 1에 init 함수 실행시 tree는
> [0, [1, 5], [3, 3], [1, 5], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
> 3. 최솟값을 찾는 함수는 find_min 함수이며, 트리 내의 최소값을 반환한다.
> 4. update함수는 현재 노드부터 루트노드까지 갱신할값 인덱스와 새값을 넣으면 그렇게 갱신

```python
 Segment Tree 초기화 함수
def init(start, end, index):
    # 만약 시작과 끝이 같으면 해당 위치의 값을 트리에 저장
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start + end) // 2
        # 좌측과 우측 자식으로 분할하여 재귀적으로 트리를 채움
        tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]

# 값 갱신 함수
def update(start, end, index, w, v):
    # 범위를 벗어나는 경우에는 종료
    if w < start or w > end:
        return
    # 리프 노드에 도달한 경우
    if start == end:
        tree[index] = v
        return tree[index]
    mid = (start + end) // 2
    # 좌측과 우측 자식으로 분할하여 갱신 대상이 있는 쪽을 선택하여 재귀 호출
    update(start, mid, index * 2, w, v)
    update(mid + 1, end, index * 2 + 1, w, v)
    # 갱신된 자식 노드들 중에서 최소값을 부모 노드에 저장
    tree[index] = min(tree[index * 2], tree[index * 2 + 1])

# 최소값 찾기 함수
def find_min(start, end, index, left, right):
    # 범위를 벗어나는 경우 최대값 반환
    if start > right or end < left:
        return [sys.maxsize, sys.maxsize]
    # 범위가 완전히 속하는 경우 현재 노드의 값을 반환
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    # 좌측과 우측 자식으로 분할하여 최소값을 찾음
    return min(find_min(start, mid, index * 2, left, right), find_min(mid + 1, end, index * 2 + 1, left, right))

# 입력 받기
N = int(input())
tmp = list(map(int, input().split()))
arr = []
for i in range(N):
    # (값, 인덱스) 형태로 리스트에 저장
    arr.append([tmp[i], i + 1])
tree = [0] * (N * 4)

# Segment Tree 초기화
init(0, N - 1, 1)
print(tree)
# 쿼리 처리
for j in range(int(input())):
    tmp = list(map(int, input().split()))
    if tmp[0] == 2:
        # 2번 쿼리인 경우 최소값 출력
        print(find_min(0, N - 1, 1, 0, N - 1)[1])
    elif tmp[0] == 1:
        # 1번 쿼리인 경우 값 갱신 및 트리 재구성
        arr[tmp[1] - 1][0] = tmp[2]
        update(0, N - 1, 1, tmp[1] - 1, arr[tmp[1] - 1])

```
> `heap`의 우선순위 큐를 활용한 문제풀이
> 1. 세그먼트 트리와 동일하게 (값, 인덱스) 튜플을 힙에 저장한다.
> 2. 쿼리번호를 받는다.
>   > 1인 경우, 해당 인덱스와 갱신할 값을 힙에 추가한다.
>   > - 그런 경우에 같은 인덱스에 값이 두 개 이상이 된다.
>   > 2인 경우, `heappop`메서드를 통해 최소값을 출력한다.
>   > - list와 비교하여 찐 최소값이 맞는지 확인한다. 맞으면 출력한다.
```py
from heapq import *  # heapq 모듈 import

N = int(input())  # 배열의 길이 입력
list_ = list(map(int, input().split()))  # 배열 입력
M = int(input())  # 쿼리 개수 입력

q = [(list_[i], i) for i in range(N)]  # (값, 인덱스) 튜플을 힙에 저장
heapify(q)  # 힙 속성 유지

for _ in range(M):  # 쿼리 개수만큼 반복
    query, *temp = list(map(int, input().split()))  # 쿼리 입력

    if query == 1:  # 쿼리가 1인 경우
        list_[temp[0] - 1] = temp[1]  # 배열의 해당 인덱스 값을 갱신
        heappush(q, (temp[1], temp[0] - 1))  # 힙에 새로운 값을 추가
    else:  # 쿼리가 2인 경우
        while list_[q[0][1]] != q[0][0]:  # 최솟값이 배열에 있는지 확인
            heappop(q)  # 최솟값이 배열에 없으면 힙에서 제거

        print(q[0][1] + 1)  # 최솟값의 인덱스 출력

```

#### ❤️‍🔥 백준 15903 카드 합체 놀이
> `heap`을 활용하여 최소값 두개를 더해서 다시 heappush로 넣어줌
```python
# 입력 받기
n, m = map(int, input().split())  # 카드의 개수와 합체 연산의 수 입력
heap = list(map(int, input().split()))  # 카드의 가치 입력
heapify(heap)  # 카드의 가치를 최소 힙으로 변환

# 합체 연산 수행
for i in range(m):
    a = heappop(heap)  # 가장 가치가 작은 카드 꺼내기
    b = heappop(heap)  # 두 번째로 가치가 작은 카드 꺼내기
    heappush(heap, a + b)  # 두 카드를 합친 가치를 다시 최소 힙에 추가
    heappush(heap, a + b)  # 합친 결과를 다시 최소 힙에 추가하여 중복해서 더할 수 있도록 함

# 최종 결과 출력
print(sum(heap))  # 합체 연산을 모두 수행한 후 카드들의 가치의 합 출력
```

#### ❤️‍🔥 백준 17626 Four Squares
> `DP` 문제인듯 하면서 브루트포스 문제
> 횟수를 줄이는 것이 관건
```py
n = int(input())

# 제곱 수는 1로 배열에 저장
DP = [4 if i**0.5%1 else 1 for i in range(n+1)]

# 제곱 수이면 패스
if DP[n] == 1: exit(print(1))

# 배열 순회
for i in range(1, n+1):
    # 최대 제곱근까지 순회
    for j in range(1, int(i**0.5)+1):
        # 최소 횟수 저장
        DP[i] = min(DP[i], DP[i-j**2] + 1)

print(DP[n])
```
