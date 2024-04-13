## Algorithm Study 11회차 회의 (24.4.13.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 4월 13일 토요일 아침 9시 30분  
        - 방식 : 김해 커피팀버 

    나. 차주 예정 일정
        - 시간 : 4월 21일 일요일 아침 9시  
        - 방식 : 비대면 디스코드 

    다. 안건 심의(투표) 결과
        1. 스터디원 모집 2명(최지우, 이권민) : 가결(전원 합의)
        2. 코드리뷰 방식 변경 : 가결(전원 합의)
        3. 8조 패널티 관련 규정 개선 : 부결(과반수 반대)
    
    라. 변경사항 요약 (4월 21일 이후)
        1. 각자 선정한 1문제 리뷰(모두 앞에서 바로 풀 수 있을 만큼) 
            - 요청있거나, 말하고 싶은 사람은 자기 문제 아니라도 추가 리뷰 가능
        2. 각자 1문제씩만 선정(총 7문제)
        3. 일정 기본값: 매주 토요일 9시 반 → 매주 일요일 저녁 7시
            - 일정 변경 시, 사전협의하여 변경. 변경불가 시 불참비 지출 要.

    마. 4월 일정
        1. 4월 21일 일요일 오전 9시 비대면 디스코드
        2. 4월 28일 일요일 저녁 7시 김해 커피팀버
            - 단, 장소는 협의하여 변경될 수 있음

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 10문제
    다. 난이도 : 최대 백준 골드 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 이번 주의 새로운 문제 : 위상정렬
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

### 🎁 이번회차 풀이 문제
   ###### 1. 창호
    - 백준 14567 선수과목(골드 5)
    - 백준 15565 귀여운 라이언(실버 1)
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
#### 🎈 백준 1327 소트게임
> `BFS` 이용한 문제 풀이 
> 1. N : 순열의 크기 / K : 순열에 들어가는 수 주어짐
> 2. 정렬된 순열(목표순열)을 정의하고, `BFS`를 이용
> 3. 목표와 같은 경우에만 본 반복문 탈출
> 4. 방문한 적 있는 배열은 visited에 저장하여 향후 방문 제외
> 5. 더 이상 탐색할 것이 없이 반복문 탈출 시, -1 출력

```python
from collections import deque

N, K = map(int, input().split())
nums = tuple(map(int, input().split()))

# 정렬된 순열 및 방문 순열 저장
sorted_nums = tuple(sorted(nums))
visit = {nums}

# BFS
Q = deque([[nums[:], 0]])
while Q:
    now, dist = Q.popleft()
    # 정렬된 순열과 같다면 종료
    if now == sorted_nums: exit(print(dist))
    # 각 자리마다 뒤집은 배열 생성
    for i in range(N-K+1):
        next = now[:i] + now[i:i+K][::-1] + now[i+K:]
        if next in visit: continue
        Q.append([next, dist+1])
        visit.add(next)

# Q가 빌 때까지 종료가 안 되었다면 정렬이 불가능한 것
print(-1)
```

#### 🧰 백준 1450 냅색문제 
> `중간에서 만나기` 새로운 로직 이용 (유사문제 : 부분수열의 합)
> 1. N개의 물건 중에서 무게의 합이 C이하인 만큼 선택가능
> 2. subSetsum : 부분집합의 합을 계산하는 함수
> 3. 물건을 두 부분집합으로 나누어, 한쪽 부분집합(A)과 나머지 부분집합(B)의 요소를 비교하여 조건 충족하는 경우 갯수 카운트
> 4. 나머지 한 집합(B)은 정렬하고, 이진탐색을 통해 A와 B의 합이 C보다 잡은 경우에만 B의 인덱스만큼 결과값에 가산
> 5. 왜냐하면 이진탐색이기 때문에, C에 가장 가까운 B의 인덱스값은 그 아래에 있는 애들은 모두 합해봤자 C보다 작기 때문에 B의 인덱스값을 더해주면 됨

```python
N, C = map(int, input().split())
items = list(map(int, input().split()))

# 부분집합의 합 계산 함수
def subSetSum(arr):
    part = [0]
    for n in arr: part += [n+x for x in part]
    return part

# 두 부분으로 나누어 부분집합의 합 계산
part1 = subSetSum(items[:N//2])
part2 = subSetSum(items[N//2:])
part2.sort()  # 이진 탐색을 위해 정렬

# 한 부분의 부분집합의 합을 다른 부분과 대조하여 조건에 맞으면 카운트하는 함수
def countPairs(part1, part2, limit, cnt=0):
    for mass in part1:
        if mass > limit: continue
        L, R = 0, len(part2)

        # 기준점에 맞는 부분을 찾기 위한 이분탐색 부분
        while L < R:
            M = (L+R)//2
            if part2[M] + mass <= limit:
                L = M+1
            else:
                R = M
        # 조건을 맞추는 무게까지 개수 합산
        cnt += L
    return cnt
print(countPairs(part1, part2, C))
```

