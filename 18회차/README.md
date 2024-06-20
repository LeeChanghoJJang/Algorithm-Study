## Algorithm Study 18회차 회의 (24.6.15.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 6월 15일 토요일 오후 7시  
        - 방식 : 송삼 2층

    나. 차주 예정 일정
        - 시간 : 6월 22일 토요일 오후 7시  
        - 방식 : 디스코드

    다. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 박동현 - 이권민 - 이창호 - 윤예리 - 최지우- 이상현 - 임경태  (순서는 매번 랜덤으로 변경 예정) 
            - ③ 한번에 2개를 다 브리핑하지 않고, 추가 문제는 다시 한번 로테이션을 돌 예정.
    
    라. 유지사항
        - 장소 선정 : 스터디원이 증대되어 장소를 송삼, 김해 중 하나로 결정(1번씩 로테이션)
        - 비대면, 대면 1회씩. 1주일마다 한번

### 🎵 문제 선정 및 방식 
    가. 유형 : 코딩테스트 기출 위주로 각자 리뷰할 문제 선정 
    나. 문제수 : 인당 1문제, 총 7문제
    다. 난이도 
        - 백준 플래티넘 이하
        - 프로그래머스 Lv.4 이하
        - SWEA D6 이하    
    라. 코드 브리핑 && 리뷰 방식
      - 위 변경사항 참고

### 🎁 이번회차 풀이 문제
   ###### 1. 창호
    - 백준 2344 거울(골드 4) 
   ###### 2. 예리
    - 백준 11779 최소비용 구하기(골드 3) 
   ###### 3. 경태
    - 백준 2437 저울(골드 2)
   ###### 4. 동현
    - 백준 12689 뮤탈리스크(골드 4)
   ###### 5. 상현
    - 프로그래머스 92335 k진수에서 소수 개수 구하기(Lv.2)
   ###### 6. 지우
    - 백준 1339 단어 수학 (골드 4)
   ###### 7. 권민
    - 백준 24533 팰린드롬 게임(골드 4)

### 🤢 문제 선정
   ###### 1. 창호
    - 백준 2629 양팔저울(골3)
   ###### 2. 예리
    - 프로그래머스 160585 혼자서 하는 틱택토(Lv.2)
   ###### 3. 경태
    - 프로그래머스 67258 보석 쇼핑(Lv.3)
   ###### 4. 동현
    - 백준 3109 빵집 (골2)
   ###### 5. 상현
    - 프로그래머스 92342 양궁대회 (Lv.2)
   ###### 6. 지우
    - 백준 3687 성냥개비 (골2)
   ###### 7. 권민
    - 백준 24533 팰린드롬 게임(골드 4)

### 🏅 스터디 내용 
#### 🎈 백준 1339 단어 수학
> 1. `char` 딕셔너리에 각 단어에 따른 실제 값 저장(아스키 코드 이용)
> 2. char.value가 높은 순으로 9부터 내림차순으로 값을 부여하기
```python
n = int(input())

char = {i: 0 for i in range(27)}

for _ in range(n):
    t = input()[::-1]
    for i in range(len(t)):
        char[ord(t[i])-65] += 10**i

result = 0
k = 9
for num in sorted(char.values(), key=lambda x: -x):
    if not num:
        break

    result += k * num
    k -= 1

print(result)
```
#### 🧰 백준 2344 거울
> 1. start 함수를 정의한다. 빔의 숫자와 방향에 따라 이동하는 함수이다.
> 2. 그러면 그 결과를 바탕으로 도착하는 부분의 위치를 반환한다.

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]


