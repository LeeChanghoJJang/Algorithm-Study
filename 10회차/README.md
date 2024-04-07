## Algorithm Study 10회차 회의 (24.4.6.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 4월 6일 토요일 아침 9시  
        - 방식 : 디스코드

    나. 차주 예정 일정
        - 시간 : 4월 13일 토요일 아침 9시 30분  
        - 방식 : 김해 커피팀버 

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 10문제
    다. 난이도 : 최대 백준 골드 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 이번 주의 새로운 문제 : 트리DP
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

### 🤢 이번회차 풀이 문제
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
  
### 🎁 문제 선정
   ###### 1. 창호
    - 백준 14567 선수과목(골드 5)
    - 백준 15565 귀여운 라이언(실버 2)
   ###### 2. 예리
    - 백준 1450 냅색문제(골드 1)
    - 백준 7576 토마토(골드 5)
   ###### 3. 경태
    - swea 2477 차량 정비소(A형 대비)
    - 백준 9465 스티커(실버 1)
   ###### 4. 동현
    - 백준 16562 친구비(골드 4)
    - 백준 13335 트럭(실버 1)
   ###### 5. 상현
    - 백준 1326 소트게임(골드 4)
    - 백준 20529 가장 가까운 세 사람의 심리적 거리(실버 1)

### 🏅 스터디 내용 
#### 🎈 백준 1629 곱셈
> 분할정복을 이용한 거듭제곱 활용.(재귀함수)
> 1. a : 밑, b: 곱하는 횟수, c : 결과값을 나눌 수 
> 2. b가 홀수이면 b//2에다가, 한번 더 곱한 a%c를 곱한 함수값을 반환한다.
> 3. b가 짝수이면 b//2를 넣은 함수값을 반환한다.
> 3. b가 1이면 a%c를 반환한다.

```python
def div_conq(a,b,c):
    if b == 1 :
        return a % c
    
    if b % 2 == 1:
        return div_conq(a,b//2,c)**2 * a % c
    
    else :
        return div_conq(a,b//2,c)**2 % c
#### 재귀함수를 통해 10 ** 11 % 12를
    # (((10^2)*10)^2*10)% 12 로 만듬

A,B,C = map(int,input().split())

print(div_conq(A,B,C))
```

> 두번째 : 동일한 로직을 반복문을 통해 구현
```python
# 입력으로 주어진 세 개의 정수를 A, B, C에 할당합니다.
A, B, C = map(int, input().split())

# 모듈러 지수 연산을 효율적으로 수행하는 함수를 정의합니다.
def power_mod(A, B, C):
    # 결과를 저장할 변수를 1로 초기화합니다.
    result = 1
    # base에는 A를 C로 나눈 나머지를 할당합니다.
    base = A % C

    # B가 0보다 클 때까지 반복합니다.
    while B > 0:
        # B가 홀수일 때, 결과에 base를 곱하고 C로 나눈 나머지를 구하여 결과 변수에 할당합니다.
        if B % 2 == 1:
            result = (result * base) % C
        # base를 제곱하고 C로 나눈 나머지를 base 변수에 할당합니다.
        base = (base * base) % C
        # B를 절반으로 나눕니다.
        B //= 2

    # 최종적으로 결과를 반환합니다.
    return result

# 함수를 호출하고 결과를 출력합니다.
print(power_mod(A, B, C))

```

#### 🧰 백준 1654 랜선 자르기 
> `매개변수 탐색` 로직을 이용한 문제 풀이 
> 1. 어떤 시점까지는 조건을 만족하지만, 그 이후에는 조건을 만족하지 않는 경우에서 최대값 찾기
> 2. 그 외에는 이진탐색과 동일
> 3. 아래의 경우, 최대의 랜선길이(최대값)과 조건(랜선 갯수)을 충족하는 지 확인 필요 
```python
K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2
    cnt = sum(cable // mid for cable in cables)

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
```

