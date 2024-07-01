## Algorithm Study 19회차 회의 (24.6.22.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 6월 22일 토요일 오후 7시  
        - 방식 : 디스코드

    나. 차주 예정 일정
        - 시간 : 6월 29일 토요일 오후 7시  
        - 방식 : 김해 커피팀버

    다. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 박동현 - 임경태 - 이상현 - 최지우 - 이창호 - 이권민 - 윤예리  (순서는 매번 랜덤으로 변경 예정) 
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
    - 백준 2482 색상환 (골3)

### 🤢 문제 선정
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

### 🏅 스터디 내용 
#### 🎈 백준 2482 색상환
> 1. 총 주어진 색의 수 N개 중 K개를 선택할 수 있는 경우의 수를 구하는 것. 단, 인접한 색은 구할 수 없기에 DP를 통해 해결.
> 2. 0개나 1개를 선택하는 경우는 고정되있으므로 먼저 반복문을 돌려준다.
> 3. 점화식은 간단하다. N개가 주어졌을 때, N-1개까지 K개를 선택하는 경우와 N-2개에서 K-1개(N번째 선택)하는 경우를 합한 것과 같음
```python
# 2482 색상환
N = int(input())
K = int(input())

# 색 분배 불가능한 경우
if K > N//2: exit(print(0))

# dp[i][j] : i개의 색 중에서 j개를 선택
DP = [[0] * (K+1) for _ in range(N+1)]

# n개의 색 중에서 1개를 선택하는 경우의 수는 n개
for i in range(N+1): DP[i][1] = i

# DP 실행
for i in range(2, N+1):
    for j in range(2, K+1):
        DP[i][j] += DP[i-1][j]
        DP[i][j] += DP[i-2][j-1] if i != N else DP[i-3][j-1]
        DP[i][j] %= 1000000003

print(DP[N][K])
```
#### 🧰 백준 2629 양팔저울
> 1. set을 이용하는 방법
> 2. 0부터 시작하여 추의 무게를 더하거나 빼주는 것을 set에 지속적 업데이트 한다.
> 3. 해당되는 구슬의 무게가 set에 있는지 확인한다. 

```python
_, weight_N = int(input()), list(map(int, input().split()))
_, weight_M = int(input()), list(map(int, input().split()))

DP = {0}

for w in weight_N:
    tmp = set()
    for i in DP:
        tmp.add(i + w)
        tmp.add(abs(i - w))
    DP |= tmp

print(*['Y' if w in DP else 'N' for w in weight_M])

```
> 1. DP + 재귀를 이용하는 방법
> 2. 0부터 시작하여 추의 무게를 더하거나 빼주는 것을 set에 지속적 업데이트 한다.

```python
import sys
sys.stdin = open('input.txt')

cnt, chu_weight = int(input()),list(map(int,input().split()))
marble_cnt, marble_weight = int(input()), list(map(int,input().split()))

# 추의 무게는 최대 500이므로 [[추의 개수*500]*추의 개수]로 배열을 구성한다.
dp, r = [[0 for j in range((i + 1) * 500 + 1)] for i in range(cnt + 1)], []
# 추의 무게를 더한다.
# 추의 무게를 뺀다.
# 추를 사용하지 않는다.

def cal(num, weight):
    if num > cnt:
        return

    if dp[num][weight]:
        return

    dp[num][weight] = 1

    cal(num + 1, weight)
    cal(num + 1, weight + chu_weight[num - 1])
    cal(num + 1, abs(weight - chu_weight[num - 1]))


cal(0, 0)

for i in marble_weight:
    if i > 30 * 500:
        r.append("N")
    elif dp[cnt][i] == 1:
        r.append("Y")
    else:
        r.append("N")
print(*r)

```
#### ⚽ 백준 3109 빵집
> 1. 왼쪽에서 오른쪽으로 장애물을 피해서 이동할 수 있는 최대 횟수 구하기
> 2. 지나간 곳은 방문처리를 해주고, 경로의 횟수를 누적해서 돌아줘야 한다. 나같은 경우는 `백트래킹` 이용

```python
import sys
sys.stdin = open('input.txt')


def dfs(row, col):
    global cnt
    if col == C - 1:
        cnt = True
        return True

    if row < 0 or row >= R or col < 0 or col >= C or pipeline[row][col] == 'x':
        return False

    pipeline[row][col] = 'x'  # 방문 처리

    for next in [-1, 0, 1]:
        if dfs(row + next, col + 1):
            return True

    # 방문 처리 원상 복구할 필요 없음
    return False


R, C = map(int, input().split())
pipeline = [list(input().strip()) for _ in range(R)]
result = 0
for i in range(R):
    cnt = False
    if dfs(i, 0):
        result += 1
print(result)

```

