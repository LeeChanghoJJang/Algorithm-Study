## Algorithm Study 26회차 회의 (24.8.24.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 8월 24일 토요일 오후 7시  
        - 방식 : 디스코드 

    나. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 이상현 - 임경태 - 이권민 - 이창호 - 박동현 - 최지우 - 윤예리  (순서는 매번 랜덤으로 변경 예정) 
            - ③ 한번에 2개를 다 브리핑하지 않고, 추가 문제는 다시 한번 로테이션을 돌 예정.
    
    다. 유지사항
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
    - 백준 14267 회사 문화 1 (골4)
   ###### 2. 예리
    - 백준 3425 고스택 (골4)
   ###### 3. 경태
    - 백준 1707 이분 그래프 (골4)
   ###### 4. 동현
    - 백준 17835 면접보는 승범이네 (골2)
   ###### 5. 상현
    - 백준 1099 알 수 없는 문장 (골3)
   ###### 6. 지우
    - 백준 1135 뉴스 전하기 (골2)
   ###### 7. 권민
    - 백준 9370 미확인 도착지 (골2)
    
### 🏅 스터디 내용 
#### 🎈 백준 1099 알 수 없는 문장
> 1. 문장에서 각 단어별로 추출하여 해석될 수 있는 단어라면 비용이 다른만큼 dp에 저장한다.
> 2. 문장의 i번째 문자에서 j번째 문자까지 해석하는데 최소비용을 누적시켜간다.

```python
# 1099 알 수 없는 문장

sentence = " " + input()
n = int(input())
words = [input() for _ in range(n)]

# dp[i][j]: 문장의 i번째 문자부터 j번째 문자까지의 구간을 해석하는 데 필요한 최소 비용
dp = [[1000] * (len(sentence)) for _ in range(len(sentence))]
dp[0][0] = 0

# 단어 해석 비용 함수
def check(word1, word2, length):
    cnt = 0
    for i in range(length):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

for i in range(1, len(sentence)+1):
    # 앞서 연결될 수 있는 단어가 없음
    if dp[i-1][0] == 1000:
        continue

    for word in words:
        length = len(word)

        # 해석될 수 있는 단어
        if sorted(sentence[i:i+length]) == sorted(word):
            dp[i][i+length-1] = min(dp[i][i+length-1], dp[i-1][0] + check(sentence[i:i+length], word, length))
            # 맨 앞에 현재 길이까지의 최솟값 업데이트
            dp[i+length-1][0] = min(dp[i+length-1][0], dp[i][i+length-1])

print(dp[-1][0] if dp[-1][0] != 1000 else -1)

```
#### 🧰 백준 1135 뉴스 전하기
> 1. 부모 리스트들을 자식리스트로 전환한다.
> 2. dfs를 통해 자식노드의 최소 시간을 구한다.  

```python
import sys
input = sys.stdin.readline
N = int(input())
parent_list = list(map(int, input().split()))
child_list = [list() for _ in range(N)]

for child in range(1, N) :
  parent = parent_list[child]
  child_list[parent].append(child)

def dfs(node) :
  if not child_list[node] :
    return 0
  result = list()
  for child in child_list[node] :
    result.append(dfs(child))
  result.sort( reverse = True)
  result = [ result[i] + i + 1 for i in range(len(child_list[node])) ]
  return max(result)

print(dfs(0))


```

#### ⚽ 백준 1707 이분 그래프
> 1. 무방향 그래프를 그려서, BFS로 이동하면 인접 노드와 다른 그룹으로 설정한다.
> 2. 만약, 방문했을 때, 같은 그룹이면 이분 그래프가 되지 않는다.

```python
import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(start, group):
    queue = deque([start])  # 시작 정점 값을 큐에 담는다.
    visited[start] = group  # 시작 정점 그룹을 설정
    while queue:  # 큐가 존재할때까지 돈다.
        x = queue.popleft()  # 큐의 맨앞 원소를 빼낸다.
        for i in graph[x]:  # 해당 정점에서 갈 수 있는 하위 정점들을 돈다.
            if not visited[i]:  # 만약 그 정점들을 아직 방문하지 않았다면
                queue.append(i)  # 그 정점들을 추가하고
                visited[i] = -1 * visited[x]  # 상위 정점과 다른 그룹으로 편성
            elif visited[i] == visited[x]:  # 만약 정점들을 이미 방문했었는데 같은 그룹이라면
                return False  # False를 바로 리턴
    return True  # 위의 조건에 걸리지 않았다면 True를 리턴

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)  # 무방향 그래프

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
```