#### ⚽ 백준 1700 멀티탭 스케쥴링
> `그리디`를 이용한 반복문(`카운트행렬` 이용)
1. 기기가 멀티탭에 꽂혀 있다면 넘어간다.(첫번쨰) 
2. 그 외, 멀티탭에 공간이 있으면 꽂는다.(두번째)
3. 꽂혀 있는 코드 중, 향후 다가오는 미래에 가장 빨리 쓰는 기기의 우선순위를 `use` 배열에 저장한다.(각 코드의 인덱스)
4. 결과적으로 뺄 코드를 정하는데, 멀티탭에 꽂혀있는 기기들을 하나씩 조회하고 아래와 같이 처리한다.
    - 사용할일 없으면 뽑는다.
    - 각 기기의 우선순위를 비교하여 더 뒤에 있으면 뽑는다. 
```python
N, K = map(int, input().split())
apps = list(map(int, input().split()))
tab, cnt = set(), 0

for i, app in enumerate(apps):
    # 멀티탭에 있으면 패스
    if app in tab: continue

    # 멀티탭에 공간이 있으면 꽂음
    if len(tab) < N: tab.add(app)
    else:
        # 꽂혀있는 코드 중 앞으로 언제 다시 사용할 지 체크
        use = [0] * 101
        for j, left_app in enumerate(apps[i:]):
            # not use 쓰는 이유는 순차적으로 가장 빠른 우선순위 저장위함
            if not use[left_app] and left_app in tab:
                use[left_app] = j

        pop_app = 0
        for now_app in tab:
            # 앞으로 사용할 일이 없으면 뽑음
            if not use[now_app]: pop_app = now_app; break
            # 제일 마지막에 사용할 코드 뽑음
            if use[now_app] > use[pop_app]: pop_app = now_app

        tab.remove(pop_app)
        tab.add(app)
        cnt += 1

print(cnt)

```

#### 🖌 백준 2075 N번째 큰수 
> `우선순위 큐`를 활용하여 N번째 큰수 도출
> 1. 규칙에 따라 같은 열에 있는 값들은 이전 행의 값보다 무조건 높음
> 2. 행의 값을 순차적으로 받아, `heapify`를 이용하여 최소힙으로 변환
> 3. N의 길이가 넘을 경우, 최소값을 반환 
```python
from heapq import heappop, heapify

N = int(input())
Q = []

for _ in range(N):
    Q += list(map(int, input().split()))
    heapify(Q)
    while len(Q) > N: heappop(Q)

print(Q[0])
``` 

#### 🎙 백준 2665 미로만들기
> `다익스트라`를 이용한 문제풀이 
> 1. 비용을 `dist` 배열에 저장.(초기값 2*n 설정)
> 2. heap을 정의한다.(각 요소는 비용,x,y으로 이뤄진다.)
> 3. heappop을 통해 최소값을 매번 축출하여, `dist`에 저장된 비용과 비교한다. 
> 4. 인접한 노드를 순회하여 신규비용을 일단 계산한다.
> 5. 이웃노드의 기존 비용과 신규 비용을 비교하여 작은 비용을 저장한다. 

```python
n = int(input())
go = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [list(map(int, input())) for _ in range(n)]
dist = [[2*n] * n for _ in range(n)]; dist[0][0] = 0

Q = [[0, 0, 0]]
while Q:
    # 이동 비용이 가장 적은 이웃 노드부터 방문
    now_cost, i, j = heappop(Q)

    # 현재 노드의 기존 비용과 신규 비용 비교
    if dist[i][j] < now_cost:
        continue

    # 이웃 노드 순회
    for di, dj in go:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            # 이웃 노드의 신규 비용 계산
            next_cost = now_cost + (1 - arr[ni][nj])

            # 이웃 노드의 기존 비용과 신규 비용 비교
            if dist[ni][nj] > next_cost:
                dist[ni][nj] = next_cost
                heappush(Q, [next_cost, ni, nj])

print(dist[-1][-1])
```

