## Algorithm Study 7회차 회의 (24.3.17.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 3월 16일 토요일 저녁 8시
        - 장소 : 디스코드 통한 비대면 회의

    나. 차주 예정 일정
        - 시간 : 3월 23일 토요일 아침 10시 반  
        - 방식 : 김해 커피팀버  

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
    - SWEA 2382 미생물 격리
   ###### 2. 경태
    - SWEA 원자 소멸 시뮬레이션
   ###### 3. 예리
    - SWEA 5650 핀볼게임 
   ###### 4. 동현
    - 백준 1647 도시 분할 계획
   ###### 5. 상현
    - 백준 2239 스도쿠

### 🎁 문제 선정
   ###### 1. 창호
    - 백준 11437 LCA(골드 3) - 상
    - 백준 14501 퇴사(실버 3) - 하
   ###### 2. 경태
    - 백준 14938 서강그라운드 (골드 4) - 상
    - 백준 9251 LCS(골드 5) - 하
   ###### 3. 예리
    - 백준 1202 보석도둑(골드 2) - 상
    - 백준 18111 마인크래프트(실버 2) - 하 
   ###### 4. 동현
    - 백준 1976 여행가자(골드 4) - 상
    - 백준 18352 특정 거리의 도시 찾기(실버 2) - 하
   ###### 5. 상현
    - 백준 17404 RGB거리2(골드 4) - 상
    - 백준 10844 쉬운 계단 수(실버 1) - 하


### 🏅 스터디 내용 
#### 🎈 백준 1202 보석도둑  
> 해결방법 : `힙`과 `그리디 알고리즘`을 이용해 푸는 문제
```python
from heapq import *
N, K = map(int, input().split())
jewel_list = []

for _ in range(N):
    w, v = map(int, input().split())
    jewel_list.append([w, v])
# 가방 무게 역순으로 정렬(끝에서 작은거 부터 뺌)
bag_list = [int(input()) for _ in range(K)]
bag_list.sort(reverse = True)
# 보석 무게 역순으로 정렬(끝에서 작은거 부터 뺌)
jewel_list.sort(reverse = True)
temp = []
result = 0

while bag_list:
    bag = bag_list.pop()

    while jewel_list:
        weight, value = jewel_list.pop()
        # 가방안에 들어갈 정로 보석 무게가 작으면 
        if bag >= weight:
            heappush(temp, -value)
        # 크면 다시 보석을 되돌려 놓음 
        else:
            jewel_list.append((weight, value))
            break
    # 하나라도 temp에 담겨있다면 그중 가장 가치나가는거부터 뺌
    if temp:
        result -= heappop(temp)

print(result)
```

#### 🧰 백준 1976 여행 가기 
> `BFS`를 이용하여 모두 방문 가능할 경우 `YES` 출력
```python
from collections import deque

# 그래프 제작(1인 경우에 연결정보 저장)
N = int(input()); input()
graph = [[] for _ in range(N)] 
for i in range(N):
    for j, v in enumerate(input().split()):
        if v == '1': graph[i].append(j)
# 여행 계획 저장 
seq = list(map(int, input().split()))
visit = [0] * N
# 시작점을 설정
Q = deque([seq[0] - 1])
# 하나씩 빼줌
while Q:
    now = Q.popleft()
    # 그래프를 순회하여 방문안한 곳만 추가 
    for next in graph[now]:
        if not visit[next]: Q.append(next)
    visit[now] = 1

# 모두 방문했다면 YES
if all(visit[city - 1] for city in seq): print('YES')
else: print('NO')
```

