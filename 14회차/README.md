## Algorithm Study 14회차 회의 (24.5.5.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 5월 5일 일요일 저녁 7시  
        - 방식 : 디스코드

    나. 차주 예정 일정
        - 시간 : 5월 12일 일요일 오전 9시  
        - 방식 : 송정삼정오피스텔 2층 휴게실

    다. 변경사항
        1. 회의 일정 기본값은 일요일 오전 9시(협의 후 변동될 수 있음)
        2. 최소한의 공동목표인 "코테합격"을 기원하기 위해 문제 수는 늘리고 난이도는 낮추어 최대한 다양한 문제 선정
            - 이번 주는 각자 한 문제며, 본인이 선정한 문제는 라이브로 코딩할 것이니, 신중히 선정 필요
            - 프로그래머스 환경에서도 많이 치는 것을 감안하여 백준 외에 사이트도 참고하여 선정 
        3. 어려운 문제를 한 명씩 선정.
            - 순서 : 이번주 박동현 (이상현 - 이창호 - 임경태 - 최지우 - 박동현 - 윤예리 - 이권민) -> 첫 차례는 예리 건너뛴다.
        4. 장소 선정 : 스터디원이 증대되어 장소를 송삼, 김해 중 하나로 결정(1번씩 로테이션)
        5. 어려운 문제 기준
            - 백준 : 골드 3 이상
            - 프로그래머스 : Lv.3 이상
            - SWEA : D5 또는 A형 역량테스트 
            - 소프티어 : Lv.3 이상
        
### 🎵 문제 선정 및 방식 
    가. 유형 : 코딩테스트 기출 위주로 각자 리뷰할 문제 선정 
    나. 문제수 : 인당 1문제, 총 7문제
    다. 난이도 
        - 백준 플래티넘 이하
        - 프로그래머스 Lv.4 이하
        - SWEA D6 이하    
    라. 코드 브리핑 && 리뷰 방식
      - 이번 주의 어려운 문제 : 철로
      - 문제 선정자가 라이브 코딩하면서 솔루션 리뷰
      - 푼 방식 이외에도 다양한 방법 제시

### 🎁 이번회차 풀이 문제
   ###### 1. 창호
    - 프로그래머스 신고 결과 받기 (2022 KAKAO BLIND RECRUITMENT, Lv.1)
    - 프로그래머스 개인정보 수집 유효기간 (2023 KAKAO BLIND RECRUITMENT, Lv.1)
   ###### 2. 예리
    - 프로그래머스 같은 숫자는 싫어 (Lv.1)
    - 프로그래머스 성격 유형 검사하기(2022 KAKAO TECH INTERNSHIP, Lv.1)
   ###### 3. 경태
    - 프로그래머스 두 큐 합 같게 만들기(2022 KAKAO TECH INTERNSHIP, Lv.2)
    - 프로그래머스 키패드 누르기(2020 카카오 인턴십, Lv.1)
   ###### 4. 동현
    - 프로그래머스 [1차] 캐시 (2018 KAKAO BLIND RECRUITMENT, Lv.2)
    - 백준 12100 2048(Easy)(골드 2) - 시뮬레이션 
   ###### 5. 상현
    - 프로그래머스 가장 많이 받은 선물 (2024 KAKAO WINTER INTERNSHIP, Lv.1)
    - 프로그래머스 숫자 문자열과 영단어 (2021 카카오 채용연계형 인턴십, Lv.1)
   ###### 6. 지우
    - 프로그래머스 크레인 인형뽑기 게임(2019 카카오 개발자 겨울 인턴십, Lv.1)
    - 백준 13334 철로(골드 2) - 우선순위 큐
   ###### 7. 권민
    - 백준 17471 게리맨더링(골드 3) - 조합론, DFS, BFS
    - 백준 17135 캐슬디펜스(골드 3) - 시뮬레이션, BFS, DFS