#### 👔 백준 2667 단지 번호 붙이기
> 첫번째 방법 : `DFS` 활용
> 1. 1인 경우, 시작점을 0으로 하고, 인접노드를 전부 순회하는 `DFS`를 통해 블록의 크기를 반환한다.
> 2. 해당 값을 리스트에 넣고, 순차적으로 값을 반환한다. 
```python
def DFS(arr, i, j, cnt):
    S = [[i, j]]
    while S:
        i, j = S.pop()
        for di, dj in go:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj]:
                arr[ni][nj] = 0; cnt += 1; S.append([ni, nj])
    return cnt

n, ans = int(input()), []
go = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            arr[i][j] = 0
            ans.append(DFS(arr, i, j, 1))

print(len(ans))
for i in sorted(ans): print(i)

```
> 두번째 방법 : `BFS` 활용
```py
from collections import deque

# 상하좌우 이동을 위한 방향 벡터
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def BFS(x, y):
    queue = deque([[x, y]])  # 시작점을 큐에 추가합니다.
    cnt = 1  # 현재 영역의 크기를 저장할 변수를 초기화합니다.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dr[i][0]  # 다음 행 좌표를 계산합니다.
            ny = y + dr[i][1]  # 다음 열 좌표를 계산합니다.
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == '1':
                arr[nx][ny] = '0'  # 방문한 영역을 표시합니다.
                cnt += 1  # 영역의 크기를 증가시킵니다.
                queue.append([nx, ny])  # 다음 위치를 큐에 추가합니다.
    return cnt  # 현재 영역의 크기를 반환합니다.

N = int(input())  # 그리드의 크기 N을 입력받습니다.
arr = [list(input()) for _ in range(N)]  # 그리드 정보를 입력받습니다.

result = []  # 각 영역의 크기를 저장할 리스트를 초기화합니다.
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':  # 아직 방문하지 않은 1이라면,
            arr[i][j] = '0'  # 해당 위치를 방문했다고 표시합니다.
            result.append(BFS(i, j))  # BFS를 통해 현재 영역의 크기를 구하고 결과 리스트에 추가합니다.

print(len(result))  # 영역의 개수를 출력합니다.
for area in sorted(result):  # 영역의 크기를 오름차순으로 출력합니다.
    print(area)
``` 
---
#### 📀 백준 15681 트리와 쿼리 
> 트리의 노드별로 서브트리의 갯수를 저장하는 배열을 트리의 DP로 구현
> 1. 트리의 연결정보를 먼저 `tree`에 저장한다. 
> 2. 방문안한 노드를 계속해서 순회하면서, 자식노드가 없을 때까지 간다.
> 3. 종점 노드에 도착하면 부모노드의 서브트리에 자식노드의 서브트리값을 계속 더한다. 

```python
def DFS(now):
    visit[now] = 1
    for next in tree[now]:
        if not visit[next]:
            DFS(next)
            # 자식 서브 트리의 서브 트리 노드 개수 합산
            subtree[now] += subtree[next]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
visit = [0] * (N+1)
subtree = [1] * (N+1)

# 트리 생성
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

DFS(R)
[print(subtree[int(input())]) for _ in range(Q)]
```