#### ⚽ 백준 7576 토마토
> `BFS`를 이용 
> 1. 익은 토마토를 모두 구해서 q에 바로 담아준다.
> 2. BFS를 돌려서, q에서 나와 다음 탐색으로 이동할 때, 현재보다 cnt를 1증가 시켜 q에 append한다.
> 3. 반복문을 탈출하고, 0이 발견되면 -1을 출력한다. 아니라면 cnt를 출력한다.

```python
from collections import deque

dr = ((1,0),(0,1),(-1,0),(0,-1))
N,M = map(int,input().split()) # N 가로 M 세로

tomatoes = [list(map(int,input().split())) for _ in range(M)]
# 토마토 위치 구하기
q = deque([])
for i in range(M):
    for j in range(N):
        if tomatoes[i][j] == 1 :
            q.append((i,j,0))
# BFS
while q :
    i,j,cnt = q.popleft()
    for dx,dy in dr :
        di, dj = i+dx, j+dy
        if 0 <= di < M and 0 <= dj < N :
            if tomatoes[di][dj] == 0 :
                tomatoes[di][dj] = 1
                q.append((di,dj,cnt+1))
# 0 발견 시 -1 출력 후 종료
for i in range(M):
    for j in range(N):
        if tomatoes[i][j]==0:
            exit(print(-1))

# 그 외에는 마지막에 pop된 cnt가 정답
print(cnt)
```

#### 🖌 백준 9465 스티커 
> `DP`를 이용한 스티커
> 1. 스티커끼리 인접할 수 없으므로, 왼쪽 하단 스티커에 누적된 합과, 왼쪽 하단의 스티커의 왼쪽에 누적된 합을 비교하여 DP에 담는다.
> 2. 마지막에 누적된 스티커의 max값을 출력
```python
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    size = int(input())
    sticker = [[0,0] + list(map(int,input().split())) for _ in range(2)]

    # 대각선 한칸 반대 or 대각 두칸 전 반대

    for j in range(2,size+2):
        for i in range(2) :
            sticker[i][j] += max(sticker[i-1][j-1], sticker[i-1][j-2])
    print(max([max(x) for x in sticker]))
``` 

#### 🎙 백준 13335 트럭
> 간단한 `구현` 문제
> 1. 다리 하중 내에서 트럭을 추가할 때, 견딜 수 있으면 트럭을 다리 위에 넘긴다.
> 2. 트럭들이 전부 없어지거나, 트럭이 다 건널 때까지 반복문 순회
> 3. 반복문을 순회하여 `temp_sum`에 무게의 합을 저장(여기에 다리에 있는 트럭의 무게합 저장)
> 4. 반복문 탈출하면 시간을 출력

```python
from collections import deque

# n: 트럭의 수, w: 다리의 길이, L: 다리의 최대 하중
n, w, L = map(int, input().split())

# 트럭의 무게를 입력 받음
trucks = deque(map(int, input().split()))

# 다리 위에 올라간 트럭들의 무게의 합을 저장할 변수 초기화
temp_sum = 0

# 다리 위의 트럭을 나타내는 deque 초기화
result = deque([0] * w)

# 경과 시간을 나타내는 변수 초기화
time = 0

# 모든 트럭이 다리를 건널 때까지 반복
while trucks or sum(result) != 0:
    temp_sum -= result.popleft()  # 다리를 건너는 트럭 중 가장 먼저 들어간 트럭의 무게를 빼줌
    if trucks and temp_sum + trucks[0] <= L:  # 다음 트럭이 다리에 올라갈 수 있는지 확인
        temp_sum += trucks[0]  # 다음 트럭을 다리에 올리고 다리 위 트럭들의 무게의 합을 업데이트
        result.append(trucks.popleft())  # 다음 트럭을 다리 위에 올림
    else:
        result.append(0)  # 다음 트럭이 올라가지 못하면 다리 위에는 아무것도 올리지 않음
    time += 1  # 경과 시간을 증가
print(time)  # 걸린 시간 출력
```

