## Algorithm Study 3회차 회의 (24.2.17.) 

### 🪙 회의개요
    가. 금일 일정 
        - 시간 : 2월 17일 토요일 10시
        - 장소 : 디스코드 비대면 스터디

    나. 차주 예정 일정
        - 시간 : 2월 24일 토요일 9시 30분
        - 방식 : 커피팀버 김해장유점

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 10문제
    다. 난이도 : 최대 백준 골드 하위 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

###### 1. 예리 
    - 14889 스타트와 링크(백준 실버 1)
    - 19185 육십갑자(swea D3)
###### 2. 상현
    - 1753 최단경로(백준 골드 4)
    - 11725 트리의 부모 찾기(백준 실버 2)
###### 3. 창호
    - 1891 사분면(백준 골드 4)
    - 1182 부분수열의 합(백준 실버 2)
###### 4. 경태
    - 7662 이중 우선순위 큐(백준 골드 4)
    - 1012 유기농 배추(백준 실버 2)
###### 5. 동현
    - 10026 적록색약(백준 골드 5)
    - 2644 촌수계산(백준 실버 2)

### 🏅 스터디 내용 
#### 🎈 백준 1149 RGB거리
> `Dynamic Programming`을 이용하여 R,G,B의 누적 최솟값 저장 
> 각 배열의 행을 순회하면서 열에 최소값을 저장하고 해당 좌표를 인덱싱하면 해당 좌표의 최솟값 도출 가능

```python
DP = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    DP[i][j] = min(DP[i - 1][(j+1)%3],DP[i - 1][(j+2)%3]) + DP[i][0]
print(min(DP[N-1]))
```
#### 🧼 백준 1463 1로 만들기
> `Dynamic Programming`을 이용하여 아래와 같이 상황 분배
> 1. 6으로 나눠지는 경우
> 2. 3으로 나눠지는 경우
> 3. 2으로 나눠지는 경우
> 4. 그 외의 경우

> `if-else`문으로 각 상황에 DP 배열에 최솟값을 저장 
```python
N = int(input())
DP = [0] * (N+1)
for n in range(2, N+1):
    if not n % 3 and not n % 2:
        DP[n] = min(DP[n//3], DP[n//2]) + 1
    elif not n % 3:
        DP[n] = min(DP[n-1], DP[n//3]) + 1
    elif not n % 2:
        DP[n] = min(DP[n-1], DP[n//2]) + 1
    else:
        DP[n] = DP[n-1] + 1

print(DP[N])
```

#### ⚽ 백준 1697 숨바꼭질
> 첫번째 방법 : DFS 이용 (`34972KB 92ms`)
> Top-Down 방식이용(`동생 -> 수빈`을 찾아가는 방식)
```python 
visit = [0] * 100001
stack = [ds]
while ds != sb :
    tc = stack.pop(0)
    if tc == sb :
        print(visit[tc])                                # 찾은 경우 - visit에 담긴 값 추출
        break
    else :
        if tc > sb :                                    # 현재 수빈의 위치보다 동생의 위치가 큰 경우
            if tc % 2 == 0:                             # 동생이 짝수 위치에 있는 경우
                if visit[tc//2] == 0:                   # 2로 나눈값이 visit 에 없으면
                    stack.append(tc//2)                 # 그대로 추가하고 
                    visit[tc//2] = visit[tc] + 1

            if tc < 100000 and visit[tc+1] == 0 :       # 도대체 어디까지 가는지 인덱스 에러가 계속 나서, 제한했습니다
                stack.append(tc+1)
                visit[tc+1] = visit[tc] +1

            if visit[tc-1] == 0:
                stack.append(tc-1)
                visit[tc-1] = visit[tc] +1
        else :                                          # 현재 수빈의 위치보다 동생의 위치가 작은 경우
            if visit[tc+1] == 0:
                stack.append(tc+1)
                visit[tc+1] = visit[tc] +1
if ds==sb: 
    print(0)
```
> 두번째 방법 : BFS 이용 (`34196KB 124ms`)
> Bottom-Up 방식 이용 
> 1. 시간절약을 위해 N이 3/4*K보다 큰경우와 나머지로 구분
> 2. X-1,X+1,2*X 해당되는 영역에 지속적으로 +1 및 Q에 원소 전부 추가 
> 3. `if-else`문으로 K와 X가 같아지면 종료.
```python
from collections import deque
# N: 수빈 위치 / K: 동생 위치
N, K = map(int, input().split())
# 거리 저장
dist = [0] * 100001
# 수빈 위치 > 동생 위치*(3/4) -> 차이만큼 시간 계산
if N >= 3*K//4:
    print(abs(N-K))
# 수빈 위치 < 동생 위치 -> BFS로 최단시간 탐색
else:
    Q = deque([N])
    while Q:
        X = Q.popleft()
        # 동생을 찾았다면 종료
        if X == K:
            print(dist[K])
            break
        # 동생을 찾지 못했다면 다음 지점 탐색
        for next in (X-1, X+1, 2*X):
            if 0 <= next <= 100000 and not dist[next]:
                dist[next] = dist[X] + 1
                Q.append(next)
```
> 세번째 방법 : DP 이용(`38824KB 136ms`)
> Bottom-Up 방식 이용
> 1. 수빈보다 낮은 곳은 전부 1씩 차감하여 채움
> 2. 2로 나눠지는 경우와 아닌 경우로 구분
> 3. 2로 나눠지는 경우 : min(1뺀 값 + 1, 2나눈값)
> 4. 2로 안나눠지는 경우 : min(1빼고 2나눈값 + 2, 1더하고 2나눈 값 + 2, 1뺀값 + 1)