#### 🧏‍♀️ 백준 16974 레벨 햄버거
> `DP`를 활용한 문제풀이 : 재귀함수
> 1. 총 갯수(2n+3) = 패티 갯수(n+1) + 번 갯수(n+2)
> 2. 현재 단계의 총 갯수 = 이전 단계의 총 갯수 * 2 + 3
> 3. 현재 단계의 패티 갯수 = 현재 단계의 총 갯수 // 2
```python
# 16974 레벨 햄버거
#  Lv |   Thickness   |     patty     |
# -------------------------------------
#  0  |  1            |  1            |
#  1  |  5 = 3 + 2*1  |  3 = 1 + 2*1  |
#  2  | 13 = 3 + 2*5  |  7 = 1 + 2*3  |
#  3  | 29 = 3 + 2*13 | 15 = 1 + 2*7  |
#  4  | 61 = 3 + 2*29 | 31 = 1 + 2*15 |
#  5  |125 = 3 + 2*61 | 63 = 1 + 2*31 |

def search(N, X):
    # L-0 까지 도달
    if N == 0:
        return 1

    # 1장 섭취
    if X == 1:
        return 0

    # 절반 미만 섭취
    elif X < burger[N-1] + 2:
        return search(N-1, X-1)

    # 절반 섭취
    elif X == burger[N-1] + 2:
        return patty[N-1] + 1

    # 전체 미만 섭취
    elif X < burger[N]:
        return patty[N-1] + 1 + search(N-1, X - burger[N-1] - 2)

    # 전체 섭취
    else:
        return patty[N]

N, X = map(int, input().split())
burger = [1] * 51; patty = [1] * 51

for i in range(1, N + 1):
    burger[i] = 3 + 2 * burger[i - 1]
    patty[i] = 1 + 2 * patty[i - 1]

print(search(N, X))
```
> `DP`를 활용한 문제풀이 : 반복문 활용
```py
N, X = map(int, input().split())  

def hamburger(N, X):
    result = 0 
    while N >= 0:
        # X의 위치가 전체 크기와 같은 경우
        if X == DP[N][0]:
            result += DP[N][1]
            return result
        # X의 위치가 딱 중간인 경우
        elif X == DP[N][0] // 2 + 1: 
            result += DP[N][1] // 2 + 1  
            return result
        # X의 위치가 중간보다 높은 경우
        # 중간만큼 먹고 들어가고, 중간이내 범위만큼 패티갯수를 저장한다.
        # 위치를 재조정한다.(중간위치를 차감한 만큼)
        elif X > DP[N][0] // 2 + 1:  
            X -= DP[N - 1][0] + 2 
            result += DP[N][1] // 2 + 1  
        # 만약 중간 위치보다 작은 경우에는, X를 1씩 차감한다. 
        # 왜냐하면 햄버거의 크기에서 번 1개 빼줘야 한다.
        else: 
            X -= 1  
        N -= 1  
    return result  

# DP 배열 초기화
DP = [[1, 1] for _ in range(N + 1)]  
# DP 저장정보 : 총 갯수, 패티 갯수 저장
for i in range(1, N + 1):
    DP[i][0] = 2 * DP[i - 1][0] + 3  
    DP[i][1] = 2 * DP[i - 1][1] + 1  

print(hamburger(N, X)) 
```

#### ❤️‍🔥 백준 17086 아기 상어 2
> `BFS`를 이용하여 위치별 최단거리를 반환한다. 
```python
from collections import deque

# 방향 벡터 정의
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# 너비 우선 탐색(BFS) 함수 정의
def BFS(x, y, visited):
    queue = deque([[x, y]])
    visited[x][y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 8방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 배열 범위 내에 있고, 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 거리를 계산하여 방문 표시
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

                # 1로 표시된 지뢰를 만났다면 최단 거리 반환
                if arr[nx][ny] == 1:
                    return visited[nx][ny] - 1

# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_val = 0

# 모든 위치에 대해 확인
for i in range(N):
    for j in range(M):
        # 지뢰가 없는 경우에만 최단 거리 계산
        if arr[i][j] == 0:
            temp = BFS(i, j, [[0] * M for _ in range(N)])
            max_val = max(max_val, temp)

# 결과 출력
print(max_val)

```
> `BFS`를 이용하여 위치별 최단거리를 반환한다. 
```python
from collections import deque

# 방향 벡터 정의
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# 너비 우선 탐색(BFS) 함수 정의
def BFS(x, y, visited):
    queue = deque([[x, y]])
    visited[x][y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 8방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 배열 범위 내에 있고, 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 거리를 계산하여 방문 표시
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

                # 1로 표시된 지뢰를 만났다면 최단 거리 반환
                if arr[nx][ny] == 1:
                    return visited[nx][ny] - 1

# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_val = 0

# 모든 위치에 대해 확인
for i in range(N):
    for j in range(M):
        # 지뢰가 없는 경우에만 최단 거리 계산
        if arr[i][j] == 0:
            temp = BFS(i, j, [[0] * M for _ in range(N)])
            max_val = max(max_val, temp)

# 결과 출력
print(max_val)
```
> `Dijkstra` 이용
```py
from collections import deque

def BFS(sea, i, j):
    dist = [[0] * M for _ in range(N)]
    Q = deque([[i, j]])
    while Q:
        i, j = Q.popleft()
        for di, dj in go:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not dist[ni][nj]:
                dist[ni][nj] = dist[i][j] + 1
                if sea[ni][nj]: return dist[ni][nj]
                Q.append([ni, nj])

go = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if not sea[i][j]:
            ans = max(ans, BFS(sea, i, j))
print(ans)
```

