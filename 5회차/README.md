## Algorithm Study 5회차 회의 (24.3.3.) 

### 🪙 회의개요
    가. 금일 일정 
        - 시간 : 3월 3일 일요일 9시
        - 장소 : 디스코드 통한 비대면 회의

    나. 차주 예정 일정
        - 시간 : 3월 10일 일요일 저녁 8시  
        - 방식 : 디스코드 통한 비대면 회의

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 10문제
    다. 난이도 : 최대 백준 골드 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

###### 선정 문제 (풀이만 기재)
    - 백준 2304 창고다각형 (실버 2)
    - 백준 2477 참외밭 (실버 2)
    - 백준 2578 빙고 (실버 4)
    - 백준 10157 자리배정 (실버 4)
    - 백준 10158 개미 (실버 3)
    - 백준 10163 색종이(브론즈 1)
    - 백준 13300 방배정(브론즈 2)
    - SWEA 4613 러시아 국기 같은 깃발(D4)
    - SWEA 1258 행렬찾기(D4)

### 🏅 스터디 내용 
#### 🎈 백준 2304 창고 다각형  
> 1. 가장 높이가 높은 곳의 인덱스 값 도출  
> 2. 왼쪽, 오른쪽부터 높이를 더해서 전체면적 합산 
```python
def cal(start,end,rev):
    global area; local_high = 0
    for i in range(start,end,rev):
        if i in idx:
            local_high = max(local_high,h[idx.index(i)])
        area += local_high
    

N = int(input())
idx, h = list(zip(*sorted(list(map(int, input().split())) for _ in range(N))))
h_idx = idx[h.index(max(h))]
area = max(h)
# 왼쪽부터 젤높은 기둥까지
cal(idx[0],h_idx,1)
# 오른쪽부터 젤높은 기둥까지
cal(idx[-1],h_idx,-1)
print(area)
```

#### 🧰 백준 2477 참외밭
> 1. 큰 사각형 - 작은사각형(면적)이 목표
> 2. 각 변을 구하기 위해 패턴 발견하기(3131,4242 등)
> 3. 앞 뒤에 같은 숫자가 반복되는 경우에 작은사각형의 길이가 중간에 있음
```python
K = int(input())
d, l = zip(*[list(map(int, input().split())) for _ in range(6)])
cnt = [d.count(i) for i in range(5)]
area, sub_area = 1, 1

for i in range(6):
    if cnt[d[i]] == 1:
        area *= l[i]
    # 4242 3131 같은 패턴이 나오면 중간 24,13이 작은 사각형의 가로세로길이
    elif d[(i - 1) % 6] == d[(i + 1) % 6]:
        sub_area *= l[i]

print(K*(area - sub_area))
```

#### ⚽ 백준 2578 빙고
> 구현 문제 
> 1. 빙고 수를 전부 파악하는 함수 정의 
```python
def chk_bingo():
    cnt = sum(row.count(0) == 5 for row in bingo)
    cnt += sum(col.count(0) == 5 for col in list(zip(*bingo)))
    cnt += all(bingo[row][row] == 0 for row in range(5))
    cnt += all(bingo[row][4 - row] == 0 for row in range(5))

    if cnt >= 3:
        return True
    return False

bingo = [list(map(int, input().split())) for _ in range(5)]
is_bingo = False
dict_ = {}

for row in range(5):
    for col in range(5):
        dict_[bingo[row][col]] = (row, col)
# 사회자가 호출하는 리스트
for i in range(5):
    target_list = list(map(int, input().split()))
    # 타겟 리스트 중 인덱스와 타겟넘버 
    for j, target in enumerate(target_list):
            # 타겟넘버를 갖는 행과열정보를 chk에 저장
            chk = dict_[target]
            # 행과 열정보를 바탕으로 bingo표시 
            bingo[chk[0]][chk[1]] = 0
    
            if chk_bingo():
                is_bingo = True
                print(5 * i + j + 1)
                break

    if is_bingo:
        break
```

#### 🖌 백준 10157 자리배정
> `SWEA` 달팽이숫자와 비슷한 문제
> `원형큐`의 구조를 `델타`에 활용하여 자리배정

```python
dr = ((1, 0), (0, 1), (-1, 0), (0, -1))
C, R = map(int, input().split())
seat = [[0] * C for _ in range(R)]
K = int(input())
i, j, k = 0, 0, 0

if K <= C * R:
    for _ in range(1, K):
        seat[i][j] = 1
        ni, nj = i + dr[k][0], j + dr[k][1]
        if 0 <= ni < R and 0 <= nj < C and not seat[ni][nj]:
            i, j = ni, nj
        # 만약 다음 범위가 벗어나거나, 방문한 적이 있다면 
        else:
            k = (k + 1) % 4
            i, j = i + dr[k][0], j + dr[k][1]
    print(j+1, i+1)
else:
    print(0)
```   

