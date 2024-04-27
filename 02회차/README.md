## Algorithm Study 2회차 회의 (24.2.12.) 

### 🪙 회의개요
    가. 금일 일정 
        - 시간 : 2월 12일 월요일 9시 30분
        - 장소 : 커피팀버 김해장유점

    나. 차주 예정 일정
        - 시간 : 2월 17일 토요일 10시
        - 방식 : 디스코드를 통한 비대면 회의  

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 8문제
    다. 난이도 : 최대 백준 골드 하위 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

###### 1. 예리 
    - 2346 풍선 터뜨리기(백준 실버 3)
    - 1931 회의실 배정(백준 실버 1)
###### 2. 상현
    - 2583 영역 구하기(백준 실버 1)
    - 1463 1로 만들기(백준 실버 3)
###### 3. 창호
    - 1697 숨바꼭질(백준 실버 1)
    - 9095 1,2,3 더하기(백준 실버 3)
###### 4. 경태
    - 2606 바이러스(백준 실버 3)
    - 1149 RGB 거리(백준 실버 1)

### 🏅 스터디 내용 
#### 🎈 백준 1343 
> 메서드(replace)를 활용하여 immutable 문자열의 부분만 변경 
```python
# 'XXXX'를 'AAAA'로 변경한 후, 남은 문자열에서 'XX'를 'BB'로 변경
board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')
# 
if 'X' in board: print(-1)
else: print(board)
```
#### ⚽ 백준 2630 
> 재귀함수를 이용해 지속적으로 분할하여 정지조건을 충족하는 경우에만 정지
1. 구하고자 하는 변수 설정
2. 조건을 충족하기 위해 탐색 
3. 정지조건을 충족하지 않은 경우 분할
4. 정지조건을 충족한 경우 결과값 반환

```python
def count_(row, col, N) :
    # 구하고자 하는 목표변수 설정 
    global white, blue
    # 목표변수를 구하기 위한 임시변수 설정
    color = list_[row][col]
    # 모든 배열을 순회 
    for i in range(N) :
        for j in range(N) :
            # 정지조건을 충족하지 않을 경우
            if color != list_[row + i][col + j]:
                # 분할해서 재귀함수 호출
                count_(row, col, N // 2)
                count_(row, col + N // 2, N // 2)
                count_(row + N // 2, col, N // 2)
                count_(row + N // 2, col + N // 2, N // 2)
                return True
    # 정지조건을 충족하고 반복문을 나올 때
    if color == 0:
        white += 1
    else:
        blue += 1
``` 

#### 💢 백준 3986
1. 첫번째 방법 : 스택을 이용
    - input에서 원하는 데이터만 뽑아 stack 저장
    - 반복문으로 input 순회
    - 각 요소와 스택의 top 비교
    - 일치 : top 제거, 불일치 : append
```python
# input을 받아 stack에 저장하는 방식 이용
for i in range(N):
    stack = []
    str_ = input()

    # input을 순회
    for char_ in str_:

        # 각 요소와 스택의 top 비교
        # 일치하는 경우 stack의 top을 제거
        if stack and char_ == stack[-1]:
            stack.pop()

        # 불일치하는 경우 요소를 stack에 append
        else:
            stack.append(char_)

    # 스택 안비면 
    if not stack:
        result += 1

print(result)
```
2. 문자열의 `replace` 메서드 활용
    - 길이의 짝수 여부 확인(조건 1)
    - 문자열이 회문이면 `True` 반환
    - 반복문 순회하여 연속된 문자열 소거
    - stack보다 효율적
```python
def good_words(word): 
    # 조건 1 평가
    if (word.count('A') % 2 == 0) and (word.count('B') % 2 == 0):
        # 조건 2 평가 - 회문
        if word == word[::-1]:
            return 1
        # 조건 2 평가 - 소거
        while ('AA' in word) or ('BB' in word):
            if 'AA' in word:
                word = word.replace('AA', '')
            elif 'BB' in word:
                word = word.replace('BB', '')

    # 좋은 단어인지 평가
    if word: return 0
    else: return 1

ans = 0
for _ in range(int(input())):
    ans += good_words(input())
print(ans)
```
3. 특이점 : `replace`가 시간 많이 걸릴거라 했으나 `if`를 써서 회문인 경우에는 바로 출력하여 시간 줄임

