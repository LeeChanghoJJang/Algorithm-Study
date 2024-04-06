## Algorithm Study 8회차 회의 (24.3.30.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 3월 30일 토요일 아침 9시 반  
        - 방식 : 김해 커피팀버  

    나. 차주 예정 일정
        - 시간 : 4월 6일 토요일 아침 9시  
        - 방식 : 디스코드

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 10문제
    다. 난이도 : 최대 백준 골드 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

### 🤢 이번회차 풀이 문제
   ###### 1. 창호
    - 백준 2098 외판원 순회(골드 1)
    - 백준 1541 잃어버린 괄호(실버 2)
   ###### 2. 예리
    - 백준 1774 우주신과의 교감(골드 3)
    - 백준 11286 절대값 힙(실버 1)
   ###### 3. 경태
    - SOFTEER 염기서열 커버(lv.3)
    - 백준 1620 나는야 포켓몬 마스터 이다솜(실버 4) 
   ###### 4. 동현
    - 백준 16236 아기상어(골드 3)
    - 백준 1072 게임(실버 3)
   ###### 5. 상현
    - 백준 27978 보물 찾기2(골드 3)
    - 백준 4358 생태학(실버 2)
  
### 🎁 문제 선정
   ###### 1. 창호
    - 백준 2665 미로만들기(골드 4)
    - 백준 2075 N번째 큰수(실버 2)
   ###### 2. 예리
    - 백준 15681 트리와 쿼리(골드 5)
    - 백준 1654 랜선 자르기(실버 2)
   ###### 3. 경태
    - 백준 1700 멀티탭 스케줄링(골드 1)
    - 백준 2667 단지번호 붙이기(실버 1) 
   ###### 4. 동현
    - 백준 16974 레벨 햅버거(골드 5)
    - 백준 1629 곱셈(실버 1)
   ###### 5. 상현
    - 백준 21609 상어 중학교(골드 2)
    - 백준 17086 아기 상어 2(실버 2)

### 🏅 스터디 내용 
#### 🎈 백준 1072 게임
> 첫번째 :`이진탐색` 알고리즘 활용
> 1. 현재 확률을 정수로 구한다.
> 2. 승률이 100이 될순 없으므로, 현재확률이 98보다 높으면 -1을 출력
> 3. 현재 총 게임횟수 안에서 이진탐색을 하여, 최초로 확률이 올라가는 시점을 포착한다.

```python
# X : 총 게임횟수 / Y : 이긴 게임 횟수
X, Y = map(int, input().split())
Z = 100*Y//X
l, r = 0, X
ans = X

if Z > 98:
    print(-1)
else:
    # 최대값과 최소값이 엇갈리지 않는 동안
    while l <= r:
        mid = (l+r)//2
        # mid번 더 해서 확률이 바뀌면 최대값을 감소
        if 100*(Y+mid)//(X+mid) > Z:
            ans = mid
            r = mid - 1
        # 확률이 바뀌지 않으면 최소값을 증가
        else:
            l = mid + 1
    print(ans+1)
```
> 두번째 : 수학적으로 계산 
> 1. 현재 확률 now를 구한다.
> 2. 최소 1만 오르면 되므로, 목표확률 = 현재확률 +1 로 잡는다.
> 3. 목표확률이 100미만 인 경우, 목표확률식을 구하는 계산식을 역산하여 추가 횟수를 구한다.
> 4. 그 외의 경우 -1을 출력한다.
```python
import sys
import math
sys.stdin = open('input.txt')

# 입력 받기
X,Y = map(int,input().split())

# 현재 승률 계산
now = int(Y*100/X)

# 목표 승률 설정 (현재 승률에서 1% 증가)
target = now + 1

# 목표 승률이 0 초과 100 미만인 경우
if 0 < target < 100:
    # 게임 횟수 계산
    added = ((Y - X) * 100) / (target-100) - X
else:
    # 목표 승률이 0 또는 100인 경우, 게임 횟수를 증가시킬 수 없음
    print(-1)
    exit()

# 최소 게임 횟수 계산 및 출력
print(max(1,math.ceil(added)))
```

#### 🧰 백준 1541 잃어버린 괄호 
> `split` 메서드를 적극 활용하여 최소값 계산(`그리디`)