#### ⚽ 백준 9251 LCS
> `DP` 1차원 배열을 이용
1. 현재 cnt를 0으로 셋팅 
2. 만약 cnt가 DP의 해당하는 열보다 작다면 cnt와 DP열을 동기화
3. 두 문자열이 같다면 cnt+1을 DP에 추가  
```python
str1, str2 = input(), input()
A, B = len(str1), len(str2)
DP, ans = [0] * B, 0

# 비교하는 문자열이 있는 배열 순회
for i in range(A):
    # 공통 부분의 카운트
    cnt = 0
    # 비교대상 배열의 문자열 순회
    for j in range(B):
        if cnt < DP[j]: cnt = DP[j]
        # 두 문자열이 같다면 카운트 + 1을 DP에 추가
        elif str1[i] == str2[j]: DP[j] = cnt + 1

print(max(DP))
```
> `DP` 2차원 배열을 이용
1. 행과 열이 각각 문자열의 자릿수를 의미
2. 순회하면서 문자열이 같으면, 우하향 대각측의 값을 1 증가
3. 그 외 다른 경우에는 최소한 전꺼랑은 같으므로, DP값 동기화
```python
str1, str2 = input(), input()
len_str1, len_str2 = len(str1), len(str2)

dp = [[0] * (len_str1 + 1) for _ in range(len_str2 + 1)]

for i in range(1, len_str2 + 1):
    for j in range(1, len_str1 + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max([max(row) for row in dp]))

```
#### 🖌 백준 10844 쉬운 계단 수
> `DP`를 이용한 풀이(1차원 배열)

```python
N = int(input())
DP = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DP2 = DP[:]

# 일의 자리를 인덱스로하여 진행
for _ in range(N-1):
    # 0인 경우와 9인 경우에는 전차의 1과 8과 같으므로
    DP2[0] = DP[1]; DP2[9] = DP[8]
    # 기본적으로 위아래로 연속된 수를 저장
    for i in range(1, 9):
        DP2[i] = DP[i-1] + DP[i+1]
    DP = DP2[:]

print(sum(DP)%(1000000000))
``` 

> `DP`를 이용한 풀이(2차원 배열)
```python
N= int(input())
# 맨 처음 1부터 9까지는 1자리는 연속된다고 가정하고 시작
DP =  [[0] +[1]* 9] + [[0] * 10 for _ in range(N-1)]
# 열 우선순회하여 연속된 정도를 저장
for i in range(1,N):
    for j in range(10):
        # 뒷 자리수가 0이면 연속되는 경우는 1밖에 없으므로 이전의 1에 저장된 값 저장
        if j ==0:
            DP[i][0] = DP[i-1][1]
        # 9면 8밖에 없으므로
        elif j==9:
            DP[i][9] = DP[i-1][8]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
# 맨 마지막 행에 모든 경우의수 저장됨
print(sum(DP[N-1])%int(1e9))
```


#### 🎙 백준 11437 LCA
> `트리`구조를 활용하여 최소 공통 조상 구하는 문제
1. 자식 인덱스에 부모 노드값을 저장하는 1차원 리스트 작성
2. 각 자식 인덱스의 노드 높이를 저장하는 배열 `depth` 지정
```python

from collections import deque
N = int(input())
# 간선이 N-1개 주어지므로 무조건 부모노드는 하나만 나와서, 정수값으로 저장
# trees는 각 인덱스가 자식노드고, 값이 부모노드임
trees = [-1 for _ in range(N+1)]
# 각 노드의 깊이 저장
depth = [0] * (N+1)

# 노드의 연결정보를 저장
adjacency_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

# 1이 루트 노드임 
queue = deque([1])
visited = [False] * (N+1)

while queue:
    parent = queue.popleft()
    visited[parent] = True

    for child in adjacency_list[parent]:
        if not visited[child]:
            trees[child] = parent
            depth[child] = depth[parent] + 1
            queue.append(child)

M = int(input())
for i in range(M):
    A, B = map(int, input().split())

    # 조상 노드를 같은 높이까지 올려줌
    while depth[A] > depth[B]:
        A = trees[A]
    while depth[B] > depth[A]:
        B = trees[B]

    # 높이를 같게 만들고 공통 조상을 찾음
    while A != B:
        A = trees[A]
        B = trees[B]

    print(A)
```
> 절대값이 큰 순으로 정렬하여 두칸씩 합을 비교
```python
N = int(input())
feat = sorted(map(int, input().split()), key=lambda x: abs(x))  # 용액의 절댓값 기준으로 정렬
min_v, temp = 1e+10, 0

for i in range(N-1):
    pls = abs(feat[i] + feat[i+1])  # 이웃한 두 수 비교
    if min_v > pls:
        min_v = pls; temp = i

print(min(feat[temp], feat[temp+1]), max(feat[temp], feat[temp+1]))
```

