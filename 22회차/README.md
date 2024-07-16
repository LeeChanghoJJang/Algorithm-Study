## Algorithm Study 21회차 회의 (24.7.14.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 7월 14일 일요일 오후 7시  
        - 방식 : 디스코드

    나. 차주 예정 일정
        - 시간 : 7월 20일 토요일 오후 7시  
        - 방식 : 디스코드 

    다. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 임경태 - 이상현 - 이창호 - 이권민 - 박동현 - 윤예리 - 최지우 (순서는 매번 랜덤으로 변경 예정) 
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
    - 백준 12015 가장 긴 증가하는 부분 수열2(골2)
   ###### 2. 예리
    - 백준 2096 내려가기(골 5)
   ###### 3. 경태
    - 백준 14462 소가 길을 건너간 이유 8 (골3)
   ###### 4. 동현
    - 백준 2023 신기한 소수(골5)
   ###### 5. 상현
    - 백준 29703 펭귄의 하루(골4)
   ###### 6. 지우
    - 백준 13549 숨바꼭질3(골5)
   ###### 7. 권민
    - 백준 2170 선긋기(골5)
    
### 🤢 문제 선정
   ###### 1. 창호
    - 백준 24337 가희와 탑(골3)
   ###### 2. 예리
    - 백준 2281 데스노트 (골3)
   ###### 3. 경태
    - 백준 9082 지뢰찾기 (골4)
   ###### 4. 동현
    - 백준 7432 디스크 트리 (골3)
   ###### 5. 상현
    - 백준 25513 빠른 오름차순 탐색 (골5)
   ###### 6. 지우
    - 백준 20040 사이클 게임 (골4)
   ###### 7. 권민
    - 백준 3584 가장 가까운 공통조상 골4
    
### 🏅 스터디 내용 
#### 🎈 백준 2023 신기한 소수
> 1. `dfs`을 이용하여 해당 넘버가 소수면, 다음 차례로 넘어감. (num -> num + (13579))
> 2. 그리고 한자리수로는 2,3,5,7이 있으므로 4번의 dfs를 돌린다.

```python
N = int(input())


def dfs(num, idx):
    if idx == N:
        if isPrime(num):
            print(num)
        return
    
    for i in range(1, 10, 2):
        if isPrime(num * 10 + i):
            dfs(num*10+i, idx+1)
    

def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if not num%i:
            return False
    return True


dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)

```
#### 🧰 백준 2096 내려가기
> 1. 메모리 초과 이슈가 있으므로, dp는 1차원배열로 하며, 계속 갱신해준다.
> 2. 이전의 가장 max값(위치에 따라 다름)과 현재값 중 큰 값으로 배열을 갱신한다.
> 3. 마지막 배열에서 max값과 min값을 도출한다.

```python
import sys
input = sys.stdin.readline

n = int(input())
dp_max = list(map(int, input().split()))
dp_min = dp_max[:]

for i in range(1, n):
    a, b, c = map(int, input().split())

    dp_max = [a + max(dp_max[0], dp_max[1]), b + max(dp_max[0], dp_max[1], dp_max[2]), c + max(dp_max[1], dp_max[2])]
    dp_min = [a + min(dp_min[0], dp_min[1]), b + min(dp_min[0], dp_min[1], dp_min[2]), c + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))


```

#### ⚽ 백준 2170 선 긋기
> 1. 최소 힙을 활용하여 시작점이 최소인 순으로 나오게 한다.
> 2. 만약, 그 다음 선의 시작점이 갱신된 선과 겹친다면 끝점의 맥스값까지 선을 갱신하고, 안겹치면 결과값에 기존 선의 길이를 저장하고 새로운 선의 정보를 저장한다.
> 3. 최종 정보를 저장하고, 마지막으로 저장된 선의길이도 저장한다.

```python
import sys
from heapq import *
sys.stdin = open('input.txt')

n = int(input())
heap =[]
for _ in range(n):
    a,b = map(int,input().split())
    heappush(heap,(a,b))
result = 0
start, end = float('-inf'),float('-inf')
while heap:
    a,b = heappop(heap)
    if start == end == float('-inf'):
        start = a; end = b
    elif start <= a <= end:
        end = max(end,b)
    elif end < a:
        result += end- start
        start = a; end = b

result += end - start
print(result)
```

#### 🖌 백준 12015 가장 긴 증가하는 부분수열 2
> 1. 가장 긴 증가하는 부분수열을 저장하기 위해, `이진 탐색`을 통해 가장 긴 증가하는 부분수열의 인덱스값을 구한다.
- 기존에 없는 값이면, 그 타겟의 숫자에 크기에 따라 위치할 수 있도록 선정한다.
- 기존에 있는 값이면 그냥 넘어간다.
> 2. 주어진 sequence를 순회하면 그 때 저장된 가장 긴 증가하는 부분수열의 길이를 반환한다.