#### 🎙 백준 10158 개미
> `수학` 유형으로 품
> 1. 규칙성 발견 : 개미는 벽에 부딪힐때마다 방향이 변경됨
> 2. x와 y좌표는 독립적으로 움직이는 점 이용
```python
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
# 개미는 벽에 부딪힐 때마다, 방향이 전환됨 
# 경과된만큼 얼마나 이동했고 그 때의 방향을 설정
width = (p + t) // w
height = (q + t) // h
 
x = (p + t) % w if width % 2 == 0 else w - (p + t) % w
y = (q + t) % h if height % 2 == 0 else h - (q + t) % h

print(x, y)
```

#### 👔 백준 10163 색종이
> 일반적으로 색종이를 모두 탐색하는 경우에는 성능저하 됨
> 그에 따라 배열을 통째로 색종이로 만들고 카운팅 필요
```python
arr, N = [[0] * 1001 for _ in range(1001)], int(input())

for idx in range(N):
    i, j, w, h = map(int, input().split())
    
    # 배열 자체를 변경
    for nj in range(j, j+h):
        arr[nj][i:i+w] = [idx+1]*w

for idx in range(N):
    ans = 0
    for j in arr:
        ans += j.count(idx+1)
    print(ans)
```
---
#### 📀 백준 13300 방 배정 
> 각 방을 만들어 적절한 인원수를 배정하는 문제 
```python
import sys
sys.stdin = open('input.txt')
# N : 학생수, K : 한방에 최대 인원수
N,K = map(int,input().split())
cnt = 0
# 6학년까지, 남여방을 temp에 저장 
temp = [[0]*6 for _ in range(2)]
# S가 0은 여자, 1은 남자
# 인덱스 에러 방지를 위해 학년은 1빼서 저장 
for _ in range(N):
    S, Y = map(int,input().split())
    temp[S][Y-1] +=1
# 최소방은 1개이며, K개 단위로 1개씩 가산하여 cnt에 저장
for i in range(len(temp)):
    for j in range(len(temp[0])):
        cnt += (temp[i][j]-1)//K+1
print(cnt)
```
#### 🧏‍♀️ SWEA 4613 러시아 국기 같은 깃발
> 1. `완전검색` : 화이트, 블루, 레드 순으로 for문을 이용한 완전검색
```python
import sys
sys.stdin = open('input.txt')

T = int(input())
 
for tc in range(T):
    N, M = map(int, input().split())
    list_ = [list(input()) for _ in range(N)]
    # WBR색깔 중에서 각 행에 뺀 갯수를 저장
    cnt_list = [[M - row.count(char_) for row in list_] for char_ in 'WBR']
    min_ = float('inf')
    # WBR순으로 순회(가장 왼쪽이 white, 중간이 blue, 오른쪽이 Red)
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            min_ = min(min_, sum(cnt_list[0][:i] + cnt_list[1][i:j] + cnt_list[2][j:]))
 
    print(f'#{tc + 1} {min_}')
```
> 2. `백트래킹` 활용한 `완전검색`
```python
import sys
sys.stdin = open('input.txt')

orders = {'W':1,'B':2,'R':3}
def count_repaint_cost(flag, color):
    cost = 0
    for i in range(len(flag)):
        if flag[i] != color:
            cost += 1
    return cost

def backtracking(row, temp):
    global cnt
    global min_repaint_cost

    if row == N:
        # 첫 줄은 흰색, 마지막 줄은 빨간색으로 고정
        if temp[0] != 'W' or temp[-1] != 'R':
            return
        # 각 행마다  
        repaint_cost = 0
        for i in range(N):
            repaint_cost += count_repaint_cost(flag[i], temp[i])
        # cost가 젤 적은거 저장
        min_repaint_cost = min(min_repaint_cost, repaint_cost)
        return

    for char in 'WBR':
        if not temp or orders[temp[-1]] <= orders[char] <= orders[temp[-1]]+1:
            temp.append(char)
            backtracking(row + 1, temp)
            temp.pop()

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    cnt = []
    min_repaint_cost = float('inf')
    backtracking(0, [])
    print(f'#{tc} {min_repaint_cost}')
```
#### ❤️‍🔥 백준 1258 행렬찾기
> `BFS`를 활용하여 0이 아닌 부분 행렬 탐색
```python
from collections import deque
 
def bfs(row, col):
    result = []
    q = deque()
    q.append((row, col))
    visited[row][col] = True
 
    while q:
        row, col = q.popleft()
        result.append((row, col))
 
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]
 
            if not (0 <= nrow < N and 0 <= ncol < N) or visited[nrow][ncol] or not list_[nrow][ncol]:
                continue
 
            visited[nrow][ncol] = True
            q.append((nrow, ncol))
 
    if len(result) >= 2:
        return max(result)[0] - min(result)[0] + 1, max(result)[1] - min(result)[1] + 1
    return
 
T = int(input())
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
 
for tc in range(T):
    N = int(input())
    list_ = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = []
 
    for row in range(N):
        for col in range(N):
            if list_[row][col] and not visited[row][col]:
                result.append(bfs(row, col))
 
    result.sort(key = lambda x : (x[0] * x[1], x[0]))
    print(f'#{tc + 1} {len(result)}', end = ' ')
    [print(*pair, end = ' ') for pair in result]
    print()
```