```python
# 수빈 :N ,동생 : K
N, K = map(int,input().split())
# 수빈이 더 크면 2배는 쓸 수 없으므로 1씩 이동
if N>=K:
    print(N-K)
# 수빈이 동생보다 작을 때 아래 로직 적용
else:
    # 여유롭게 계산하고자 DP의 길이를 K의 2배정도까지 설정
    DP = [0]*2*(K+1)
    # N 밑으로는 1씩만 이동가능.
    for i in range(N):
        DP[i] = N-i
    # N보다 클 때 DP를 이용하여 누적 최소값을 더한다.
    for i in range(N+1,2*K+1):
        '''
        2로 나눠지는 경우
        1. 2로 나눈 수의 값 + 1                      
        2. 1뺀 값의 + 1
        '''
        if i%2 ==0:
            DP[i] = min(DP[i//2]+1,DP[(i-1)]+1)
            '''
            2로 안나눠지는 경우
            1. 1뺀 값을 2로 나눈 수의 값 + 2
            2. 1더한 값을 2로 나눈 수의 값 + 2
            3. 1뺀 값의 + 1
            '''
        else:
            DP[i] = min(DP[(i-1)//2]+2, DP[(i+1)//2] +2,DP[i-1]+1)
    print(DP[K])

```
#### 🧰 백준 1931 회의실 배정
> 주어진 배열을 `tuple`로 바꾸면 메모리와 시간절약됨
> for문을 순회하면서 `tuple`로 바꾸어 저장하는 경우에는 성능 악화됨(`tuple`은 정적인 배열을 선언할 때 활용하는 게 좋음. 나머지 할당과 복사, pop, append를 이용하면 리스트보다 시간복잡도가 많이 걸림)
```python
# 예시 1 : meetings라는 배열 내부를 변화시킬 것이 아니고, 다른 곳에 할당과 복사를 할 것이 아니라면, tuple로 저장하는 것이 좋음
meetings = sorted([tuple(map(int,input().split())) for _ in range(N)] ,key=lambda x:(x[0],x[1])) # O
meetings = sorted([list(map(int,input().split())) for _ in range(N)] ,key=lambda x:(x[0],x[1])) # X
# 예시 2 : append와 pop을 이용할 때에는 주로 list가 tuple보다 나음
temp = []
temp.append((1,2)) #X
temp.append([1,2]) #O
```

