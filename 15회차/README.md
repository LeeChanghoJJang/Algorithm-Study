## Algorithm Study 14회차 회의 (24.5.12.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 5월 12일 일요일 오후 7시  
        - 방식 : 송정삼정오피스텔 2층 휴게실

    나. 차주 예정 일정
        - 시간 : 6월 1일 일요일 오후 7시  
        - 방식 : 김해 커피팀버

    다. 변경사항
        1. 회의 일정 기본값은 일요일 오전 9시(협의 후 변동될 수 있음)
        2. 최소한의 공동목표인 "코테합격"을 기원하기 위해 문제 수는 늘리고 난이도는 낮추어 최대한 다양한 문제 선정
            - 이번 주는 각자 한 문제며, 본인이 선정한 문제는 라이브로 코딩할 것이니, 신중히 선정 필요
            - 프로그래머스 환경에서도 많이 치는 것을 감안하여 백준 외에 사이트도 참고하여 선정 
        3. 어려운 문제를 한 명씩 선정.
            - 순서 : 이번주 이권민 (이상현 - 이창호 - 임경태 - 최지우 - 박동현 - 윤예리 - 이권민)
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
      - 이번 주의 어려운 문제 : k번째 최단거리
      - 문제 선정자가 라이브 코딩하면서 솔루션 리뷰
      - 푼 방식 이외에도 다양한 방법 제시

### 🎁 이번회차 풀이 문제
   ###### 1. 창호
    - 프로그래머스 258707 n+1 카드게임(2024 KAKAO WINTER INTERNSHIP, Lv.3) 
   ###### 2. 예리
    - 백준 2146 다리만들기(골드 3) 
   ###### 3. 경태
    - 프로그래머스 17681 비밀지도(2018 KAKAO BLIND RECRUITMENT,Lv.1)
   ###### 4. 동현
    - 백준 1854 k번째 최단 경로 찾기(플래티넘 4)
   ###### 5. 상현
    - 프로그래머스 258711 도넛과 막대 그래프(Lv.2)
   ###### 6. 지우
    - 프로그래머스 150368 이모티콘 할인행사(2023 KAKAO BLIND RECRUITMENT Lv.3)
   ###### 7. 권민
    - 백준 7579 앱(골드 3)

### 🤢 문제 선정
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

### 🏅 스터디 내용 
#### 🎈 백준 1854 k번째 최단경로
> `다익스트라` 함수 구현
> 일반적으로 동일하나, k번째 경로의 비용을 비교하여 더 작을 경우 저장하고, sort함
> 마지막에 for문을 돌려 각 요소별 값을 도출

```python
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra():
    heap = []
    heappush(heap, (0, 1))
    dist[1][0] = 0

    while heap:
        now_w, now_node = heappop(heap)
        for nxt_w, nxt_node in link[now_node]:
            new_w = now_w + nxt_w
            if dist[nxt_node][k - 1] <= new_w:
                continue

            dist[nxt_node][k - 1] = new_w
            dist[nxt_node].sort()
            heappush(heap, (new_w, nxt_node))


n, m, k = map(int, input().split())

link = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    link[a].append((c, b))

dist = [[1e9] * k for _ in range(n+1)]
dijkstra()

for i in range(1, n+1):
    if dist[i][k-1] == 1e9:
        print(-1)
    else:
        print(dist[i][k-1])

```
#### 🧰 백준 2146 다리만들기
> 1. `BFS`를 통해 같은 섬을 색칠하여 같은 무리로 지정
> 2. 각 섬의 좌표를 전부 한 곳에 모음.
> 3. 서로 다른 섬끼리 좌표간의 거리를 비교하여 최소 좌표 도출
```python
# 상하좌우 이동을 위한 좌표 변화를 나타내는 리스트입니다.
dr = [(1,0),(0,1),(-1,0),(0,-1)]

# 같은 섬은 색칠하고 같은 무리로 담기 위한 BFS 함수입니다.
def BFS(x, y, num):
    # 해당 지점을 num으로 색칠하고, 해당 무리의 좌표들을 임시 리스트에 저장합니다.
    colors[x][y] = num
    temp = [(x, y)]
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        # 상하좌우로 이동하며 같은 섬을 탐색합니다.
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not colors[nx][ny]:
                colors[nx][ny] = num
                queue.append([nx, ny])
                temp.append((nx, ny))
    return temp

# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 지점의 색상을 나타내는 2차원 리스트입니다.
colors = [[0] * N for _ in range(N)]

# 색깔별로 무리를 나누어 저장하는 딕셔너리입니다.
color_dict = {}
num = 0

# 같은 곳끼리 색칠을 시작합니다.
for i in range(N):
    for j in range(N):
        if arr[i][j] and not colors[i][j]:
            num += 1
            color_dict[num] = BFS(i, j, num)

# 최소 거리를 나타내는 변수를 무한대로 초기화합니다.
min_distance = float('inf')

# 색깔이 다르면 거리를 재기 시작합니다.
for combi in combinations(range(1, num+1), 2):
    a, b = combi
    for i in color_dict[a]:
        i1, i2 = i
        for j in color_dict[b]:
            j1, j2 = j
            # 두 지점 간의 거리를 계산합니다.
            cal_dis = abs(i1 - j1) + abs(i2 - j2) - 1
            # 최소 거리를 업데이트합니다.
            min_distance = min(min_distance,cal_dis)
            # 최소 거리가 1이면 더 이상 계산할 필요 없이 1을 출력하고 종료합니다.
            if min_distance == 1:
                exit(print(1))

print(min_distance)
```

