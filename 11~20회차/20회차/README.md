## Algorithm Study 20회차 회의 (24.6.29.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 6월 29일 토요일 오후 7시  
        - 방식 : 김해 커피팀버

    나. 차주 예정 일정
        - 시간 : 7월 6일 토요일 오후 7시  
        - 방식 : 디스코드

    다. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 최지우 - 임경태 - 이창호 - 윤예리 - 이상현 - 박동현 - 이권민   (순서는 매번 랜덤으로 변경 예정) 
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
    - 백준 17299 오등큰수(골3)
   ###### 2. 예리
    - 백준 2473 세 용액(골3)
   ###### 3. 경태
    - 백준 2457 공주님의 정원(골3)
   ###### 4. 동현
    - 백준 1600 말이 되고픈 원숭이 (골3)
   ###### 5. 상현
    - 프로그래머스 92341 주차 요금 계산 (Lv.2)
   ###### 6. 지우
    - 프로그래머스 49993 스킬트리 (Lv.2)
   ###### 7. 권민
    - 프로그래머스 42895 N으로 표현 (Lv.3)

### 🤢 문제 선정
   ###### 1. 창호
    - 백준 1423 원숭이 키우기(골2)
   ###### 2. 예리
    - 백준 17144 미세먼지 안녕!(골4)
   ###### 3. 경태
    - 프로그래머스 250136 석유시추 (Lv.2)
   ###### 4. 동현
    - 백준 3190 뱀(골4)
   ###### 5. 상현
    - 프로그래머스 1829 카카오 프렌즈 컬러링북(Lv.2)
   ###### 6. 지우
    - 백준 16724 피리부는 사나이(골3)
   ###### 7. 권민
    - 백준 14938 서강그라운드(골4)

### 🏅 스터디 내용 
#### 🎈 백준 1600 말이 되고픈 원숭이
> 1. 점프 횟수가 있는 경우와 없는 경우를 구분해서 `BFS`를 수행한다.
> 2. 이동할 때마다 visited 여부를 표시하고, 이동할 때마다 횟수를 추가한다.
> 3. 맨 처음으로 도착한 때의 result를 반환한다.

```python
from collections import deque
import sys
sys.stdin = open('input.txt')

# 방향 벡터 정의 (네 방향 이동 + 말의 이동)
normal_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
horse_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]

def is_valid(nx, ny, h, w):
    return 0 <= nx < h and 0 <= ny < w

# 입력 처리
k = int(input())
w, h = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(h)]

# BFS 초기 설정
locations = deque([(0, 0, k, 0)])  # (x, y, 남은 점프 횟수, 현재 동작 수)
visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
visited[0][0][k] = True

# BFS 탐색
result = -1
while locations:
    x, y, jump, cnt = locations.popleft()

    if x == h - 1 and y == w - 1:
        result = cnt
        break

    # 일반 이동
    for dx, dy in normal_moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, h, w) and chess[nx][ny] == 0 and not visited[nx][ny][jump]:
            visited[nx][ny][jump] = True
            locations.append((nx, ny, jump, cnt + 1))

    # 말의 이동
    if jump > 0:
        for dx, dy in horse_moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, h, w) and chess[nx][ny] == 0 and not visited[nx][ny][jump - 1]:
                visited[nx][ny][jump - 1] = True
                locations.append((nx, ny, jump - 1, cnt + 1))

print(result)

```
#### 🧰 백준 2457 공주님의 정원
> 1. 꽃이 피는 날짜를 기준으로 오름차순 정렬한다.
> 2. 가장 최근 꽃이 지는 일자를 기준으로, 추가 꽃을 심을 대상을 선정한다.
>   - 기존 꽃의 피는 일자와 지는 일자에 최근 꽃이 지는 일자가 있어야 한다.
>   - 그 뒤에 있는 꽃들 중 가장 지는 일자가 긴 것을 고른다.
> 3. 추가 꽃을 고를 때마다 최근 지는 일자를 갱신하고, 갯수를 추가한다.
> 4. 만약, 지는 일자가 11월 30일 이후면 갯수를 반환한다.
> 5. 없다면 0을 반환한다.

```python
import sys
sys.stdin = open('input.txt')

n = int(input())
flower = [list(map(int,input().split())) for i in range(n)]
flower.sort()

i = 0
result = 0
latest_end = (3,1)

while i < n:
    sm,sd,em,ed = flower[i]
    if (sm,sd) <= latest_end < (em,ed):
        max_end = (em,ed)
        while i < n-1:
            nsm,nsd,nem,ned = flower[i+1]
            if latest_end < (nsm,nsd):
                break
            if max_end < (nem,ned):
                max_end = (nem,ned)
            i +=1

        # 찾은 꽃 심기
        result +=1
        latest_end = max_end

        if (11,30) < latest_end:
            exit(print(result))
    i+=1
print(0)

```

#### ⚽ 백준 2473 세 용액
> 1. 세 용액을 `투 포인터` 기법을 통해 선정하기 위해 아래와 같이 정한다.
>   - i번째를 순회하며, i+1이 시작점, n-1이 끝점으로 탐색
>   - 용액을 오름차순으로 정렬한다.
> 2. 각 포인터가 위치한 곳의 용액의 절대값 합을 비교해서 기존보다 작으면 갱신한다.
> 3. 세 용액의 합이 0보다 크면 오른쪽 포인터 -1을 , 0보다 작으면 왼쪽 포인터 +1을 한다.