#### 🖌 백준 3425 고스택
> 1. operator를 설정하고, while문을 반복하여 각 input을 받는다.
> 2. 해당 명령어를 수행한다.

```python
import sys
sys.stdin =open('input.txt')
input = sys.stdin.readline

while True:
    operator = []
    while True:
        operator.append(input().strip())
        if operator[-1] == 'QUIT': quit()
        if operator[-1] == 'END': break

    for _ in range(int(input())):
        try:
            stack = [int(input())]
            for o in operator:
                if o == 'END': break
                if o[:3] == 'NUM':
                    stack.append(int(o[4:]))
                elif o == 'POP':
                    stack.pop()
                elif o == 'INV':
                    stack[-1] *= -1
                elif o == 'DUP':
                    stack.append(stack[-1])
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if o == 'SWP':
                        stack.append(a)
                        stack.append(b)
                    elif o == 'ADD':
                        stack.append(a + b)
                    elif o == 'SUB':
                        stack.append(b - a)
                    elif o == 'MUL':
                        stack.append(a * b)
                    elif o == 'DIV':
                        if b / a < 0:
                            stack.append((abs(b) // abs(a)) * -1)
                        else:
                            stack.append(abs(b) // abs(a))
                    elif o == 'MOD':
                        if b < 0:
                            stack.append((abs(b) % abs(a)) * -1)
                        else:
                            stack.append(abs(b) % abs(a))
                if stack and abs(stack[-1]) > 10 ** 9: raise
            if len(stack) != 1: raise
        except:
            stack = ['ERROR']
        print(stack[0])

    print()
    input()

``` 

#### 🎙 백준 9370 미확인 도착지 
> 1. 다익스트라를 통해, s -> g- > h -> e로 향하는 거리와 s -> e로 가는 거리가 같은 경우를 추린다.
> 2. 위 도착지들을 하나씩 출력한다.
```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    end = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for i in range(t):
        end.append(int(input()))

    Ds = dijkstra(s)
    Dg = dijkstra(g)
    Dh = dijkstra(h)

    result = []
    for e in end:
        if Ds[g] + Dg[h] + Dh[e] == Ds[e] or Ds[h] + Dh[g] + Dg[e] == Ds[e]:
            result.append(e)

    result.sort()
    for r in result:
        print(r, end=' ')
```

#### 👔 백준 14267 회사 문화 1 
> 1. 칭찬 점수를 point 리스트에 저장한다.
> 2. 해당 직속상관의 칭찬점수를 누적해서 point 리스트에 저장한다.
> 3. 하나씩 출력한다.

```py
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] + list(map(int, input().split()))
point = [0] * (n + 1)

for i in range(m):  # 입력받은 칭찬점수를 더해주는 부분
    u, cnt = map(int, input().split())
    point[u] += cnt

for i in range(2, n + 1):  # 직속상관의 칭찬점수를 더해주는 부분
    point[i] += point[parent[i]]

for i in range(1, len(point)):
    print(point[i], end=' ')
```

#### ❤️‍🔥 백준 17835 면접보는 승범이네
> 1. 거리가 가장 먼 도시의 번호를 역추적하기 위해 도착지 -> 출발지의 역방향 그래프를 그린다.
> 2. 면접장 다음 도시부터 힙에 거리와 위치를 저장한다.
> 3. 그리고 방문하지 않은 곳이 나올때까지 반복문을 돌리면서, 최소 거리가 나올때 거리를 출력한다.

```py
import sys
sys.stdin = open('input.txt')
from heapq import *
input =sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for i in range(n+1)]

# 역방향 그래프
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[b].append((a,w))

# 면접장
data = [*map(int,input().split())]
check = [0]*(n+1); hq = []

# 프림의 원리를 이용
# 면접장 다음 도시부터 힙에 저장
for a in data:
    check[a] = 1
    for b,w in graph[a]:
        heappush(hq,(w,-b))

# 변수의 초기값 설정
now,w = -1,0
for _ in range(n-k):
    while 1:
        w,now = heappop(hq)
        if check[-now]:
            continue
        break
    check[-now] = 1
    for next,w1 in graph[-now]:
        heappush(hq,(w+w1,-next))
print(-now);print(w)
```