> `list`의 `sort` 메서드과 `for`문을 활용한 그리디 알고리즘 적용
```python
T = int(input())

test_list = [list(map(int, sys.stdin.readline().strip("\n").split())) for _ in range(T)]
# 끝을 기준으로 정렬
test_list.sort(key = lambda x : (x[1],x[0]))
# test_list.sort(key = lambda x : (x[1]))  <<< 틀림. 왜? 끝 기준인데 같은 경우 앞도 정렬되야 함. 그래서 x[0] 도 후순위 정렬이 필요

end = 0
count = 0
# end이 이번 start값보다 작은 경우, end값 갱신 및 count+=1
for start_time, end_time in test_list :     
    if end <= start_time :
        count += 1
        end = end_time
print(count)
```
#### 🖌 백준 2346 풍선 터뜨리기
> `원형큐`의 개념 이용(`31120KB / 36ms`)
> 1. `enumerate` 함수를 이용하여 풍선인덱스와 번호 저장 
> 2. 반복문과 `list`의 `pop`메서드 활용하여 인덱스 추출
```python
# N: 풍선 개수 / B: 풍선 번호와 종이 번호 저장
N = int(input())
B = [[i+1, num] for i, num in enumerate(map(int, input().split()))]

pang = 0
while B:
    print(B[pang][0], end= ' ')
    n, p = B.pop(pang)
    if B:
        # 종이에 적혀있는 숫자만큼 이동
        if p < 0: pang = (pang + p) % len(B)
        else: pang = (pang + p - 1) % len(B)

``` 
> `deque`의 `rotate`메서드도 이용가능
```python
N = int(input())
num_list = deque(enumerate(map(int, input().split()), start = 1))
result = []

# 터뜨려야할 풍선을 맨 앞에 위치하게 리스트를 회전시킴
while num_list:
    # index는 터진 풍선의 번호를, num은 터진 풍선에 적힌 수를 의미
    index, num = num_list.popleft()
    result.append(index)

    # 파이썬 deque 라이브러리의 rotate(n)메서드는 덱의 요소들을
    # 오른쪽으로 n만큼 회전시킴 (n이 음수면 반대)

    # 풍선에 적힌 숫자가 양수라면, 리스트를 왼쪽으로 회전시켜줘야함
    # 음수라면 오른쪽으로 회전시켜줘야함
    if num > 0:
        num_list.rotate(1 - num)
    else:
        num_list.rotate(-num)

print(*result)
```

#### 🎙 백준 2583 영역 구하기
> DFS나 BFS 이용 (`DFS : 32588KB 72ms`)
1. 주어진 영역의 범위를 1로 색칠
2. 영역을 발견시, area 변수로 넓이 구하고, DFS,BFS로 탐색
3. 임시 리스트에 넓이를 담고 갯수 구하기 

```python
# DFS
import sys
sys.setrecursionlimit(100000)

def dfs(row, col, temp):

    # 인덱스를 벗어나거나 이미 방문한 곳 혹은 직사각형의 내부라면 0을 반환
    if not (0 <= row < len(temp) and 0 <= col < len(temp[0])) or temp[row][col]:
        return 0

    # 만약 직사각형의 내부가 아니라면 그 영역과 연결된 모든 영역을
    # 탐색하고 다른 영역을 탐색할 때마다 area의 값을 1 증가시킴
    area = 1
    temp[row][col] = 1

    area += dfs(row + 1, col, temp)
    area += dfs(row - 1, col, temp)
    area += dfs(row, col + 1, temp)
    area += dfs(row, col - 1, temp)

    return area

M, N, K = map(int, input().split())
paper = [[0] * N for _ in range(M)]
area_cnt = 0
area = []

# 주어진 직사각형의 좌표를 이용하여 직사각형들의 내부에
# 위치해 있는 칸의 값을 1증가시킴
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())

    for row in range(r1, r2):
        for col in range(c1, c2):
            paper[row][col] += 1

for row in range(M):
    for col in range(N):
        # 직사각형의 내부가 아닐 때마다 area_cnt의 값을 1 증가시킴

        if paper[row][col] == 0:
            area_cnt += 1

            # 반환된 넓이를 area에 추가
            area.append(dfs(row, col, paper))

print(area_cnt)
print(*sorted(area))
```
> 아래는 BFS 이용(`34096KB 72ms`)
```python
mport sys
sys.stdin = open('input.txt')
from collections import deque
# 델타 설정
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 일단 주어진 조건에 따라 직사각형들을 색칠하여 구역 나누기
def paint(x1,y1,x2,y2,graph):
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] =1
    return graph
    
# BFS를 활용해서 한번 0을 만난 경우, 인접한 것들도 전부 색칠해줌
def BFS(x,y):
    # area로 그 구역의 넓이 계산
    area = 1
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        graph[x][y]=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and graph[nx][ny]==0:
                graph[nx][ny]=1
                queue.append([nx,ny])
                area += 1
    return area

# M : 행 N : 열 K : 직사각형의 범위 
M,N,K = map(int,input().split())
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    # 직사각형의 범위를 시작점 행,열과 도착점 행,열로 구분해서 언팩 
    y1,x1,y2,x2 = map(int,input().split())
    # 직사각형으로 일단 전 구역 색칠
    graph = paint(x1,y1,x2,y2,graph)
temp = []
for i in range(M):
    for j in range(N):
        # BFS를 활용해서 한번 0을 만난 경우, 인접한 것들도 전부 색칠해줌 ==> temp의 길이가 총 구역의 갯수이며, 각 원소는 그 구역의 넓이
        if graph[i][j] ==0:
            temp.append(BFS(i,j))
print(len(temp))
print(*sorted(temp))
```

