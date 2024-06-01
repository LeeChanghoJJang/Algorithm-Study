## Algorithm Study 16회차 회의 (24.6.1.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 6월 1일 일요일 오후 7시  
        - 방식 : 김해 커피팀버

    나. 차주 예정 일정
        - 시간 : 6월 9일 일요일 오전 9시  
        - 방식 : 디스코드

    다. 변경사항
        1. 6월 16일부터 회의 일정 기본값은 토요일 오전 9시(협의 후 변동될 수 있음)
        2. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        3. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 이상현 - 이창호 - 임경태 - 최지우 - 박동현 - 윤예리 - 이권민 (순서는 매번 랜덤으로 변경 예정) 
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
    - 프로그래머스 214289 에어컨(2023 현대모비스 알고리즘 경진대회 예선, Lv.3) 
   ###### 2. 예리
    - 백준 1052 물병(골드 5) 
   ###### 3. 경태
    - 프로그래머스 150369 택배 배달과 수거하기 (2023 KAKAO BLIND RECRUITMENT, Lv.2)
   ###### 4. 동현
    - 백준 17392 우울한 방학(실버 1)
   ###### 5. 상현
    - 프로그래머스 42888 오픈채팅방 (Lv.2)
   ###### 6. 지우
    - 백준 2529 부등호 (실버 1)
   ###### 7. 권민
    - 프로그래머스 72411 메뉴 리뉴얼 (2021 KAKAO BLIND RECRUITMENT,Lv.2)

### 🤢 문제 선정
   ###### 1. 창호
    - 프로그래머스 92343 양과 늑대(2022 KAKAO BLIND RECRUITMENT, Lv.3) 
   ###### 2. 예리
    - 백준 1079 마피아(골드 2) 
   ###### 3. 경태
    - 없음
   ###### 4. 동현
    - 백준 2812 크게 만들기(골드 3)
   ###### 5. 상현
    - 없음
   ###### 6. 지우
    - 프로그래머스 92345 - 사라지는 발판 (Lv.3, 2022 KAKAO BLIND RECRUITMENT)
   ###### 7. 권민
    - 없음

### 🏅 스터디 내용 
#### 🎈 백준 1052 물병
> 이진수를 이용한 `비트마스킹` 기법 활용
> 이진수에서 1의 갯수 : 다합쳤을 때, 물병의 갯수를 의미 
> 그래서 최소한으로 물병을 사서 남는 물병이 없도록 하려면, 1개씩 물병을 더 사면서 최초로 1의 갯수가 K개 미만인 경우를 찾을 수 밖에 없음
> 하지만, 0에서 1이되면 오히려 물병의 갯수가 늘어나는 꼬라지가 됨. 따라서 오른쪽부터 1인 경우에만 순회하여 N을 증가시키고, 물병의 갯수를 세어줌 
```python
N, K = map(int, input().split())
ans = 0

# 이진수에서 1의 개수 찾기
while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    ans += 2**idx
    N += 2**idx  
print(ans)
```
#### 🧰 백준 2529 부등호
> 1. `백트래킹`을 통해 문제 해결
> 2. 0~9까지 한번씩만 사용하고, 매번 result의 결과를 비교하여 작은 경우와 큰 경우 나눔

```python
import sys
sys.stdin  = open('input.txt')

def back(k,result,j):
    global min_str,max_str
    if j==k or len(result) == k+1:
        if min_str > result:
            min_str = result
        if max_str < result:
            max_str = result
        return

    for i in range(10):
        if not visited[i] and (not result or result and eval(f'{result[-1]} {equals[j]} {i}')):
            visited[i] = 1
            if result:
                back(k, result + str(i), j + 1)
            else:
                back(k, result + str(i), j)
            visited[i] = 0

k = int(input())
equals = input().split()
min_str = '9999999999'
max_str = ''
visited = [0] * 10
back(k,'',0)
print(max_str)
print(min_str)
```

#### ⚽ 백준 17392 우울한 방학 
> `그리디` 알고리즘 활용 
> 1. 최대한 균등하게 우울증을 분포시킨다.(각 수의 제곱의 합은 모든 수가 동일할 때 최저가 됨)
> 2. 총 우울한 일수를 구해서 N보다 크다면 0을 반환한다.(우울할 기미가 없음)
> 3. 그 외 각 dp에 우울값을 구할 수있게 일수에 따른 제곱값을 저장한다.
> 4. 우울할 수 있는 총 일수를 구하고, 이를 N+1만큼 균등배분한다.(1에 따라)
> 5. 그리고 result에 각 균등배분 몫을 저장해주고, 나머지를 앞에서부터 차례대로 1씩 더해준다.
> 6. 3에서 구한 dp의 누적 우울함을 구해서 더해준다.
```python
import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
depress = list(map(int,input().split()))

if sum(depress) >= M:
    exit(print(0))
dp = [0] * 1001
for i in range(1,1001):
    dp[i] =dp[i-1] + i**2

leaves = M - sum(depress) - N
quotient = leaves // (N+1)
remainder = leaves % (N+1)
result = [quotient] * (N+1)
for i in range(remainder):
    result[i]+=1

print(sum(map(lambda x:dp[x],result)))


```
#### 🖌 프로그래머스 42888 오픈채팅방 (2018 KAKAO BLIND RECRUITMENT)
> 1. 우선 오픈채팅방에서 고유값인 id에 따라 닉네임을 저장하는 uid_dict를 설정한다.
> 2. record를 순회하여, Enter와 Change의 경우에만 저장되는 닉네임을 바꿔준다.
> 3. 다시 한번 순회하여, Enter일 때는 들어왔다는, Leave일 때는 나갔다는 문구를 특정 리스트에 저장한다.
```python
def solution(record):
    answer = []
    uid_dict = {}

    for rec in record:
        temp = rec.split()

        if temp[0] == 'Leave':
            continue

        uid_dict[temp[1]] = temp[2]

    for rec in record:
        temp = rec.split()

        if temp[0] == 'Enter':
            answer.append(f'{uid_dict[temp[1]]}님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(f'{uid_dict[temp[1]]}님이 나갔습니다.')

    return answer
``` 