```python
# 입력 받기
arr = list(input().split('-'))

# 첫 번째 숫자는 더하고 시작
result = sum(map(int, arr[0].split('+')))

# 나머지 숫자들은 빼줌
for i in arr[1:]:
    result -= sum(map(int, i.split('+')))

# 결과 출력
print(result)
```

#### ⚽ 백준 1620 나는야 포켓몬 마스터 이다솜
> `딕셔너리`를 이용한 분기 탐색 
1. 포켓몬이름 -> 숫자 / 숫자 -> 포켓몬이름의 각 딕셔너리를 만든다.
2. 숫자면 전자에, 문자면 후자에 딕셔너리 키값을 넣어 값을 도출한다.

```python
n, m = map(int, input().split())
pokemon_name = {}
pokemon_idx = {}

for i in range(1, n+1):
    char = input().strip()
    pokemon_name[char] = i
    pokemon_idx[i] = char

for _ in range(m):
    char = input().strip()
    if char.isdigit():
        print(pokemon_idx[int(char)])
    else:
        print(pokemon_name[char])
```

#### 🖌 백준 1774 우주신과의 교감
> 첫번째 방법 : `프림` 알고리즘 활용
> 1. 각 정점별 거리를 구해 2차원 배열에 담는다.
> 2. 기존 연결된 통로는 비용을 0으로 담는다.
> 3. 최소 스패닝 트리를 구하기 위한 프림 알고리즘을 쓴다.
>   - 최소힙 구조에 시작점을 넣는다.
>   - 최소힙에서 요소를 하나 꺼내어 순회하여, 방문하지 않았으면 해당 지점의 비용을 가산한다.