```python
import sys
sys.stdin = open('input.txt')

n = int(input())
sol = sorted(map(int,input().split()))
result =[3*int(1e9)] + [int(1e9)] * 3

for k in range(n):
    i = k+1; j = n-1
    while i < j:
        total = sol[i] + sol[j] + sol[k]
        if abs(total) < result[0]: result = [abs(total),sol[k],sol[i],sol[j]]
        if total < 0:i += 1
        elif total > 0:j -= 1
        else: break
print(*result[1:])

```

#### 🖌 백준 17299 오등큰수
> 오등큰수 : 오른쪽에 해당 배열에서 갯수가 본인보다 큰수
> 1. 그를 위해 `Counter`를 써서 각 원소의 갯수를 저장한다.
> 2. 스택의 마지막원소와 비교해서 오등큰수를 발견하면 스택을 하나씩 pop하면서 오등큰수의 대상에 되는 원소들을 전부 갱신한다.

```python
from collections import Counter
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))
num_cnt = Counter(arr)
result = [-1] * N
stack = [0]

for i in range(N):
    while stack and num_cnt[arr[stack[-1]]] < num_cnt[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)
``` 

#### 🎙 프로그래머스 42895 N으로 표현
> 1. dp의 각 행에는 N 최소 몇개를 썻는지를, 그 행에 쓴 수만큼 나올 수 있는 수를 값으로 저장한다.
> 2. 그러기 위해서 dp에서 각 원소를 빼서 연산을 한다. (ex i = i-j + j이므로, i보다 작은 j를 반복하여 dp를 갱신한다.)
> 3. dp의 해당 행에 number가 존재하면 number를 반환하고, 없으면 -1을 반환한다.

```python
# 42895 N으로 표현
def solution(N, number):
    # 1번 사용 가능 시
    if N == number: return 1

    DP = [set() for _ in range(8)]

    for i in range(8):
        DP[i].add(int(str(N) * (i + 1)))

    # N을 2번부터 8번까지 사용해서 만들 수 있는 숫자 계산
    for i in range(1, 8):
        for j in range(i):
            
            # DP[j]와 DP[i-j-1]의 모든 조합을 통해 숫자 생성
            for op1 in DP[j]:
                for op2 in DP[i-j-1]:
                    DP[i].add(op1 + op2)  # 덧셈
                    DP[i].add(op1 - op2)  # 뺄셈
                    DP[i].add(op1 * op2)  # 곱셈
                    if op2 != 0: DP[i].add(op1 // op2)  # 나눗셈

        # number를 만들 수 있는지 확인
        if number in DP[i]: return i + 1
    return -1

```

#### 👔 프로그래머스 49993 스킬트리
> 1. `skill_tree`에서 하나의 스킬씩 다 탐색을 한다.
> 2. skill을 리스트화하여 별도의 변수를 두고, skill에 있는 원소가 나오면 그게 순차적으로 나온건지 체크를 한다.
> 3. 순차적이지 않으면 break를 하고, `for-else` 구문에 따라 break 안되었으면 스킬트리에 따라 익힌것이므로 결과값에 1 추가한다.

```python
def solution(skill, skill_trees):
    answer = 0
    # skill은 무조건 처음부터 나와야 한다.
    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill and s != skill_list.pop(0):
                 break
        else:
            answer+=1
    return answer
```

#### ❤️‍🔥 프로그래머스 92341 주차요금 계산
> 1. `cars` : 차번호별로 입차시각과 출차시각, 차가없으면 -1을 저장한다. 
> 2. `car_fees` : 차번호별로 누적된 요금을 저장한다.
> 3. 위 사항처럼 저장하되, 출차기록이 없는 경우는 23시 59분 기준으로 요금을 계산한다.
> 4. 차량을 번호순으로 정렬하여 요금결과를 반환한다.

```py
from collections import defaultdict
import math

def solution(fees, records):
    cars = defaultdict(int)
    car_fees = defaultdict(int)

    for record in records:
        time, car_num, inout = record.split()
        hour, minutes = map(int, time.split(':'))
        time_in_minutes = hour * 60 + minutes

        if inout == "IN":
            cars[car_num] = time_in_minutes
        elif inout == "OUT":
            cultime = time_in_minutes - cars[car_num]
            car_fees[car_num] += cultime
            cars[car_num] = -1  # 차가 주차장 밖에 있는 상태 표시

    # "IN" 기록만 있고 "OUT" 기록이 없는 경우를 처리
    for car_num, in_time in cars.items():
        if in_time != -1:
            cultime = 1439 - in_time
            car_fees[car_num] += cultime

    # 요금 계산
    final_fees = {}
    for car_num, total_time in car_fees.items():
        if total_time <= fees[0]:
            final_fees[car_num] = fees[1]
        else:
            final_fees[car_num] = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]

    # 차량 번호순으로 정렬하여 결과 반환
    return [fee for car_num, fee in sorted(final_fees.items())]


```