#### 💞 백준 11053
> `Dynamic programming` + `count배열` 활용
1. 정적 카운트배열 할당(최대값 범위)
2. 반복문을 순회하면서, 이전 배열의 최대값에서 +1한 값을 카운트배열에 저장
3. 카운트배열의 최대값 출력 
```python
N = int(input())
num_list = list(map(int, input().split()))

# dp를 이용한 풀이
# 수열을 이루는 수의 최댓값이 1000이므로 길이가 1001인 max_seq 선언
max_seq = [0] * 1001

for num in num_list:
    # max_seq[num]은 num 숫자를 마지막으로 가지는 수열 중 가장 긴
    # 증가하는 부분 수열의 길이와 같음
    max_seq[num] = max(max_seq[:num]) + 1
print(max(max_seq))
```

#### 🐷 백준 11660
> `Dynamic programming` 활용
1. 원배열과 별도로 누적합을 저장하기 위한 배열 선언
2. 누적합 = 서쪽 좌표의 누적합 + 북쪽 좌표의 누적합 - 북서쪽 좌표의 누적합 + 본인 좌표의 값
3. `메모이제이션`과 주어진 배열을 이용하여 미리 누적합 배열 계산
4. 구하고자 하는 범위의 시작좌표를 기준으로 끝좌표까지 누적합 계산 
```python
import sys
N,M = map(int,sys.stdin.readline().split())
# 주어진 배열 DP에 입력
DP = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# 누적합을 저장하기 위한 배열 선언 
DP_sum = [[0]*(N+1) for _ in range(N+1)]

# 중첩 반복문 활용하여 누적합 배열 계산
for row in range(1,N+1):
    for col in range(1,N+1):
        # 서쪽누적 + 북쪽누적 - 북서쪽누적 + 당 좌표값
        DP_sum[row][col] = DP_sum[row-1][col] + DP_sum[row][col-1] - DP_sum[row-1][col-1] + DP[row-1][col-1]

# 시작좌표 (x1,y1) 에서 끝좌표(x2,y2)사이 값 구하기
for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(DP_sum[x2][y2] - DP_sum[x1-1][y2] - DP_sum[x2][y1-1] + DP_sum[x1-1][y1-1])
```
#### 🌱 백준 14888
> 백트래킹 이용
1. 구하고자 하는 min, max 변수 설정
2. 스택의 구조를 활용하여 재귀함수 호출
```python
def dfs(temp, index):
    global n, min_, max_, num_list, operator_list

    # num_list의 모든 수를 계산에 사용했으면 최솟값, 최댓값을 저장
    if index == n:
        min_, max_ = min(min_, temp), max(max_, temp)
        return True

    for i in range(4):
        if operator_list[i] > 0:
            operator_list[i] -= 1

            # 더하기
            if i == 0:
                dfs(temp + num_list[index], index + 1)

            # 빼기
            elif i == 1:
                dfs(temp - num_list[index], index + 1)

            # 곱하기
            elif i == 2:
                dfs(temp * num_list[index], index + 1)

            # 나누기
            else:
                # 문제에서 나눗셈은 몫만 취한다고 함
                if temp >= 0:
                    dfs(temp // num_list[index], index + 1)

                # 문제에서 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 
                # 그 몫을 음수로 바꾼 것과 같다고 했음
                else:
                    dfs(-(-temp // num_list[index]), index + 1)
                    
            # 그 전의 상태로 돌아가야하기 때문에 연산자의 개수를 원래대로 복구
            operator_list[i] += 1

n = int(input())
num_list = list(map(int, input().split()))

# 연산자의 개수를 operator_list에 배열의 형태로 저장
operator_list = list(map(int, input().split()))

# min,max의 default값 선언
min_ = 10 ** 9
max_ = -min_

dfs(num_list[0], 1)

print(f'{max_}\n{min_}')
```