#### 🖌 백준 3687 성냥개비
> 1. 주어진 성냥개비 갯수에서 `최소 숫자`와 `최대 숫자` 구하기
> 2. 최대 숫자는 성냥개비 갯수가 짝수면 전부 1로, 홀수면 7하나 나머지 1로 나타내면 된다.
> 3. 최소 숫자는 DP를 구성하고, 2개부터 8개까지 1,7,4,2,6,8,10 순으로 나타내어 진다. 여기서 반복문을 돌면서 DP에 누적해서 최솟값을 더해주면 된다.

```python
# 3687 성냥개비
DP = [float('inf')] * 101
DP[2:9] = ["1", "7", "4", "2", "6", "8", "10"]

# 최소 숫자 찾기
for i in range(9, 101):
    for j in range(2, i-1):
        DP[i] = min(DP[i], int(str(DP[j]) + str(DP[i-j])))
        if j == 6:
            DP[i] = min(DP[i], int(str(DP[i-j]) + '0'))

# 최대 숫자 찾기
def find_max(N):
    return "7" + "1" * (N//2-1) if N & 1 else "1" * (N//2)

for _ in range(int(input())):
    N = int(input())
    print(DP[N], find_max(N))
``` 

#### 🎙 프로그래머스 67258 보석 쇼핑
> 1. `투포인터`를 써서 모든 보석을 담는 최소 사이즈를 재야 한다.
> 2. 포인터가 gems의 길이 안에 있을 동안 아래와 같이 반복한다.
>   - gem_dict와 gem_cnt가 같으면 현재 구간이 이전 구간보다 짧으면 결과를 갱신. 보석 카운트가 다 되면 딕셔너리에서 제거
>   - gem_dict와 gem_cnt가 다르면 end point를 증가시키고, 보석을 포함시킨다 gem_dict에

```python
# 보석 쇼핑
def solution(gems):
    gem_dict = {gems[0]: 1}
    gem_cnt = len(set(gems))
    answer = [1, len(gems)+1]
    start = end = 0

    while end < len(gems):
        if len(gem_dict) == gem_cnt:
            # 현재 구간이 이전 구간보다 짧다면 결과 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start+1, end+1]
            # 카운트 감소
            gem_dict[gems[start]] -= 1
            # 보석의 카운트가 0이 되면 딕셔너리에서 제거
            if not gem_dict[gems[start]]:
                del gem_dict[gems[start]]
            start += 1
        else:
            end += 1
            # 카운트 증가
            if end < len(gems):
                gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1

    return answer


```

#### 👔 프로그래머스 92342 양궁대회
> 1. `combinations_with_replacement` 라이브러리를 이용하여 중복해서 n번의 화살을 쏜다.
> 2. 라이언이 쏜 화살의 갯수를 info_peach에 카운트 해준다.
> 3. 그래서 각 횟수를 비교하여 점수를 계산한다.
> 4. 라이언이 이겼으면 그 기록을 저장한다.

```python
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_ = -1

    for comb in combinations_with_replacement(range(11), n):
        info_peach = [0] * 11
        lion = peach = 0
        
        for score in comb:
            info_peach[10 - score] += 1
            
        for score in range(11):
            if info[score] == info_peach[score] == 0:
                continue
            if info[score] >= info_peach[score]:
                peach += 10 - score
            else:
                lion += 10 - score
                
        if lion <= peach:
            continue
        
        if lion - peach > max_:
            max_ = lion - peach
            answer = info_peach

    return answer
```

#### ❤️‍🔥 프로그래머스 160585 혼자서 하는 틱택토
> 1. x가 o보다 많거나 2개 이상 차이나면 잘못된거다.
> 2. x가 이겼는데, 갯수가 같지 않거나 o가 이겼는데 갯수가 1개 차이가 안나면 잘못된거다.
> 3. 그 외에는 잘된거로 반환한다.

```py
def chk(player, board):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x > num_o or abs(num_x - num_o) > 1:
        return 0

    x_wins = chk('X', board)
    o_wins = chk('O', board)

    if (x_wins and num_x != num_o) or (o_wins and num_x != num_o - 1):
        return 0

    return 1

```