def start(v, d):
    if d == 0:p = [(v, 0)]
    elif d == 1:p = [(N-1, v)]
    elif d == 2:p = [(v, M-1)]
    else:p = [(0, v)]

    while p:
        x, y = p.pop()

        if box[x][y]:
            d = change_dr[d]
        dx, dy = dr[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            p.append((nx, ny))
        else:
            if nx == -1:return 2*N + 2*M - ny
            elif ny == -1:return nx+1
            elif nx == N:return N + ny + 1
            else:return 2*N + M - nx


dr = [(0, 1), (-1, 0), (0, -1), (1, 0)]
change_dr = [1, 0, 3, 2]
result = []
for i in range(N):
    result.append(start(i, 0))

for i in range(M):
    result.append(start(i, 1))

for i in range(N):
    result.append(start(N-i-1, 2))

for i in range(M):
    result.append(start(M-i-1, 3))

print(*result)
```

#### ⚽ 백준 2437 과제
> 어떤 숫자보다 작은 모든 숫자들의 합이 그 숫자가 되지 않으면 연속적이지 않는 성질을 이용한다.

```python
# 2437 저울
_ = int(input())
weights = sorted(map(int, input().split()))

# 현재까지 측정 가능한 최대 무게
sum_v = 0

for w in weights:
    # 사이 간격이 1이 아니라면 종료
    if w > sum_v + 1:
        break
    sum_v += w

# 측정할 수 없는 가장 작은 무게 출력
print(sum_v + 1)
```

#### 🖌 백준 11779 최소비용 구하기 2
> 1. 다익스트라를 통해 start 지점부터 end 지점까지 최소 비용을 구한다.
> 2. 트리의 구조를 이용하여 경로를 이동하면서 start 지점을 end 인덱스에 저장한다.
> 3. while문을 통해 트리에 end인덱스에 해당되는 start를 계속 반환한다. (start와 end가 동일하기 전까지)

```python
import sys
sys.stdin = open('input.txt')
from collections import defaultdict
from heapq import heappush,heappop
input=sys.stdin.readline
def dijkstra(start):
    dist[start] = 0
    heap = []
    heappush(heap,(0,start))
    while heap:
        wei,now = heappop(heap)
        if dist[now] < wei:
            continue
        for next_node, next_wei in graph[now]:
            next_cost = wei + next_wei
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                prev_node[next_node] = now
                heappush(heap,(next_cost,next_node))

N = int(input())
M = int(input())
graph = defaultdict(list)
dist = [float('inf')] * (N + 1)
prev_node = [0] * (N+1)
for i in range(M):
    start,end,wei = map(int,input().split())
    graph[start].append((end,wei))

start, end = map(int,input().split())
dijkstra(start)
print(dist[end])
path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))
``` 

#### 🎙 백준 12869 뮤탈리스크
> 1. 적의 체력을 깎는 최소한의 횟수를 구하기 위해 DP를 쓴다. 
> 2. DP는 각 SCV의 원소를 하나씩 대응시켜 최소 공격 횟수를 각 DP에 저장한다.

```python
from collections import deque

N = int(input())
SCV = list(map(int, input().split()))
SCV += [0] * (3 - len(SCV))

# 공격 조합 설정
attacks = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

# DP 테이블 초기화
DP = [[[float('inf')] * 61 for _ in range(61)] for __ in range(61)]

# BFS 초기 설정
Q = deque([SCV])
DP[SCV[0]][SCV[1]][SCV[2]] = 0

while Q:
    a, b, c = Q.popleft()

    # 가능한 모든 공격 조합에 대해 새로운 상태를 계산
    for attack in attacks:
        nx, ny, nz = max(0, a - attack[0]), max(0, b - attack[1]), max(0, c - attack[2])

        # 새로운 상태에서의 최소 공격 횟수를 갱신할 수 있는 경우
        if DP[nx][ny][nz] > DP[a][b][c] + 1:
            DP[nx][ny][nz] = DP[a][b][c] + 1  # 최소 공격 횟수 갱신
            Q.append((nx, ny, nz))  # 새로운 상태를 큐에 추가

# 모든 적의 체력을 0으로 만드는 최소 공격 횟수 출력
print(DP[0][0][0])

```

#### 👔 백준 24553 팰린드롬 게임
> 1. 처음 시작하는 경우에는 한자릿수면 무조건 승리한다.
> 2. 10의 배수인 경우 전부 다가져가지 못하기 때문에, 후발주자가 승리한다.
> 3. 따라서 10의 배수가 아닐때만 승리하는 평가식을 적으면 된다.
```python
# 24553 팰린드롬 게임
for _ in range(int(input())):
    # N이 10의 배수인 경우 선공이 무조건 승리
    print(0 if int(input()) % 10 else 1)
```

#### ❤️‍🔥 프로그래머스 92335 k진수에서 소수 개수 구하기
> 1. 먼저, 주어진 문자열을 0을 기준으로 분리한다.
> 2. 각 문자를 숫자로 변환한 후, 소수인지 판정하고 카운트를 한다.

```py
# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt
```