#### 👔 백준 14501 퇴사
> `BFS`를 통해 벌어들이는 돈의 `max`값을 출력
1. 현재 일에서 소요일수를 더했을 때, N을 초과하면 현재와 기존 맥스값을 비교하여 저장
2. N이면 기존 money와 상담을 통해 벌어들이는 돈을 더한 값과 기존 맥스값을 비교하여 저장
3. 그 외의 경우, 모든 경우에 대해 저장
```python
from collections import deque

def bfs():
    global max_

    q = deque()
    q.append((0, 0))

    while q:
        day, money = q.popleft()

        if day < N:
            if day + list_[day][0] >= N:
                if day + list_[day][0] == N:
                    max_ = max(max_, money + list_[day][1])
                    q.append((day + 1, money))
                else:
                    max_ = max(max_, money)
                    q.append((day + 1, money))
            else:
                q.append((day + list_[day][0], money + list_[day][1]))
                q.append((day + 1, money))

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
max_ = 0
bfs()
print(max_)
```

> `DP`와 `while`문을 통해 벌어들인 돈의 최대값을 지속적으로 저장
1. 어제와 오늘의 맥스값을 지속적으로 갱신
2. 오늘 상담을 했을 때 며칠 후의 수입과 기존에 쌓여있던 며칠후의 수입과 비교하여 큰 값을 저장
```python
N = int(input())
DP, d = [0] * (N+6), 1

while d < N+1:
    t, p = map(int, input().split())
    # 현재에서 최선을 구한 후, 상담이 완료된 후 최선을 구함
    DP[d] = max(DP[d-1], DP[d])
    # 현재 상담을 한 후 며칠 후의 수입과 기존에 쌓여있던 며칠 후의 수입 비교
    DP[d+t] = max(DP[d+t], DP[d]+p)
    d += 1

print(max(DP[:N+2]))
```