```python
from heapq import heappush, heappop

n, m = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]

# 2차원 배열 그래프 생성
adj = [[0] * n for _ in range(n)]
for i in range(n-1):
    for j in range(i, n):
        x1, y1 = pos[i]; x2, y2 = pos[j]
        dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
        adj[i][j] = dist; adj[j][i] = dist
# 연결된 통로의 비용 0으로 변환
for _ in range(m):
    i, j = map(int, input().split())
    adj[i-1][j-1] = adj[j-1][i-1] = 0

# Prim Algorithm
MST = [0] * n
Q = []; heappush(Q, (0, 0)); ans = 0
while Q:
    weight, now = heappop(Q)
    if MST[now]: continue
    MST[now] = 1
    ans += weight

    for next in range(n):
        if now != next and not MST[next]:
            heappush(Q, (adj[now][next], next))

print(f'{ans:.2f}')
``` 
> 두번째 방법 : `크루스칼` 알고리즘 활용
> 1. `find` : 두 무리의 대표노드(최상위 노드)를 찾는 함수(두 집단 동일성 비교) 
> 2. `union` : 두 집단을 합치는 함수(대표노드가 같아짐)
> 3. `cal_distance` : 비용을 계산하는 함수
> 4. 가능한 모든 간선의 비용을 계산하여 리스트에 비용이 적은순으로 담는다.(좌표 포함)
> 5. 기존에 연결된 건이면 `union`을 이용해 미리 연결해둔다.
> 6. 적은 비용부터 순회하여 `find`로 서로 두 집단이 다르면, `union`으로 합쳐서, 최종 비용을 계산해준다.  
```py
import sys
sys.stdin = open('input.txt')
# 두 점 사이의 거리 계산 함수
def cal_distance(loc1, loc2):
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# 루트 노드를 찾는 함수 (경로 압축)
def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 집합을 합치는 함수 (작은 집합을 큰 집합에 합침)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
N, M = map(int, input().split())
parent = list(range(N + 1))  # 각 정점의 부모를 저장할 리스트
edges = [0] * (N + 1)  # 각 정점의 좌표를 저장할 리스트

# 정점의 좌표 입력 받기
for i in range(1, N + 1):
    edges[i] = list(map(int, input().split()))

# 이미 연결된 정점들을 합치기
for _ in range(M):
    a, b = map(int, input().split())
    union(parent, a, b)

# 가능한 모든 간선 구하기
possible = []
for i in range(1, len(edges) - 1):
    for j in range(i + 1, len(edges)):
        possible.append([cal_distance(edges[i], edges[j]), i, j])

# 거리 순으로 간선 정렬
possible.sort()

result = 0
# Kruskal 알고리즘을 통해 최소 신장 트리 구하기
for cost, x, y in possible:
    if find(parent, x) != find(parent, y):  # 사이클을 형성하지 않으면 연결
        union(parent, x, y)
        result += cost

# 결과 출력
print(f'{result:.2f}')

```
#### 🎙 백준 2098 외판원 순회
> 외판원 순회 문제(최초)
> `정의` : 쉽게 말하면, 가장 비용이 적은 `순환 구조`를 찾는 알고리즘으로, `DFS`의 원리와 `비트마스킹`을 이용한다.
> 1. 각 정점사이 비용을 2차원 배열에 저장한다. 
> 2. visited 를 비트마스킹으로 구현한다.
> 3. 시작점은 아무거나 상관없으며, `DFS`를 구현한다.
> 4. 현재 간선의 비용이 0여서 갈 수 없거나 방문한 루트면 넘긴다.
> 5. 모두 방문했으면 시작점으로 돌아오는 값까지 합쳐서 최소비용을 갱신하여 저장한다. 
> 6. 그 당시 시점에 현재 지점을 방문한 적이 있으면 dp에 저장하여 이미 계산된 경우에는 바로 계산된 비용을 돌려준다. 
```python
import sys
sys.stdin = open('input.txt')
N = int(input())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = {}

def DFS(now, visited):
    # 모든 도시를 방문한 경우
    if visited == (1 << N) - 1:
        # 다시 출발 도시로 갈 수 있는 경우 출발 도시까지의 비용 반환
        if world[now][0]:
            return world[now][0]
        else:
            # 갈 수 없는 경우 무한대 반환 (이 경로가 최소비용으로 채택되지 않게)
            return int(1e9)

    # 이전에 계산된 경우 결과 반환
    if (now, visited) in dp:
        return dp[(now, visited)] # now까지 방문한 최소 비용

    min_cost = int(1e9)
    for next in range(1, N):
        # 비용이 0이어서 갈 수 없거나, 이미 방문한 루트면 무시
        if world[now][next] == 0 or visited & (1 << next):
            continue
        cost = DFS(next, visited | (1 << next)) + world[now][next]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost  # 현재도시까지 방문한 경우 중에서 최소 비용이 드는 루트의 비용 저장
    return min_cost  # 현재도시까지 방문하는 비용 리턴


print(DFS(0, 1))  # now: 0번째 도시부터 방문, visited: 0번째 도시 방문 처리
```


#### 👔 백준 4358 생태학
> 첫번째 방법 : `Counter` 라이브러리와 입력을 `sys.stdin.readlines()`로 받음 
>   - `sys.stdin.readlines()` : EOFerror를 방지하기 위해
>   - `Counter` : 리스트 안에 있는 요소를 key로, 요소의 갯수를 value로 받는 딕셔너리를 반환  
```python
# 표준 입력을 파일로 변경
sys.stdin = open('input.txt')

# 입력을 한 번에 읽기
lines = sys.stdin.readlines()

# Counter를 사용하여 단어 빈도 계산
info = Counter(lines)
total = sum(info.values())

# 결과 출력
for key in sorted(info.keys()):
    print(f'{key.strip()} {info[key]*100/total:.4f}')

```
> 두번째 방법 : try ~ except 구문 활용
```py
dict_ = {}
total = 0

while True:
    try:
        name = input().strip()
    except EOFError:
        break

    if name in dict_:
        dict_[name] += 1
    else:
        dict_[name] = 1
    total += 1

list_ = list(dict_.items())
list_.sort(key = lambda x : x[0])

[print(f'{wood[0]} {round(wood[1] * 100 / total, 4):.4f}') for wood in list_]
``` 
---
#### 📀 백준 11286 절대값 힙 
> 최소힙 문제 
> 1. 절대값이 가장 작은 숫자 중 가장 작은 숫자를 꺼내야 하므로, heap에 `abs(x)`, `x//abs(x)`(값, 부호)를 넣어준다.
> 2. 차례대로 pop을 해주고, 없으면 0을 출력한다.
```python
from heapq import heappush, heappop

Q = []
for _ in range(int(input())):
    x = int(input())
    if x: heappush(Q, [abs(x), x//abs(x)])
    else:
        if Q: x, y = heappop(Q); print(x*y)
        else: print(0)
```