#### 🎙 프로그래머스 72411 메뉴리뉴얼
> 1. course에서 각 요리의 조합을 order_dict에 저장한다.
> 2. 그리고 조합의 갯수의 최대치를 max_len에 저장한다.
> 3. 그 조합의 갯수가 2이상인 것들만 오름차순으로 result에 저장한다.
> 4. 거기서 각 조합의 갯수가 max_len에 저장된 갯수와 일치한것만 별도의 리스트에 저장하여 출력한다.

```python
from itertools import combinations

def solution(orders, course):
    order_dict = {}
    max_len = {i: 0 for i in course}
    for length in course:
        for cook in orders:
            for a in combinations(cook, length):
                b = ''.join(sorted(a))
                if b not in order_dict:
                    order_dict[b] = 1
                else:
                    order_dict[b] += 1
                    lens = len(b)
                    if max_len[lens] < order_dict[b]:
                        max_len[lens] = order_dict[b]

    result = sorted(filter(lambda x: order_dict[x] >= 2, order_dict.keys()))

    total_result = []
    for i in result:
        if max_len[len(i)] == order_dict[i]:
            total_result.append(i)
    return total_result
```

#### 👔 프로그래머스 150369 택배 배달과 수거하기
> 1. `그리디`에 따라 같은 거리를 이동할 때, 최대한 먼거리에 있는 곳에 택배를 배달하고 수령하여 이동거리를 단축시키는 것이 핵심
> 2. 맨 뒤에서부터 반복문을 실행하여 한번에 배달과 수거할 물건들만큼 갯수를 빼준 후, 왕복횟수를 더해준다.

```python
def solution(cap, n, deliveries, pickups):
    answer = 0
    deli_item = 0
    pick_item = 0

    # 가장 먼 곳부터 탐색
    for i in range(n-1, -1, -1):
        # 현재 위치에서 배달과 수거할 물건의 수를 추가
        deli_item += deliveries[i]
        pick_item += pickups[i]

        # 배달 또는 수거할 물건이 남아있는 동안 반복
        while deli_item > 0 or pick_item > 0:
            # 각 위치의 배달과 수거 값에서 cap값 감산
            deli_item -= cap
            pick_item -= cap
            # 왕복 횟수 합산
            answer += (i+1)*2

    return answer
```

#### ❤️‍🔥 프로그래머스 214289 에어컨
> 1. `배낭` 문제 활용. onboard에 따라 최소 소비전력의 누적치를 dp에 저장한다.
> 2. 이전의 실내온도와 실외온도(희망온도)가 2이상 차이날 경우 소비전력이 a만큼, 같을 경우에는 b만큼 들거나, 에어컨을 끄는 경우 중 가장 적은 소비전력을 저장한다. 
```py
def solution(temperature, t1, t2, a, b, onboard):
    # 인덱스를 맞추기 위해 온도를 10씩 더해준다
    temperature, t1, t2 = temperature + 10, t1 + 10, t2 + 10
    # 시간을 행으로, 온도를 열로, 값은 누적된 소비전력을 넣는다.
    dp = [[float("inf")] * 53 for _ in range(len(onboard))]
    # 시간이 0일 때는 온도가 어떻든 소비전력이 0으로 시작
    dp[0][temperature] = 0
    # 신경써야할 온도의 최소값과 최대값을 설정합니다.
    min_t, max_t = min(temperature, t1), max(temperature, t2)
    for i in range(1, len(onboard)):
        # 손님이 있으면 지정된 최소온도와 최대온도를 신경쓰고,
        # 없을 때에는 실외온도와 비교해서 작거나 큰걸로 결정해도 무관함
        start, end = [t1, t2] if onboard[i] else [min_t, max_t]

        for j in range(start, end + 1):
            # 이전 시간 간격에서 현재 온도로 변하는 비용을 계산
            # 실외온도와 실내온도가 같으면 b, 다르면 a만큼 소비전력 소모
            l = dp[i - 1][j - 1] if j-1 < temperature else dp[i - 1][j - 1] + a
            m = dp[i - 1][j] if j == temperature else dp[i - 1][j] + b
            h = dp[i - 1][j + 1] if j+1 > temperature else dp[i - 1][j + 1] + a
            # 위 3개 중에 가장 누적소비전력이 작은것을 dp배열에 저장
            dp[i][j] = min(l, m, h)
    return min(dp[-1])

print(solution(28,18,26,10,8,[0, 0, 1, 1, 1, 1, 1]))
```