> 역순으로 순회하여 `DP`에 누적해서 저장 
1. 가장 첫열에 가장 높은값이 저장되는 구조 
2. 만약 상담 소요일과 현재 일수를 합친날이 N을 넘으면 전항의 값을 그대로 저장
3. 그 외의 경우에는 상담을 한것과 기존에 저장되있는 값과 비교하여 더 큰 값을 저장
```python
N = int(input())
consultation= [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1,-1,-1):
    cost, profit = consultation[i]
    if i + cost > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + cost] + profit)
print(dp[0])
```
---
#### 📀 백준 14938 서강그라운드
> `Dijkstra`를 활용
> 1. 
```python
from heapq import heappush, heappop

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

# 양방향 그래프 제작(비용을 뒤에 저장)
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

ans, Q = 0, []
INF = float('inf')

# 시작 지점을 바꾸어가며 탐색
for i in range(1, n+1):
    heappush(Q, [i, 0]); dist = [INF] * (n+1); dist[i] = 0

    # 다익스트라
    while Q:
        now, w = heappop(Q)
        if dist[now] < w: continue
        for next, next_w in graph[now]:
            cost = w + next_w
            if dist[next] > cost:
                dist[next] = cost; heappush(Q, [next, cost])

    # 갈 수 있는 곳의 점수 합산
    ans = max(ans, sum(item[i-1] for i in range(n+1) if dist[i] <= m))

print(ans)
```
#### 🧏‍♀️ 백준 17404 RGB거리2
> `DP`을 이용하여 
1. 시작점을 고정시키고 `RGB거리` 의 로직대로 `DP` 구성
2. 시작점과 일치하지 않는 도착점의 경우에 최솟값을 지속적 비교하여 저장 
3. 시작점 모두 순회
```python
N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
min_ = float('inf')

for start in range(3):
    temp = [row[:] for row in list_]

    for i in range(3):
        if i != start:
            temp[0][i] = float('inf')

    dp[0] = temp[0][:]
    temp[N - 1][start] = float('inf')

    for i in range(1, N):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][k] for k in range(3) if j != k) + temp[i][j]

    min_ = min(min_, min(dp[N - 1]))

print(min_)
```
#### ❤️‍🔥 백준 18111 마인크래프트
> 전형적인 `브루트포스` 알고리즘 문제
1. 평균치에서 땅의 최대 높이까지만 반복문 순회
2. 제거하는 경우에는 2초가 걸리고, 추가하는 경우에는 1초 소요됨
3. 만약 순회하다가 block이 음수가 된다면, 평균치에서 1씩 증가하여 동일한 로직 반복
```python
import sys
sys.stdin = open('input.txt')
N,M,B = map(int,input().split())
# 제거 : 2초, 추가 : 1초 (추가 먼저한다)
arr =[]
# 어차피.. 1차원으로 구현해도 노상관
for _ in range(N):
    arr.extend(list(map(int,input().split())))
# 목표치를 평균으로 둔다 
obj = round(sum(arr)/(N*M))
maxi = max(arr)
min_time= int(1e9)

# 목표부터 최대값까지 순회(같으면 높은 값을 출력해야하기 때문)
for target in range(obj-1,maxi+1):
    time = 0
    block = B
    # 현재 위치의 높이
    for earth in arr:
        # 목표치가 현재 땅보다 낮은경우 : 블록 제거(2초 소요)
        if target < earth:
            time += 2*(earth- target)
            block += earth - target
        # 목표치가 현재 땅보다 높은 경우 : 블록 추가(1초 소요)
        else:
            time += target-earth
            block -= target - earth
    # 한번씩 순회했는데 마이너스면.. 다음 목표치로 변경
    if block < 0:
        continue
    # 최소 시간을 저장하고, 그 때의 평탄화된 땅 높이를 저장 
    if min_time >= time:
        min_time = time
        result = target
print(min_time,result)
```

#### ❤️‍🔥 백준 18352 특정 거리의 도시 찾기
> `BFS`를 이용하여 방문할 때마다 시작점에서의 거리를 저장
```python
from collections import deque
import heapq
# 다익스트라 써볼랬는데, 인접한 거리가 항상 1이라 안써도 풀 수 있을거 같아서 BFS로 함
def BFS(start):
    queue = deque([start])
    visited[start]=1
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now]+1
                queue.append(next)
    temp= []
    for i,j in enumerate(visited):
        # 최단거리가 K인 경우에는 temp에 저장
        if j-1==K:
            temp.append(i)
    # temp에 있으면 sort해서 출력
    if temp:
        for i in sorted(temp):
            print(i)
    # 없으면 -1
    else:
        print(-1)
    return

N, M, K, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
visited = [0] * (N+1)
# 인접한 거리는 항상 1이기
for i in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
# X부터 출발
BFS(X)
```
> `dijkstra`를 이용하여 시작점에서의 최소거리를 저장 
```python
from heapq import heappush, heappop

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]; INF = float('inf')
dist = [INF] * (N+1); dist[X] = 0

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

Q, ans = [], []
heappush(Q, [0, X])

while Q:
    w, now = heappop(Q)
    if dist[now] < w: continue
    if w == K: ans.append(now); continue
    for next in graph[now]:
        cost = w + 1
        if dist[next] > cost:
            dist[next] = cost
            heappush(Q, [cost, next])

if ans:
    for i in ans: print(i)
else: print(-1)
```