#### 👔 백준 14567 선수과목
> `그래프`의 연결정보를 저장하고, 깊이를 구한다. 
> 각 `그래프`의 깊이를 순회할 때마다 max값을 저장한다.(모든 선수과목을 수강해야 한다.)
```python
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
depth = [1] * (N+1)

# 그래프 생성
for _ in range(M):
    pre, post = map(int, input().split())
    graph[pre].append(post)

# 진입 차수 계산
for now in range(1, N+1):
    for next in graph[now]:
        depth[next] = max(depth[next], depth[now] + 1)

print(*depth[1:])

```
> 두번째 방법 : `위상정렬` 활용
> 1. `indegree` : 진입차수를 저장
> 2. `result` : 각 인덱스에 최대 깊이를 저장
> 3. `heap` 구조를 활용하여, 깊이가 최소인 경우를 우선 탐색
> 4. 최종적으로, 결과값 반환(모든 진입차수 저장)
```py
from heapq import*

def topological_sort():
    q = []
    result = [0] * (N + 1)

    for vertex in range(1, N + 1):
        if indegree[vertex] == 0:
            heappush(q, (1, vertex))

    while q:
        semester, vertex = heappop(q)
        result[vertex] = semester

        for v in graph[vertex]:
            indegree[v] -= 1
            
            if indegree[v] == 0:
                heappush(q, (semester + 1, v))

    return result

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

result = topological_sort()

for i in result:
    if i:
        print(i, end = ' ')
``` 
---
#### 📀 백준 15565 귀여운 라이언 
> `슬라이딩 윈도우` 활용
> 1. 라이언 갯수가 충족될 때까지 오른쪽으로 이동
> 2. 갯수 충족시, 오른쪽 포인터 - 왼쪽 포인터 + 1 값과 기존 최소값을 비교하여, 최소 길이를 저장해주고, 왼쪽 포인터를 오른쪽으로 이동한다.
> 3. 그리고 다시 갯수가 충족될 때까지 위 과정을 반복한다.
> 4. 길이 N만큼 모두 순회할 때 최소 길이를 반환한다.

```python
N, K = map(int, input().split())
doll = list(map(int, input().split()))

cnt = L = R = 0
ans = N + 1

# 첫 번째 인형이 라이언이면 카운트 + 1
if doll[L] == 1: cnt += 1

# 오른쪽 포인터가 끝까지 갈 때까지 반복
while R < N:
    # 조건 충족 시
    if cnt == K:
        ans = min(ans, R-L+1)  # 기록
        cnt -= (doll[L] == 1)
        L += 1
    # 조건 미충족 시
    else:
        R += 1
        cnt += (R < N and doll[R] == 1)

print(ans if ans < N+1 else -1)
```

#### 🧏‍♀️ 백준 16562 친구비
> `Kruskal` 알고리즘 활용
> 1. 친한친구끼리 `union`과 `find`로 묶어준다.
> 2. 같은 무리별 가격을 `sep_dict`에 저장한다.
> 3. 무리별로 반복하여 최소값을 결과값에 저장한다.
```python
# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:  # 현재 노드의 부모 노드가 자기 자신이 아니면
        parent[x] = find_parent(parent, parent[x])  # 부모 노드를 재귀적으로 찾아서 경로 압축
    return parent[x]  # 부모 노드 반환

# 두 집합을 합치는 함수
def union(parent, a, b):
    a = find_parent(parent, a)  # 노드 a의 부모 노드를 찾음
    b = find_parent(parent, b)  # 노드 b의 부모 노드를 찾음
    if a < b:  # 두 노드의 부모가 다르면
        parent[b] = a  # b의 부모를 a로 설정
    else:
        parent[a] = b  # a의 부모를 b로 설정

# 입력값 받음: N은 친구의 수, M은 친구 관계의 수, k는 친구들이 모이는데 드는 돈
N, M, k = map(int, input().split())

# 친구들의 가격 정보를 받음
friends_cost = list(map(int, input().split()))

# 각 노드의 부모 노드를 저장하는 배열 초기화(처음은 자기가 자기 무리의 대표노드)
parent = [i for i in range(N + 1)]

# 친구 관계를 입력받고 두 친구를 같은 무리로 합침
# 향후 가장 낮은 비용이 드는 친구에게만 비용지불 예정
for _ in range(M):
    v, w = map(int, input().split())
    union(parent, v, w)

# 부모 노드별로 친구들의 가격을 저장하는 사전 초기화
sep_dict = {i: set() for i in range(1, max(parent) + 1)}

# 친한 친구끼리 묶어 sep_dict에 저장
for i in range(1, N + 1):
    sep_dict[find_parent(parent, i)].add(friends_cost[i - 1])

# 각 친구무리별 최소 비용을 구하고 결과에 더함
result = sum(map(lambda x:min(x) if x else 0, sep_dict.values()))

# 소요비용이 내가 가진 돈 k를 초과하는지 확인하고 출력
print(result if result <= k else 'Oh no')
```
> `Prim`을 활용한 문제풀이
> 1. `graph`에 친구비용을 저장한다.
> 2. 단, 연결된 곳은 0으로 저장한다.
> 3. 0을 시작점으로 하여 `그리디`하게 낮은 비용을 전부 합해준다.
> 4. 결과값을 반환한다.
```py
from heapq import *

def prim(start):
    connected = {start}
    unconnected = [(w, v) for w, v in graph[start]]
    heapify(unconnected)
    cost = 0
    while unconnected:
        weight, vertex = heappop(unconnected)
        if vertex in connected:
            continue
        connected.add(vertex)
        cost += weight
        for w, v in graph[vertex]:
            if v in connected:
                continue
            heappush(unconnected, (w, v))
    return cost

N, M, k = map(int, input().split())
list_ = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[0].append((list_[i], i))
    graph[i].append((list_[i], 0))

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append((0, w))
    graph[w].append((0, v))

result = prim(0)
if result > k:print('Oh no')
else:print(result)
```