#### ❤️‍🔥 백준 21609 상어 중학교
> `시뮬레이션` + `구현` 문제
> 1. `DFS`를 이용하여 최대 블록 크기를 찾는다.
> 2. 탐색과정에서 무지개 블록갯수, 블록크기와 모든 블록의 인덱스를 반환한다.
> 3. `gravity` : 중력함수
> 4. `turn` :  90도 반시계방향 회전 함수
> 5. 블록을 찾는 로직을 반복한다. (무지개와 검은 블록 제외)
> 6. 1 크기 이상의 블록그룹이 없으면 강제 종료.
> 7. 그 외의 경우, 모든 블록들을 아래 순서에 따라 정렬한다.
>   - 블록크기, 무지개 블록 포함갯수, 행과 열순
>   - 점수의 제곱을 계속 더해준다. 
```py
def DFS(i, j, C):
    stack = [[i, j]]
    n_cnt, r_cnt = 1, 0
    n_cube, r_cube = [[i, j]], []

    while stack:
        i, j = stack.pop()
        for di, dj in go:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
                # 특정 색 블록
                if grid[ni][nj] == C:
                    visit[ni][nj] = 1
                    stack.append([ni, nj])
                    n_cube.append([ni, nj])
                    n_cnt += 1

                # 무지개 블록
                if grid[ni][nj] == 0:
                    visit[ni][nj] = 1
                    stack.append([ni, nj])
                    r_cube.append([ni, nj])
                    n_cnt += 1; r_cnt += 1

    for i, j in r_cube: visit[i][j] = 0

    return n_cnt, r_cnt, n_cube + r_cube

def gravity(arr):
    # 밑에서 부터 탐색
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if 0 <= arr[i][j] <= M:
                temp = arr[i][j]; arr[i][j] = -2; ni = i
                # 바닥이나 검은 블록에 닿을 때까지 낙하
                while ni < N - 1 and arr[ni + 1][j] == -2: ni += 1
                arr[ni][j] = temp

def turn(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][N - i - 1]
    return new_arr

go = ((1, 0), (0, 1), (0, -1), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    visit = [[0] * N for _ in range(N)]
    groups = []

    # 블록 그룹 탐색
    for i in range(N):
        for j in range(N):
            if 0 < grid[i][j] and visit[i][j] == 0:
                visit[i][j] = 1
                group = DFS(i, j, grid[i][j])
                if group[0] > 1: groups.append(group)

    # 블록 그룹이 존재하지 않으면 종료
    if not groups: exit(print(ans))
    # 조건에 맞는 블록 찾기 : 블록 개수 - 무지개 개수 - 행과 열
    B, R, cubes = sorted(groups, reverse=True)[0]

    # 블록 제거 - 점수 획득 - 중력 - 회전 - 중력
    for i, j in cubes: grid[i][j] = -2
    ans += B**2
    gravity(grid)
    grid = turn(grid)
    gravity(grid)
```
