## Algorithm Study 22회차 회의 (24.7.14.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 7월 27일 토요일 오후 7시  
        - 방식 : 디스코드

    나. 차주 예정 일정
        - 시간 : 8월 3일 토요일 오후 2시  
        - 방식 : 디스코드 

    다. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 이권민 - 이상현 - 임경태 - 최지우 - 이창호 - 윤예리 - 박동현 (순서는 매번 랜덤으로 변경 예정) 
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
    - 백준 12865 평범한 배낭(골5)
   ###### 2. 예리
    - 백준 2293 동전 1(골5)
   ###### 3. 경태
    - 백준 2141 우체국(골4)
   ###### 4. 동현
    - 백준 2836 수상택시(골3)
   ###### 5. 상현
    - 백준 2448 별찍기 - 11 (골4)
   ###### 6. 지우
    - 백준 9252 LCS2 (골4)
   ###### 7. 권민
    - 백준 11049 행렬 곱셈 순서(골3)
    
### 🤢 문제 선정
   ###### 1. 창호
    - 백준 1943 동전 분배(골2)
   ###### 2. 예리
    - 백준 20056 마법사 상어와 파이어볼 (골4)
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
#### 🎈 백준 2141 우체국
> 1. 중앙값을 구하는 문제와 같음
> 2. 사람들이 가장 많이 분포되어 있는 최빈값일 가능성도 높지만, 만약 사람들을 순서대로 했을 때 중앙값을 구하면 됨

```python
# 2141 우체국
N = int(input())
location = []
p = 0

# 각 위치와 가중치를 입력받음
for i in range(1, N + 1):
    a, b = map(int, input().split())
    location.append((a, b))
    p += b  # 가중치의 합을 계산

# 위치를 기준으로 정렬
location.sort(key=lambda x: x[0])

# 중간 위치를 찾기 위한 변수 초기화
cnt = 0

# 위치를 순회하며 중간 위치를 찾음
for i in range(N):
    cnt += location[i][1]  # 현재까지의 가중치 합
    if cnt >= p / 2:  # 현재까지의 가중치 합이 총 가중치 합의 절반 이상인 경우
        print(location[i][0])  # 해당 위치를 출력
        break

```
#### 🧰 백준 2293 동전 1
> 1. 전형적인 dp문제로, 동전 단위마다 누적해서 dp값을 더해주면 됨 

```python
import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [1] + [0] * (k+1)

for i in coins:
    for j in range(i,k+1):
        dp[j] += dp[j-i]
print(dp[k])

```

#### ⚽ 백준 2448 별 찍기 - 11
> 1. 기본 삼각형을 먼저 저장한다.
> 2. 칸수를 맞춰주기 위해 재귀를 한번 할 때마다 위 삼각형을 밑에 두개 추가
> 3. 삼각형의 길이가 N만큼 되면 종료

```python
def recursion(temp):
    len_ = len(temp)
    result  = []

    for row in temp:
        result.append(' ' * len_ + row + ' ' * len_)

    for row in temp:
        result.append(row + ' ' + row)

    return result

N = int(input())
temp = [
    '  *  ',
    ' * * ',
    '*****',
]

while len(temp) != N:
    temp = recursion(temp)

[print(row) for row in temp]
```

#### 🖌 백준 2836 수상택시
> 1. 순방향이면 어차피 가는길에 내려주면 되기 때문에 고려대상이 아님
> 2. 역방향인 경우만 L에 담고, 시작점을 기준으로 내림차순으로 저장한다.
> 3. 만약 이전 구간과 겹치는 경우에는 병합해주고, 겹치지 않는 경우는 별도로 저장한다.
> 4. 구간마다 왕복구간을 더해준다. 처음부터 마지막점에 

```python
import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

L = []
N, M = map(int, input().split())
for _ in range(N):
    s, e = map(int, input().split())
    if s > e:
        L.append([e, s])

L.sort(key=lambda x: -x[1])
tmp = []
ts, te = L[0]
for i in range(1, len(L)):
    s, e = L[i]

    if ts <= e:  # <=te (sort에 의해 보장됨)
        ts = min(ts, s)

    else:  # e < ts
        tmp.append([ts, te])
        ts, te = s, e

tmp.append([ts, te])

answer = M
for i in range(len(tmp)):
    answer += 2 * (tmp[i][1] - tmp[i][0])

print(answer)

``` 

#### 🎙 백준 9252 LCS 4
> 1. LCS 로직을 DP를 이용해 구한다.
> 2. 마지막 dp에 저장된 LCS 값부터 시작하고, 두 점이 일치하면 역순으로 값을 리스트에 저장한다.
> 3. 순회할 때, 해당 위치에서의 dp값을 비교하여 더 큰쪽부터 포인터를 차감한다.

```python
import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

a, b = input().strip(), input().strip()
la = len(a)
lb = len(b)
dp = [[0] * (lb+1) for _ in range(la+1)]
for i in range(1,la+1):
    for j in range(1,lb+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[la][lb])
# LCS 추적하여 출력
if dp[la][lb] != 0:
    lcs = []
    x, y = la, lb
    while x > 0 and y > 0:
        if a[x - 1] == b[y - 1]:
            lcs.append(a[x - 1])
            x -= 1
            y -= 1
        elif dp[x - 1][y] >= dp[x][y - 1]:
            x -= 1
        else:
            y -= 1
    print(''.join(reversed(lcs)))

```

#### 👔 백준 11049 행렬 곱셈 순서
> 1. 기본 행렬 곱셈 : 왼쪽 행렬 행 * 왼쪽 행렬 열 * 오른쪽 행렬 열
> 2. 간격별로 연산을 해준다.
> 3. 각 부분 행렬의 곱셈 횟수와 두 행렬의 곱셈횟수 중 더 최적분할을 dp에 저장해준다.
```py
import sys
sys.stdin = open('input.txt')

input =sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 곱셈의 최소 횟수 행렬
dp = [[0]*N for _ in range(N)]

for diagonal in range(1, N):  # dp[i][i]는 자기 자신의 행렬이기 때문에 값이 0
    for i in range(0, N-diagonal):  # 대각선의 우측 한 칸씩 이동
        j = i + diagonal  # 현재 대각선에서 몇 번째 원소인지
        # 차이가 1밖에 나지 않는 칸
        if diagonal == 1:
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue

        dp[i][j] = float('inf')
        # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
        for k in range(i, j):  # k값으로 최적분할 찾기
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

print(dp[0][N-1])

```

#### ❤️‍🔥 백준 12865 평범한 배낭
> 대표적인 냅색 문제로, 이차원 dp에 행에는 물건 갯수, 열에는 무게를 지정해서 해당 행렬에는 최적의 가치가 저장된다.
```py
import sys
sys.stdin = open('input.txt')
n,k = map(int,input().split())
thing = [[0,0]] + [list(map(int,input().split()))]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):

        w= thing[i][0]
        v= thing[i][1]
        
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k])
```