### 🤢 문제 선정
   ###### 1. 창호
    - 프로그래머스 258707 n+1 카드게임(2024 KAKAO WINTER INTERNSHIP, Lv.3) 
   ###### 2. 예리
    - 백준 2146 다리만들기(골드 3) 
   ###### 3. 경태
   ###### 4. 동현
   ###### 5. 상현
   ###### 6. 지우
   ###### 7. 권민

### 🏅 스터디 내용 
#### 🎈 백준 12100 2048(easy)
> `백트래킹` 을 활용하여 `시뮬레이션` 구현
> 1. rotate : 2차원 리스트를 시계 방향으로 90도 회전시키는 함수
> 2. merge : 리스트를 왼쪽으로 이동시키고, 병합하는 함수. 0이 아닌 숫자들에 한해 같은 숫자가 있다면 합치기
> 3. dfs를 수행하여 깊이를 줄여 0면 현재 최대값 반환

```python
from copy import deepcopy

# 2차원 리스트를 시계 방향으로 90도 회전시키는 함수
def rotate(list_, size):
    new_list = deepcopy(list_)
    for row in range(size):
        for col in range(size):
            new_list[size - col - 1][row] = list_[row][col]
    return new_list

# 리스트를 왼쪽으로 이동시키고 병합하는 함수
def merge(list_):
    # 0이 아닌 숫자만 필터링
    temp = [i for i in list_ if i]

    for i in range(1, len(temp)):
        # 연속된 같은 숫자가 있다면 합치기
        if temp[i] == temp[i - 1]:
            temp[i - 1] *= 2
            temp[i] = 0
    # 0이 아닌 숫자만 남기고 나머지는 0으로 채움
    temp = [i for i in temp if i]
    return temp + [0] * (len(list_) - len(temp))

# 깊이 우선 탐색으로 최대 점수를 계산하는 함수
def dfs(list_, size, depth):
    # 현재 보드에서 가장 큰 값 찾기
    max_ = max([max(row) for row in list_])
    # 깊이가 0이면 현재 최대 값 반환
    if depth == 5:
        return max_

    # 네 방향으로 보드를 회전하면서 각각의 경우 계산
    for _ in range(4):
        new_list = [merge(row) for row in list_]
        # 현재 보드와 회전 후 보드가 다르다면 계속 탐색
        if new_list != list_:
            max_ = max(max_, dfs(new_list, size, depth + 1))
        # 보드를 시계 방향으로 90도 회전
        list_ = rotate(list_, size)
    return max_

# 입력 받기
N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]

# 깊이 우선 탐색 호출하여 결과 출력
print(dfs(list_, N, 0))
```

#### 🧰 백준 13334 철로
> `우선순위 큐` 및 `슬라이딩 윈도우` 방식을 이용하여 최대 카운트 세기
> 1. 각 철로를 종착점을 기준으로 정렬
> 2. 건물의 왼쪽 끝점을 기준으로 힙에 넣고 빼고를 반복
```python
# 13334 철로
import heapq

N = int(input())
bulidings = sorted([sorted(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
D = int(input())
Q = []; ans = 0

# 끝점을 기준으로 정렬된 건물들 순회
for building in bulidings:
    # 건물의 끝점을 기준으로 철로 설정
    left, right = building
    heapq.heappush(Q, left)

    # 시작점이 철로 범위 밖에 있는 경우 제거
    while Q and Q[0] < right - D:
        heapq.heappop(Q)
    
    # 시작점이 철로 범위 안에 있는 경우 카운트
    ans = max(ans, len(Q))

print(ans)
```