#### 🧏‍♀️ 백준 16236 아기상어
> 시뮬레이션 및 구현 문제
> 1. `BFS`를 활용하여 다음 먹잇감을 탐색한다.
>   - 크기가 작고, 범위 안에 들어오며, 방문하지 않았으면 먹잇감 후보에 등극
>   - 거리와 좌표를 저장하고, 거리가 가까운 물고기를 찾는다.
> 2. 시작점은 값이 9인 좌표이며, 자신의 크기만큼 먹을때 마다 사이즈를 키운다.
> 3. 먹을 게 없을 때 종료하며 시간을 반환한다. 
```python
from collections import deque

def BFS(i, j, size):
    Q = deque([[i, j]])
    dist = [[0] * N for _ in range(N)]
    dist[i][j] = 1
    fish = []

    while Q:
        i, j = Q.popleft()
        for di, dj in go:
            ni, nj = i + di, j + dj

            # 범위, 방문, 크기 같거나 작음 -> 이동 가능
            if 0<=ni<N and 0<=nj<N and dist[ni][nj] == 0 and sea[ni][nj] <= size:
                dist[ni][nj] = dist[i][j] + 1
                Q.append([ni, nj])

                # 상어 크기보다 작으면 먹잇감 후보에 등극
                if 0 < sea[ni][nj] < size:
                    # 우선순위 : 가까움 - 가장 위 - 가장 왼쪽
                    fish.append([dist[ni][nj]-1, ni, nj])

        # 거리가 가까운 물고기만 찾으면 되므로 많이 찾을 필요 없음
        if len(fish) > 2: break

    if fish: return sorted(fish)[0]
    else: return

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
go = ((-1, 0), (0, -1), (0, 1), (1, 0))
time, size, feed = 0, 2, 2

# 초기 위치 확인
def search():
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                sea[i][j] = 0
                return i, j
i, j = search()

while True:
    # 사냥할 물고기 탐색
    info = BFS(i, j, size)

    # 사냥 가능한 물고기가 없다면 종료
    if not info: break

    # 물고기 먹고 쑥쑥 자라나자
    dist, i, j = info
    sea[i][j] = 0
    time += dist
    feed -= 1

    # 먹이 할당량 충족
    if not feed:
        size += 1
        feed = size

print(time)
```
#### ❤️‍🔥 백준 27978 보물찾기 2
> 첫번째 : `Dijkstra` + `델타탐색` 활용 
> 1. 8방향 델타 탐색한다.
> 2. 범위, 암초, 비용을 고려해서 전단계보다 비용이 작다면 비용을 갱신하여 2차원 배열에 저장
>   - 단, 우측은 비용 0, 좌측은 비용 + 1 
> 3. 보물발견하면 갱신된 비용을 반환하여 끝.
```python
from heapq import heappop, heappush

di = (0, 1, -1, 1, -1, 1, -1, 0)
dj = (1, 1, 1, 0, 0, -1, -1, -1)
H, W = map(int, input().split())
sea = [input().rstrip() for _ in range(H)]

# 배 위치 검색
def ship():
    for i in range(H):
        for j in range(W):
            if sea[i][j] == 'K':
                return i, j
i, j = ship()

# 다익스트라
dist = [[10**8] * W for _ in range(H)]
dist[i][j] = 0
Q = [[0, i, j]]
while Q:
    w, i, j = heappop(Q)

    if dist[i][j] < w:
        continue

    for k in range(8):
        ni, nj = i + di[k], j + dj[k]

        # 오른쪽으로 가면 연료 소모 없음
        if k < 3: next_w = w
        else: next_w = w + 1

        # 범위, 암초, 비용 고려
        if 0<=ni<H and 0<=nj<W and sea[ni][nj] != '#' and dist[ni][nj] > next_w:
            dist[ni][nj] = next_w
            heappush(Q, [next_w, ni, nj])

            # 보물 발견하면 끝
            if sea[ni][nj] == '*':
                exit(print(dist[ni][nj]))

print(-1)
```
> 두번째 : `BFS` 활용
> 1. 시작점 좌표 K와 끝점좌표 *을 동시에 찾아놓는다. 
> 2. `BFS`를 사용하여 범위 내에 들어오며, '*','.'인 경우에만 탐색한다.
>    - 단, 우측일때는 0, 좌측일 때는 +1하여 비용이 적은 경우를 distance에 저장
> 3. 전부 순회했을 때, 끝점이 초기값일 가능성이 있으므로, 초기값이라면 -1로 반환하도록 조건설정
```python
# 8개의 방향에 대한 상대 좌표
dr = [(1,0), (-1,0), (0,-1), (-1,-1), (1,-1), (0,1), (-1,1), (1,1)]

def BFS(start):
    # 시작 지점으로부터 BFS 탐색을 시작한다.
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        # 8방향으로 이동하며 탐색한다.
        for i in range(8):
            nx = x + dr[i][0]  # 다음 위치의 행 좌표
            ny = y + dr[i][1]  # 다음 위치의 열 좌표
            # 다음 위치가 유효한 범위 내에 있고, 갈 수 있는 곳이라면
            if 0 <= nx < H and 0 <= ny < W and treasure[nx][ny] in ['.', '*']:
                # 거리를 갱신한다. 기존보다 왼쪽 방향일 경우 거리에 1을 더한다.
                if distance[nx][ny] > distance[x][y] + (i < 5):
                    distance[nx][ny] = distance[x][y] + (i < 5)
                    # 다음 위치를 큐에 추가하여 계속해서 탐색한다.
                    queue.append([nx, ny])
    # 보물에 도달할 수 없는 경우 -1을 반환한다.
    return -1 if distance[end[0]][end[1]] == float('inf') else distance[end[0]][end[1]]

# 보물 지도의 세로와 가로 길이를 입력받는다.
H, W = map(int, input().split())
# 보물 지도를 입력받는다.
treasure = [input() for _ in range(H)]

# 각 위치까지의 최소 거리를 저장하는 배열을 초기화한다.
distance = [[float('inf')] * W for _ in range(H)]
# 시작 지점의 좌표를 찾아 거리를 0으로 초기화한다.
for i in range(H):
    for j in range(W):
        if treasure[i][j] == 'K':
            start = (i, j)
            distance[i][j] = 0
            continue

        if treasure[i][j]=='*':
            end = (i, j)
            continue
# BFS 탐색을 수행하고 결과를 출력한다.
print(int(BFS(start)))
```
> `행`단위로 배열돌리기 수행 
```python
from itertools import permutations

# (r, c, s) 회전 연산을 수행하는 함수
def rotation_func(r, c, s):
    for depth in range(s):
        temp1 = temp[r - 1 - (s - depth)][c - 1 - (s - depth)]

        for row in range(r - 1 - (s - depth), r - 1 + (s - depth)):
            temp[row][c - 1 - (s - depth)] = temp[row + 1][c - 1 - (s - depth)]
        for col in range(c - 1 - (s - depth), c - 1 + (s - depth)):
            temp[r - 1 + (s - depth)][col] = temp[r - 1 + (s - depth)][col + 1]
        for row in range(r - 1 + (s - depth), r - 1 - (s - depth), -1):
            temp[row][c - 1 + (s - depth)] = temp[row - 1][c - 1 + (s - depth)]
        for col in range(c - 1 + (s - depth), c - 1 - (s - depth), -1):
            temp[r - 1 - (s - depth)][col] = temp[r - 1 - (s - depth)][col - 1]

        temp[r - 1 - (s - depth)][c - (s - depth)] = temp1

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
rotation_list = [list(map(int, input().split())) for _ in range(K)]
rotation_list = permutations(rotation_list)
min_ = float('inf')

for rotation in rotation_list:
    # 원본 matrix를 변환하지 않기 위해 matrix를 복사하여
    # temp에 저장
    temp = [row[:] for row in matrix]

    for r, c, s in rotation:
        rotation_func(r, c, s)

    min_ = min(min_, min(sum(row) for row in temp))

print(min_)
```
<!-- 염기서열 대기 -->