#### 👔 백준 2606 
> `Set`의 `update` 메서드를 이용
> 1. `Set`으로 바이러스 경로를 모두 저장하고 `list`에 담음
> 2. `list`의 각 원소를 비교하고, 교집합이 있다면 `update`를 통해 갱신
> 3. 그 중 1이 들어 있는 리스트가 있다면 길이를 도출
```python
a = int(input())        # 컴퓨터 수
b = int(input())        # 테스트 케이스 수
temp_list = []
for i in range(b):
    temp_set = set(map(int, input().split()))       # set로 받고 list에 저장
    temp_list.append(temp_set)

for j in range(b):                 
    for k in range(b):
        if temp_list[j] & temp_list[k]:             # 교집합이 있는 경우
            temp_list[j].update(temp_list[k])       # update해 한 단위로 병합

output = 0
for k in temp_list:         # 병합된 리스트의 각 원소에 대해
    if 1 in k:              # 1이 k에 들어있으면
        rem = len(k)        # 그 길이를 재서 비교
        if rem > output:
            output = rem

if output == 0:         # 없으면 0인데, 있는 경우 숙주를 제외하고 -1한 값을 출력
    print(0)
else:
    print(output-1)
```
> `BFS` 이용(`34016KB / 64ms`)
```python
rom collections import deque

Q = deque([1])                    # 덱
V = int(input())                  # 컴퓨터 개수
E = int(input())                  # 연결쌍 개수
NW = [[] for _ in range(V + 1)]   # 연결 번호 목록
visited = [None] * (V + 1)        # 방문 확인

# 연결 번호 목록 입력
for _ in range(E):
    n1, n2 = map(int, input().split())
    NW[n1].append(n2)
    NW[n2].append(n1)

# BFS 실행
cnt = 0
while Q:
    n1 = Q.popleft()
    for n2 in NW[n1]:
        if not visited[n2] and n2 != 1:
            visited[n2] = 1
            cnt += 1
            Q.append(n2)

print(cnt)
```
> DFS 이용(`31120KB / 40ms`)
```python
V = int(input())                  # 컴퓨터 개수
E = int(input())                  # 연결쌍 개수
NW = [[] for _ in range(V + 1)]   # 연결 번호 목록
visited = [False] * (V + 1)       # 방문 확인

# 연결 번호 목록 입력
for _ in range(E):
    n1, n2 = map(int, input().split())
    NW[n1].append(n2)
    NW[n2].append(n1)

# DFS 실행
def DFS(n1):
    global cnt
    for n2 in NW[n1]:
        if not visited[n2] and n2 != 1:
            visited[n2] = True
            cnt += 1
            DFS(n2)

cnt = 0
DFS(1)
print(cnt)
```
---
#### 📀 백준 9095
> `Dynamic Programming` 이용
> 규칙성을 찾아내는게 중요함
> 1,2,3으로만 어떤 수를 나타내야 함
> 전전전단계 +3, 전전단계 +2, 전단계 + 1로 해당 수를 나타낼 수 있어, 아래와 같은 수식 도출
> DP[N] = DP[N-1] + DP[N-2] + DP[N-3]

```python
DP = [0, 1, 2, 4] + [0] * 7

for c in range(int(input())):
    N = int(input())

    for i in range(4, N+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

    print(DP[N])
```