#### ⚽ 백준 7579 앱 
> `배낭`문제를 통해 풂
> 1. 앱의 갯수를 행으로, 비용의 합을 열로 하는 이차원 DP를 구성한다.
> 2. 비용대비 메모리가 좋은 것을 구하기 위해 역순으로 순회.
> 3. 목표 메모리를 처음으로 달성하는 최소비용 찾으면 됨 
```python
N, M = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))
DP = [0] * (sum(cost)+1)  # 비용당 비활성화 가능한 메모리

for i in range(N):  # 각 앱에 대하여
    for j in range(sum(cost), cost[i]-1, -1):  # 각 비용에 대하여
        # 앱의 비용이 j보다 작다면
        if j >= cost[i]:
            # 비활성화하지 않았을 때의 바이트 수, 비활성화하였을 때의 바이트 수를 더한 값 비교
            DP[j] = max(DP[j], DP[j - cost[i]] + byte[i])

# 필요한 바이트 수 M 이상을 처음으로 달성하는 최소 비용 찾기
for i, mem in enumerate(DP):
    if mem >= M: exit(print(i))
```

#### 🖌 프로그래머스 17681 비밀지도 (2018 KAKAO BLIND RECRUITMENT)
> 1. 두 수를 비트별로 비교하여 정수로 변환하고, n개 미만의 수면 빈자리는 0으로 채운다.
> 2. 열마다 두 수를 순회하여, `replace`를 써서,1은 #으로 0은 공백으로 저장한다.

```python
def solution(n, arr1, arr2):
    return [f'{int(bin(i|j)[2:]):0{n}}'.replace("1","#").replace("0"," ") for i,j in zip(arr1,arr2)]
``` 

#### 🎙 프로그래머스 150368 이모티콘 할인 행사(2023 KAKAO BLIND RECRUITMENT)
> 1. 가능한 할인율 중복 조합 생성
> 2. 각 유저가 이모티콘을 구매할 할인율과 구매한도를 조회한다.
> 3. 그 때, 각 이모티콘의 할인율과 가격을 비교하여 할인율 조건을 충족하면 가격에 합산하고, 현재 가격이 사용자의 기대 가격 이상이면 이모티콘 플러스 가입자수를 증가시킨다.
> 4. 사용자가 만족하지 않으면 전체 가격을 합산시킨다.