#### ⚽ 백준 17135 캐슬 디펜스
> `시뮬레이션` + `BFS` 활용 문제
> 1. 모든 열 중에 3개의 열을 선택하여 궁수를 배치한다(`combinations`)
> 2. vistied : 모든 배열에 방문 위치를 둔다. 
> 3. queue에 현재 궁수위치와 사정거리를 담는다.
> 4. 궁수의 사정거리 내에 있으면 죽이고 다음 턴으로 넘어간다. 
> 5. 단, 동시에 죽이고 다음턴으로 넘어가야 한다. 
```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
per_n = sorted(list(map(int, input().split())))
per_m = sorted(list(map(int, input().split())))

# 만약 n이 많으면 남녀를 바꿔준다.
# 여자가 많다고 가정하고 풀어줄 예정이라
if n > m:
    n, m = m, n
    per_n, per_m = per_m, per_n

dp = [[0] * m for _ in range(n)]    # 2차원 dp로 풀 예정
# dp[남자][여자] = 남자가 여자를 선택했을 때 셩격 차 합의 최소값
dp[0][0] = abs(per_n[0] - per_m[0])
for i in range(1, m-(n-1)):
    dp[0][i] = min(abs(per_n[0]-per_m[i]), dp[0][i-1])

for i in range(1, n):
    for j in range(i, m-(n-i-1)):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(per_n[i]-per_m[j])
        else:
            dp[i][j] = min(dp[i-1][j-1] + abs(per_n[i]-per_m[j]), dp[i][j-1])
print(dp[n-1][m-1])
```

#### 🖌 백준 17471 게리멘더링
> `BFS`를 활용하여 최솟값, 최댓값 선정
> 1. 두 구역으로 나누어(조합 사용) BFS를 사용(각 sum을 도출) 
> 2. 두 구역의 길이의 합이 N으로 같을 경우에만 최솟값을 저장한다. 
```python
# 17471 게리맨더링
from collections import deque
from itertools import combinations

# 선거구 체크
def BFS(area):
    s = area[0]
    sumPop = population[s]
    Q = deque([s])
    visit = {s,}

    while Q:
        now = Q.popleft()

        for next in graph[now]:
            if next in area and next not in visit:
                sumPop += population[next]
                Q.append(next)
                visit.add(next)

    return sumPop, len(visit)

N = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(N)]
ans = 10000

# 그래프 제작
for i in range(N):
    _, *info = list(map(int, input().split()))
    graph[i] = list(map(lambda x: x-1, info))

# 조합 만들어 BFS 실행
for i in range(1, N//2+1):
    for area in combinations(range(N), i):
        sumA, lenA = BFS(area)
        sumB, lenB = BFS([i for i in range(N) if i not in area])

        if lenA + lenB == N:
            ans = min(ans, abs(sumA - sumB))

print(ans if ans != 10000 else -1)

``` 

#### 🎙 프로그래머스 12906 같은 숫자는 싫어
> 반복문 사용하여 연속되지 않는 숫자는 제외

```python
def solution(arr):
    numbers = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            numbers.append(arr[i])
    return numbers
```

#### 👔 프로그래머스 17680 캐시
> 단순 반복문 + 조건문
> 1. result 리스트에 기존 city가 있으면 갱신(1초 추가)
> 2. 없다면 추가 (5초 증가)
> 3. 최종적인 시간 도출

```python
from collections import deque
def solution(cacheSize, cities):
    result = []
    time= 0
    # 도시를 순회
    for city in cities:
        # 대문자 소문자 구분 없어 한가지로 통일
        city = city.lower()
        # 기존에 city가 없으면 city를 추가
        if city not in result:
            result.append(city)
            # 다만.. 캐시사이즈가 초과한다면 맨 첨에 들어간거는 빼고
            if len(result) > cacheSize:
                result.pop(0)
            # 새거가 들어가면 무조건 5초 증가
            time+=5
        # 기존에 city가 있다면?
        else:
            # 기존꺼를 갱신하기 위해 제거하고, 새거 추가
            result.remove(city)
            result.append(city)
            # 기존것이 있으면 1초 추가
            time+=1
    return time
```