```python
import sys
sys.stdin = open('input.txt')
def custom_bisect_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def lis_length(sequence):
    if not sequence:
        return 0

    lis = []

    for num in sequence:
        pos = custom_bisect_left(lis, num)
        if pos < len(lis):
            lis[pos] = num
        else:
            lis.append(num)

    return len(lis)

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))
print(lis_length(A))
``` 

#### 🎙 백준 13549 숨바꼭질 3 
> 1. `bfs`를 통해 수빈이가 동생을 찾는 가장 빠른 시간을 도출한다.
> 2. 순회할 때, 수빈이가 동생보다 큰 위치에 있으면 차이를 반환하고, 그 외에는 `bfs`를 돌린다.
> 3. 우선 순간이동하는 경우가 가장 초가 짧으므로, 순간이동의 경우에는 appendleft를 이용하여 값을 추가해준다. 그 외에는 순차적으로 순회한다.
> 4. 타겟을 찾으면 해당 위치의 dp값을 반환하고, 그 외에는 -1을 반환한다.

```python
from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.read
n, k = map(int, input().split())

def bfs(n, k):
    if n >= k:
        return n - k

    maximum = 100001
    dp = [float('inf')] * maximum
    visited = [False] * maximum
    queue = deque([n])
    dp[n] = 0
    visited[n] = True

    while queue:
        current = queue.popleft()
        if current == k:
            return dp[current]

        for next in [current - 1, current + 1, current * 2]:
            if 0 <= next < maximum and not visited[next]:
                visited[next] = True
                if next == current * 2:
                    dp[next] = dp[current]
                    queue.appendleft(next)  # 순간이동은 0초이므로 우선적으로 처리
                else:
                    dp[next] = dp[current] + 1
                    queue.append(next)

    return -1

print(bfs(n, k))

```

#### 👔 백준 14462 소가 길을 건너는 이유 8 
> 1. `dp`를 이용해서 풀이. `dp`는 양쪽 소의 위치까지 최대 횡단보도 갯수. 만약, 양쪽에 소가 친하면 양쪽 다 이전 위치 다음으로 이동하고, +1을 해줌.
> 2. 안 친할 경우, 한쪽에서 한칸 전의 소의 위치일 때, 값끼리 비교하여 더 큰 수를 저장시킴.

```py
import sys
input = sys.stdin.readline

N = int(input().strip())
lefts = [int(input().strip()) for _ in range(N)]
rights = [int(input().strip()) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        if abs(lefts[i] - rights[j]) <= 4:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
# 그 전꺼에서 넘어온것들 비교
print(dp[N][N])

```

#### ❤️‍🔥 백준 29703 펭귄의 하루
> 1. 펭귄의 시작점과 홈의 위치를 별도로 좌표로 저장하고, 해당 위치를 E로 변경한다.(시작점이나 홈도 지나쳐도 되기 때문)
> 2. `BFS`를 돌려 위험지역이 아니면서 방문하지 않은 경우만 순회하며, visit에는 물고기 서식지 방문여부도 저장한다.
> 3. 만약 물고기 서식지를 방문했고, 홈으로 왔을 때에는 해당 시간을 반환한다.

```py
from collections import deque
import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

N, M = map(int,input().split())
Map = [list(input()) for _ in range(N)]
Dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N) :
    for j in range(M) :
        if Map[i][j] == 'S' : p, q = i, j ; Map[i][j] = 'E'
        elif Map[i][j] == 'H' : r, s = i, j ; Map[i][j] = 'E'

D = deque([[0, p, q]])
visit = [[[-1] * M for _ in range(N)] for _ in range(2)]
visit[0][p][q] = 0

while D :
    d, x, y = D.popleft()
    if d == 1 and x == r and y == s : exit(print(visit[d][x][y]))

    for a, b in Dir :
        nx = x+a ; ny = y+b
        if 0<=nx<N and 0<=ny<M and Map[nx][ny] != 'D' :
            if Map[nx][ny] == 'E' and visit[d][nx][ny] == -1 :
                visit[d][nx][ny] = visit[d][x][y]+1
                D.append((d, nx, ny))
            elif Map[nx][ny] == 'F' and visit[1][nx][ny] == -1 :
                visit[1][nx][ny] = visit[d][x][y]+1
                D.append((1, nx, ny))
print(-1)
```