```python
# 이모티콘 할인행사 (2023 KAKAO BLIND RECRUITMENT)
from itertools import product

def solution(users, emoticons):
    ans = []

    # 가능한 할인율 조합 생성
    for rates in product((10, 20, 30, 40), repeat=len(emoticons)):
        cnt, price = 0, 0

        # 각 사용자에 대하여
        for user_rate, user_price in users:
            now_cnt, now_price = 0, 0

            # 각 이모티콘에 대하여
            for rate, emoticon in zip(rates, emoticons):

                # 현재 할인율이 사용자의 기대 할인율 이상인 경우
                if rate >= user_rate:
                    now_price += (emoticon // 100 * (100 - rate))

                # 현재 가격이 사용자의 기대 가격 이상이면
                if now_price >= user_price:
                    now_cnt += 1; break

            # 만약 현재 사용자가 만족했다면
            if now_cnt == 1:
                cnt += 1  # 전체 만족하는 사용자 수 증가
            else:
                price += now_price  # 만족하지 않으면 가격 추가

        ans.append([cnt, price])

    return sorted(ans, key=lambda x: (-x[0], -x[1]))[0]
```

#### 👔 프로그래머스 258707 N+1 카드게임
> 1. 카드를 1/3과 2/3를 나누고, 아래 사항이 진행될때마다 라운드를 추가한다 
> 2. 첫번째, 원래 카드조합에서 비교한다.
> 3. 두번째, 카드조합 + 1개 뽑았을 때 비교한다.(코인 1개 감소)
> 4. 세번째, 카드조합 + 2개 뽑았을 때 비교한다.(코인 2개 감소)
> 5. 위 해당사항 없으면 현재까지 라운드를 반환한다.
```python
from collections import deque
def solution(coin,cards):
    N = len(cards)
    init = cards[:N//3]
    cards = deque(cards[N//3:])
    temp = set()
    round = 1
    def pre_test(temp, init):
        for i in temp:
            for j in init:
                if i!=j and i+j == N+1:
                    temp.remove(i)
                    init.remove(j)
                    return True
        return False

    def merge(cards):
        if cards: temp.update({cards.popleft(),cards.popleft()})

    while cards:
        merge(cards)
        # 1단계 : 사전에 init에서 N+1이 발견된다면 다음 라운드로
        if pre_test(init,init):
            round += 1
        # 2단계 : 기존 init에 없고, 선택한 1개 중에 있다면 (코인 1개 감소)
        elif coin >=1 and pre_test(init,temp):
            coin-=1
            round += 1
        # 3단계 : 기존 init에 없고, 선택한 2개를 포함해 있다면 (코인 1개 감소)
        elif coin>=2 and pre_test(temp,temp):
            coin -=2
            round += 1
        else:
            break
    return round
```

#### ❤️‍🔥 프로그래머스 258711 도넛과 막대 그래프
> 1. 생성 정점, 도넛, 막대, 8자 그래프를 구하기 위해 진입차수, 진출차수를 계산한다.
> 2. 생성 정점 : 진입차수가 없고, 진출차수가 있는 경우
> 3. 막대그래프 : 진입차수가 1개 이상이고, 진출차수가 없을 때
> 4. 8자그래프 : 진입차수가 2개 이상이고, 진출차수도 2개 이상일 때, 
> 5. 도넛그래프 : 생성정점의 진출차수 - 막대와 8자그래프 수
```py
def solution(edges):
    answer = [0, 0, 0, 0]  # 생성 정점, 도넛, 막대, 8자
    max_val = max(map(max, edges)) + 1  # +1 은 인덱스 맞춰주기 위함
    in_degree, out_degree = [0] * max_val, [0] * max_val

    # in, out 간선 저장
    for now_out, now_in in edges:
        out_degree[now_out] += 1
        in_degree[now_in] += 1

    for now_node in range(1, max_val):
        # 생성정점은 최상위 노드같이 맨 처음에 시작
        if in_degree[now_node] == 0 and out_degree[now_node] >= 2:  # 생성 노드
            answer[0] = now_node
        # 막대그래프는 들어오는게 1개 이상이고 나가는 것이 없을 때
        elif in_degree[now_node] >= 1 and out_degree[now_node] == 0:  # 막대 그래프
            answer[2] += 1
        # 들어오는 것이 2개 이상이고, 나가는것도 2개 이상
        elif in_degree[now_node] >= 2 and out_degree[now_node] == 2:  # 8자 그래프
            answer[3] += 1
    # 도넛은 생성정점의 아웃 개수 - 위 두개 그래프 갯수 빼면 됨
    answer[1] = out_degree[answer[0]] - sum(answer[2:])  # 도넛 그래프

    return answer
```