#### ❤️‍🔥 프로그래머스 64061 크레인 인형뽑기 게임 
> 1. 인형뽑기에서 남아있는 것이 없을때까지 stack에 추가
> 2. stack에 두 인형이 연속된다면 둘다 빼주고 결과값에 2추가
```py
def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break

    return answer
```
#### 💕 프로그래머스 67256 키패드 누르기 
> 1. 두 키패드 간의 거리를 구하는 `distance` 함수 도출 
> 2. 키패드가 147이면 왼손, 369면 오른손, 2580이면 거리를 도출하여 각 손으로부터 거리가 작은 곳을 선택
```py
def solution(numbers, hand):
    result =''
    # 두 키보드 위치간에 가까운 거리의 키패드를 반환하는 함수
    def distance(left,right,keypad,hand):
        # 각 거리 재기
        result_l = abs(keypad[1] - left[1]) + abs(keypad[0] - left[0])
        result_r = abs(keypad[1] - right[1]) + abs(keypad[0] - right[0])
        if result_l > result_r:
            return 'R'
        elif result_l < result_r:
            return 'L'
        else:
            if hand =='right':
                return 'R'
            else:
                return 'L'
    # 첫 스타트 지점
    now_l = (3,0)
    now_r = (3,2)
    # 숫자들에서 키패드 숫자를 뺀다.
    for keypad in numbers:
        # 키패드에 따른 좌표 설정
        if keypad ==0:
            location = (3,1)
        else:
            location = ((keypad-1)//3,(keypad-1)%3)
        # 키패드가 어떤 숫자임에 따라 결과값 지정
        if keypad in [1,4,7]:
            result+='L'
            now_l = ((keypad-1)//3,0)
        elif keypad in [3,6,9]:
            result+='R'
            now_r = ((keypad-1)//3,2)
        # 같을 경우 현재 각 손으로부터 거리를 쟤고 가까운쪽 선택
        else:
            temp = distance(now_l,now_r,location,hand)
            result += temp
            if temp=='L':
                now_l = location
            elif temp=='R':
                now_r = location
    return result
```
#### 💕 프로그래머스 81301 숫자 문자열과 영단어
> 딕션너리와 `replace` 사용
```py
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    # 모든 숫자를 순회하여 변경하면 됨
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
```
#### 🥪 프로그래머스 92334 신고 결과 받기
> 1. 신고 당한자들의 횟수를 기록한다.
> 2. k번 이상 신고 당했으면, 그의 신고자들에게 메일 1회씩 추가 발송한다.
> 3. 처음 주어진 id_list의 순서에 따라 리스트를 반환한다.  
```py
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x:0 for x in id_list}
    # report : 신고자와 신고 당한자 기록
    for r in set(report):
        # 신고자가 불량이용자 신고하면 신고횟수 1추가
        reports[r.split()[1]] +=1

    for r in set(report):
        # k번 이상 신고당했으면
        if reports[r.split()[1]] >= k:
            # 정지횟수 1추가
            answer[id_list.index(r.split()[0])] += 1
    return answer
```

#### 🏫 프로그래머스 118666 성격유형검사하기
> 1. MBTI의 정보를 순차적으로 정리.
> 2. tendency_dict에 각 성향을 저장
> 3. 최종적으로 많은 성향을 가진 리스트를 반환

```py
def solution(survey, choices):
    MBTI = ["TR","CF","MJ","AN"]
    tendency_dict = {i:0 for i in ["A","C","F","M","N","J","R","T"]}
    for i in range(len(survey)):
        left, right = survey[i]
        if choices[i] - 4 > 0:
            tendency_dict[right] += choices[i] - 4
        else:
            tendency_dict[left] += 4 - choices[i]
    result = ''
    for i,j in MBTI:
        if tendency_dict[i] > tendency_dict[j]:
            result += i
        elif tendency_dict[i] < tendency_dict[j]:
            result += j
        else:
            result += min(i,j)
    return result
```