#### ❤️‍🔥 백준 20529 가장 가까운 세 사람의 심리적 거리
> `비둘기집 원리`와 `combinations`를 이용
> 1. 세 사람의 심리적거리를 쟤기 때문에 세 사람이 동일한 MBTI면 무조건 값이 0임 --> N이 33이면 무조건 겹치는 세사람이 존재
> 2. `combinations`에서 세 사람을 조회하여 MBTI 동일성 판단하여 일치여부 최소값 반환(`브루트포스`)
```python
from itertools import combinations

for _ in range(int(input())):
    N, ans = int(input()), 8
    MBTI = input().split()

    # N이 32보다 크면 적어도 3개인 mbti가 있으므로 최소 거리는 0
    if N > 32: print(0); continue

    # 주어진 MBTI중에서 원소 개수가 3개인 조합 골라냄
    for a in set(combinations(MBTI, 3)):
        cnt = 0

        # 각 자리마다 set 글자 개수로 동일 문자 판별
        for b in map(set, zip(*a)):
            if len(b) == 2: cnt += 2

        # 답과 비교 후 최솟값 선정
        ans = min(ans, cnt)

    print(ans)

```

#### ❤️‍🔥 SWEA 2477 차량정비소
> `시뮬레이션` + `구현` 문제
> 1. `Guest`라는 클래스를 정의하여, 보다 가독성좋게 문제풀이
> 2. 정비창구 → 정비대기 → 접수창구 → 접수대기 순으로 반복문 순회
> 3. 모든 `Guest`의 인스턴스를 순회하여 잃어버린 지갑 고객과 같은 경우 결과값 추가
```py
from collections import deque

class Guest:
    def __init__(self, pk):
        self.pk = pk
        self.numA = 0
        self.numB = 0
        self.time = 0
        self.end = False

def find(arr, V):
    try: return arr.index(V)
    except ValueError: return -1

for tc in range(int(input())):
    N, M, K, A, B = map(int, input().split())  # 접수 창구 수, 정비 창구 수, 방문 고객 수, 타겟 접수 창구, 타겟 정비 창구
    timeA = list(map(int, input().split()))  # 접수 소요 시간 : N개
    timeB = list(map(int, input().split()))  # 정비 소요 시간 : M개
    timeT = list(map(int, input().split()))  # 고객 방문 시간 : K개

    deskA = [False] * N; waitA = deque([])  # 접수 창구 및 대기
    deskB = [False] * M; waitB = deque([])  # 정비 창구 및 대기

    timeT = deque(timeT)
    ans, num = 0, 1
    guests = []

    for t in range(5000):
        # 정비 창구
        for j, desk in enumerate(deskB):
            if not(desk and not desk.time): continue

            # 정비 대기 인원 정비 창구 이동
            if waitB:
                deskB[j] = waitB.popleft()
                deskB[j].time = timeB[j]
                deskB[j].numB = j
            else:
                deskB[j] = False
            # 종료 조건 추가
            desk.end = True

        # 접수 창구
        for i, desk in enumerate(deskA):
            if not desk or desk.time > 0: continue

            # 접수 완료자 정비 창구 또는 정비 대기 이동
            j = find(deskB, False)
            if j > -1:
                deskB[j] = desk
                deskB[j].time = timeB[j]
                deskB[j].numB = j
            else:
                waitB.append(desk)

            # 접수 대기 인원 접수 창구 이동
            if waitA:
                deskA[i] = waitA.popleft()
                deskA[i].time = timeA[i]
                deskA[i].numA = i
            else:
                deskA[i] = False

        # 정비소 방문
        while timeT and timeT[0] == t:
            guests.append(Guest(num))
            # 방문자 접수 창구 또는 접수 대기 이동
            i = find(deskA, False)
            if i > -1:
                deskA[i] = guests[-1]
                deskA[i].time = timeA[i]
                deskA[i].numA = i
            else:
                waitA.append(guests[-1])

            num += 1
            timeT.popleft()

        # 시간 경과
        flag = 0
        for guest in guests:
            guest.time -= 1
            if guest.end: flag += 1

        if flag == K: break

    # 지갑 분실자 체크
    for guest in guests:
        if guest.numA == A-1 and guest.numB == B-1:
            ans += guest.pk

    print(f'#{tc+1} {ans if ans else -1}')
```