#### 👩‍❤️‍👨 백준 17276 
> `델타 탐색`과 `큐`의 구조를 이용
- 중간부터 시작하여 점차 순회하는 구조
- `델타`를 회전시키는 방법으로 효율적인 코드 구성
```python
for tc in range(int(input())):
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    size, degree = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(size)]
    temp = [[0] * 8 for _ in range(size//2)]

    # 회전시켜야 할 값을 임시배열 temp에 저장 
    for l in range(size//2):
        # 8방향 순회 
        for r in range(8):
            ni = size//2 + di[r] * (l+1)
            nj = size//2 + dj[r] * (l+1)
            temp[l][r] = arr[ni][nj]

    # 숫자를 회전하기 위해 델타탐색 인덱스를 회전
    turn = (degree // 45) % 8
    # 시계 방향
    if turn > 0:
        for _ in range(turn):
            di.append(di.pop(0))
            dj.append(dj.pop(0))
    # 반시계 방향
    else:
        for _ in range(-turn):
            di.insert(0, di.pop())
            dj.insert(0, dj.pop())

    # 회전시킨 숫자들을 배열에 입력
    for l in range(size//2):
        for r in range(8):
            ni = size//2 + di[r] * (l+1)
            nj = size//2 + dj[r] * (l+1)
            arr[ni][nj] = temp[l][r]

    for i in range(size):
        print(*arr[i])

```

#### 🍁 swea 1868
> `델타탐색`과 `BFS` 이용
1. 주변 지뢰가 있는 숫자만큼 모든 배열에 숫자 표시
2. 아래에 해당하는 경우 클릭수를 1 증가하고, 전부 *표시
    - 숫자 0 : 주변 확산 + 별표시
    - 0 이외 숫자 : 별표시
3. 남은 경우는 `0이 아닌 숫자`와 *밖에 없음
4. `0이 아닌 숫자`는 하나씩 클릭해줄 수 밖에 없으므로, 하나씩 더하기
```python
from collections import deque
# 1. 8방향에 지뢰 숫자가 있는만큼 모든 배열에 숫자로 표시하기
def count_land_mine(x,y):
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny <N and arr[nx][ny] =='*':
            cnt +=1
    arr[x][y] = cnt

# 2. 0이 있으면 클릭 +1 해주고, 주변 숫자 모두 *로 표시하여 클릭수에 가산안되게끔 하기 
def make_land_mine(x,y):
    queue = deque([[x,y]])
    arr[x][y]='*'
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] ==0:
                    arr[nx][ny]='*'
                    queue.append([nx,ny])
                elif arr[nx][ny] != '*':
                    arr[nx][ny]='*'

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 8방향 설정
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, -1, 1, 1, -1]
    click = 0
    # 좌표가 .인 경우, 그 배열의 8방향에 위치한 지뢰 숫자만큼 좌표에 표기
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='.':
                count_land_mine(i,j)
    # 전체 갯수가 0부터 시작하고, 0인 좌표를 찾으면 주변 전부 *로 표시
    # 0이 아닌 숫자 발견할 때는 거기까지만 *로 표시
    total_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==0:
                total_cnt +=1
                make_land_mine(i,j)
    # 0도 없고, 남은건 0이 아닌 숫자밖에 없으며, 발견시마다 카운트 세기
    for i in range(N):
        for j in range(N):
            if arr[i][j] !='*':
                total_cnt +=1
    print(f'#{tc} {total_cnt}')

```
#### 🍅 swea 2806
> `백트래킹` 문제로, `dfs`와 `인접리스트`를 활용하여 문제 풀이
```python
# 퀸을 현재 위치에 놓을 수 있는지 확인
def is_valid(col):
    return all(row[i] != row[col] and abs(row[col] - row[i]) != col - i for i in range(col))

# 1열부터 시작해서 퀸을 차례대로 놓기 시작함
# 만약 N열까지 퀸을 놓는 데 성공했다면 cnt의 값에 1을 더해줌
def dfs(col, N):
    cnt = 0

    if col == N:
        return 1
    else:
        for i in range(N):
            # 퀸을 i + 1 행 col + 1 열에 놓음
            row[col] = i

            # 만약 그 칸에 퀸을 놓아도 아무런 문제가 없으면 다음 열로 넘어감
            if is_valid(col):
                cnt += dfs(col + 1, N)
    return cnt

T = int(input())

for tc in range(T):
    N = int(input())

    # row[num] 은 num + 1 열에 퀸이 위치한 행의 번호 - 1 을 나타냄
    row = [0] * N

    print(f'#{tc + 1} {dfs(0, N)}')
```