#### 🏫 프로그래머스 118667 두 큐합 같게 만들기
> 1. 두큐를 계속 비교. 매번 sum을 쓰는것이 아니라 기존 sum에서 각 숫자의 합과 차를 계산하여 갱신
> 2. 한 큐에서 다른 큐로 갈 때 횟수 1회 추가
> 3. 두 큐 합이 같은 경우가 나오면 그 때의 count 반환
> 4. 만약 두 큐의 합이 홀수거나, 한 원소가 전체의 반이상이면 -1 반환

```py
from collections import deque
def solution(queue1, queue2):
    # queue1 과 queue2
    queue1 = deque(queue1); queue2 = deque(queue2)
    q1_sum = sum(queue1);q2_sum = sum(queue2)
    n = len(queue1) + len(queue2)
    # 두 큐의 합이 홀수면 -1 반환
    if (q1_sum+ q2_sum) % 2: return -1
    count = 0
    # 반복 횟수가 총 길이의 2배면 중단
    while queue1 and queue2 and count <= n*2:
        if q1_sum < q2_sum:
            now = queue2.popleft()
            queue1.append(now)
            q2_sum-=now;q1_sum+=now
        elif q1_sum > q2_sum:
            now = queue1.popleft()
            queue2.append(now)  
            q2_sum+=now;q1_sum-=now
        # 두 큐의 합이 동일하면 count 반환
        else:
            return count
        if now > (q1_sum + q2_sum) / 2:return -1 
        count+=1
    return -1
```
#### 🏫 프로그래머스 150370 개인정보 수집 유효기간
> 1. 날짜를 계산하여 비교하기 위해 terms의 날짜를 일수로 환산
> 2. privacies의 모든 케이스를 순회하여 보관기한 내에 today가 있는 경우, 리스트의 인덱스를 추가한다.

```py
def solution(today, terms, privacies):
    ans = []
    termsDict = {char[0]: int(char[2:]) * 28 for char in terms}
    nowY, nowM, nowD = map(int, today.split('.'))
    now = nowY * 28 * 12 + nowM * 28 + nowD

    for i in range(len(privacies)):
        pre, case = privacies[i].split()
        preY, preM, preD = map(int, pre.split('.'))
        pre = preY * 28 * 12 + preM * 28 + preD + termsDict[case]

        if pre <= now: ans.append(i+1)

    return ans
```
#### 🏫 프로그래머스 258712 가장 많이 받은 선물
> 1. 선물한 사람, 받은 사람을 바탕으로 선물지수와 관계를 계산한다.
> 2. 중복없이 친구 2명을 순회해서, 두 사람 사이 선물을 누가 더 많이 줬는지 계산한다.
> 3. 기록이 없거나 같다면 선물지수에 따라 친구별로 갯수를 추가한다.
```py
from itertools import combinations
def solution(friends, gifts):
    # gift_index : 선물지수
    gift_index = {i: 0 for i in friends}
    # gift_relation : 각 친구가 각 선물한 친구를 딕셔너리로 구현
    gift_relation = {i: {j:0 for j in friends} for i in friends}
    # 선물한사람, 받은사람, 그 관계를 각각 저장
    for person in gifts:
        gifting, gifted = person.split(' ')
        gift_index[gifting] +=1
        gift_index[gifted] -=1
        gift_relation[gifting][gifted] +=1
    # will : 친구별로 앞으로 선물 받을 수를 저장함
    will = {i:0 for i in friends}
    # 모든 친구 중 두명씩을 중복없이 뽑아, 서로 선물 기록을 비교
    for person1,person2 in combinations(friends,2):
        if gift_relation[person1][person2] > gift_relation[person2][person1]:
            will[person1] +=1
        elif gift_relation[person1][person2] < gift_relation[person2][person1]:
            will[person2] +=1
        else:
            # 만약 기록이 없거나 같다면 선물지수에 따라 판정
            if gift_index[person1] < gift_index[person2]:
                will[person2] +=1
            elif gift_index[person2] < gift_index[person1]:
                will[person1] +=1
    return max(will.values())
```