#### 🍆 swea 4259
1. C언어 방식 이용
```python
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    result =0
    # 10을 나눈 몫을 밑으로, 나머지를 지수로 하여 result값 합산
    for i in numbers:
        k,v = divmod(i,10)
        result+=k**v
    print(f'#{tc} {result}')
```
2. 문자열의 슬라이싱으로 구분
```python 
for tc in range(T):
    n = int(input())
    num_list = input().split()
 
    sum_ = 0

    # 입력받은 각 숫자마다 끝자리 수 전까지의 수를 끝자리 수만큼 제곱을 해주어
    # 모두 더한 합을 구한 후 출력
    for num in num_list:
        sum_ += int(num[:-1]) ** int(num[-1])
 
    print(f'#{tc + 1} {sum_}')
```

#### 🌎 swea 12173
> 통상 2차원 배열을 활용하여 문제를 풀었으나, 1차원 리스트를 활용하여 `Dynamic Programming` 구현
1. 각 행을 입력받을 때마다, 각 행의 누적합 계산
2. 이동하는 것은 위로오거나 왼쪽으로 오는 경우 두 가지뿐.
3. 왼쪽의 금화 최대값과 위쪽의 금화 최대값(이전 행의 같은 위치의 값)을 합산
```python
T = int(input())

# DP 를 이용하여 접근
for tc in range(T):
    N, M = map(int, input().split())
    # max_coin[i]는 (_ + 1) 행 i 열로 이동할 때 얻을 수 있는 최대 동전 개수를
    # 저장
    max_coin = [0] * (M + 1)

    for _ in range(N):
        # row는 주어진 배열 각 행의 입력값
        row = [0] + list(map(int, input().split()))

        # 행을 순환할 때마다, 이전 행의 값을 누적해서 합산
        # 왼쪽의 누적값과 이전 행 같은 위치의 누적값을 비교하여 더 큰값에 본 좌표의 값을 더함 
        for i in range(1, M + 1):
            max_coin[i] = max(max_coin[i - 1], max_coin[i]) + row[i]

    print(f'#{tc + 1} {max_coin[-1]}')
```
#### 🏯 swea 19189
> 굉장히 큰 숫자범위 + DP의 메모이제이션 활용
1. 팩토리얼 배열을 DP로 구함(P를 지속적으로 나눠주어 연산값 감소)
2. 반복문을 통해 결과값 도출
```python
for tc in range(int(input())):
    # N : 순열의 길이 / P : 소수
    N, P = map(int, input().split())
    happy = 0
    facto = [1] * (N+1)

    # 팩토리얼 배열 입력 (기하급수적으로 수가 커지므로 P로 계속 나누어 준다)
    for i in range(2, N+1):
        facto[i] = (facto[i-1] * i) % P

    # 팩토리얼 배열을 이용하여 답안 도출
    for k in range(N):
        happy += ((facto[N-k] * (N-k)) % P * facto[k+1]) % P
        happy %= P

    print(f'#{tc+1} {happy}')
```
