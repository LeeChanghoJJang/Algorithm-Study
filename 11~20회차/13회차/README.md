## Algorithm Study 13회차 회의 (24.4.28.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 4월 28일 일요일 저녁 7시  
        - 방식 : 김해 커피팀버

    나. 차주 예정 일정
        - 시간 : 5월 5일 일요일 오전 7시  
        - 방식 : 디스코드

    다. 변경사항
        1. 회의 일정 기본값은 일요일 오전 9시(변동 가능)
        2. 코테 기출 위주 문제 선정(난이도는 하향하고 최대한 다양한 문제 선정)
        3. 본인 선정 문제는 라이브로 코딩
        4. 신유형을 매주 한 명씩 선정했으나, 어려운 문제를 한 명씩 선정하는 것으로 변경.
            - 순서 : 이번주 최지우 (이상현 - 이창호 - 임경태 - 최지우 - 박동현 - 윤예리 - 이권민) -> 첫 차례는 예리 뜀
        5. 장소 선정 : 스터디원이 증대되어 장소를 송삼, 김해 중 하나로 결정(1번씩 로테이션)

### 🎵 문제 선정 및 방식 
    가. 유형 : 코딩테스트 기출 위주로 각자 리뷰할 문제 선정 
    나. 문제수 : 인당 2문제, 총 14문제
    다. 난이도 : 백준 플래티넘 이하  
    라. 코드 브리핑 && 리뷰 방식
      - 이번 주의 새로운 문제 : 오일러 경로
      - 문제 선정자가 라이브 코딩하면서 솔루션 리뷰
      - 푼 방식 이외에도 다양한 방법 제시

### 🎁 이번회차 풀이 문제
   ###### 1. 창호
    - 백준 2357 최소값과 최댓값(골드 1) - 세그먼트 트리
   ###### 2. 예리
    - 백준 1727 커플만들기(골드 2) - DP
   ###### 3. 경태
    - 백준 1199 오일러 경로(플래티넘 4) - 오일러 경로
   ###### 4. 동현
    - 백준 16946 벽 부수고 이동하기 4(골드 2)- BFS,DFS
   ###### 5. 상현
    - 백준 1062 가르침(골드 4) - 백트래킹
   ###### 6. 지우
    - 백준 2638 치즈(골드 3) - 탐색, 구현
   ###### 7. 권민
    - 백준 2533 사회망서비스(골드 3) - 트리DP
   
### 🤢 문제 선정
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

### 🏅 스터디 내용 
#### 🎈 백준 1062 가르침
> `백트래킹` 이용한 문제 풀이(복습) 
> 1. word_list : 익힐 단어 리스트
> 2. teach : 가르쳐야 할 알파벳
> 3. 'a','n','t','i','c'단어는 미리 학습처리 한다.
> 4. 가르칠 수 있는 최대 단어 숫자가 5미만인 경우는 0를 출력하고, 26인 경우 전 단어를 다 가르칠 수 있으므로 N을 출력한다.
> 5. 나머지의 경우 백트래킹을 돌려 K-5의 갯수만큼 추가로 배웠을 때 익힐 수 있는 단어의 수를 계속 갱신한다.

```python
def dfs(idx, teach_cnt):
    global max_

    # 가르칠 수 있는 글자 수가 K - 5에 도달하면 단어의 개수를 세고 최댓값 갱신
    if teach_cnt == K - 5:
        cnt = 0

        # 모든 단어에 대해 가르쳐진 글자가 포함되어 있는지 확인하여 개수 세기
        for word in word_list:
            cnt += all(teach[ord(char) - ord('a')] for char in word)

        max_ = max(max_, cnt)
        return

    # idx부터 25까지의 알파벳에 대해 가르치지 않은 경우를 가르치고 재귀 호출
    for i in range(idx, 26):
        if not teach[i]:
            teach[i] = True
            dfs(i, teach_cnt + 1)  # 가르친 글자 수 증가
            teach[i] = False  # 백트래킹: 가르친 글자를 다시 되돌리고 다음 알파벳으로 이동

# 입력 받기
N, K = map(int, input().split())
word_list = [set(list(input())) for _ in range(N)]  # 단어 리스트 생성
teach = [False] * 26  # 각 알파벳을 가르쳤는지 여부를 저장하는 배열
max_ = 0

# 예외 처리: K가 5 미만이면 0 출력
if K < 5:
    print(0)
    exit()
# 예외 처리: K가 26이면 모든 알파벳을 가르칠 수 있으므로 단어의 개수 N 출력
if K == 26:
    print(N)
    exit()

# 'a', 'n', 't', 'i', 'c'은 무조건 가르쳐야 함
for char in 'antic':
    teach[ord(char) - ord('a')] = True

# dfs 호출하여 단어를 가르치고 최대 가르칠 수 있는 단어의 개수 구하기
dfs(0, 0)
print(max_)
```

#### 🧰 백준 1199 오일러 회로
> `오일러 회로` : 꼭짓점과 변으로 이루어진 그래프가 있을 때, 모든 간선을 단 한번씩만 통과하는 회로(한붓그리기가 가능한 회로)
> 1. 인접배열을 count에 받고 graph를 그린다.
> 2. 모든 정점이 짝수 간선을 갖지 않은 경우, 한붓그리기가 불가하므로 가지친다.
> 3. DFS를 써서, 두 노드 사이에 남은 간선이 있다면 패스하고, 없다면 그래프에서 해당 노드를 제거한다.
> 4. 현재 노드에서 갈 수 있는 노드가 있다면 스택에서 다음 노드를 추가하고, 간선을 빼준다.(해당 노드로 이동하면서 간선 한 개씩 제거)
> 5. 현재 노드에서 갈 수 있는 노드가 없다면 스택에서 현재 노드 제거 및 출력(전부 제거됬으므로 한붓그리기 가능)
```python
# 1199 오일러 회로

import sys
sys.stdin = open("input.txt")

N = int(input())
count = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N):
    # 모든 정점이 짝수 차수를 갖지 않으면 오일러 회로 불가능
    if sum(count[i]) & 1: exit(print(-1))

    # 그래프 제작
    for j in range(i):
        if count[i][j]:
            graph[i].append(j)
            graph[j].append(i)

# DFS 진행
S = [0]
while S:
    now = S[-1]

    while graph[now]:
        next = graph[now][-1]

        # x가 y보다 더 작게
        x, y = (next, now) if now > next else (now, next)
        # 두 노드 사이에 남은 간선이 있다면 패스
        if count[x][y]: break
        # 두 노드 사이에 남은 간선이 없다면 그래프에서 해당 노드 제거
        graph[now].pop()

    # 현재 노드에서 갈 수 있는 노드가 있다면 스택에 다음 노드 추가 및 간선 소모
    if graph[now]:
        S.append(next)
        count[x][y] -= 1
    # 현재 노드에서 갈 수 있는 노드가 없다면 스택에서 현재 노드 제거 및 출력
    else:
        S.pop()
        print(now + 1, end=" ")
```


#### ⚽ 백준 1727 커플 만들기
> `그리디`와 `DP` 이용
> 1. 여자와 남자를 오름차순으로 정렬하여 받는다.
> 2. 여자가 많다고 가정하고 문제를 풀며, 반대일 경우에는 각 변수를 서로 바꿔준다.
> 3. DP에 남자를 행으로, 여자를 열로하여 성격차 합의 최솟값을 지속적으로 갱신한다.
> 4. 여자와 남자의 수가 같을 경우, 1명씩 적을 때에서 여자와 남자 성격 차이를 더한다.
> 5. 다를 경우 수가 많을 쪽에서 선택권이 있으므로, 1명씩 적을 때 + 현재 성격차합, 많은 쪽이 1명 적을 때와 비교해서 적은 숫자로 갱신한다. 

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

#### 🖌 백준 2357 최솟값과 최댓값
> `세그먼트 트리`를 활용하여 최솟값, 최댓값 선정
> 1. make_seg : 루트노드부터 리프노드까지 노드별로 trees에 최솟값과 최댓값을 지정해준다.
> 2. find : 범위가 주어지면, 범위 내에서의 trees에 최솟값과 최댓값을 지정해준다. 
```python
import sys
import math
sys.stdin = open('input.txt')

# make_seg : 세그먼트 트리를 만드는 함수
# 각 노드의 첫번째는 자식노드들의 최솟값, 두번째는 최댓값이 저장됨
# 루트 노드에는 범위를 최대화하고, 자식노드로 갈수록 범위는 좁아진다.
# 리프 노드에 도달할 경우, 그 인덱스에 해당하는 integer의 값을 반환한다.
def make_seg(start,end,index):
    if start == end:
        trees[index] = (integers[start],integers[start])
        return trees[index]
    mid = (start + end) // 2

    left_node = make_seg(start,mid,index*2)
    right_node = make_seg(mid+1,end,index*2+1)

    trees[index] = (min(left_node[0],right_node[0]),max(left_node[1],right_node[1]))
    return trees[index]
# 주어진 범위에 따른 최댓값과 최솟값을 반환하는 함수
def find(start,end,index):
    # 문제에서 주어진 범위에서 완전히 벗어난 경우
    if start > range2 or end < range1:
        return (sys.maxsize, 0)
    # 양쪽 끝이 범위 내에 들어온다면 tree의 index를 반환
    if start >= range1 and end <= range2:
        return trees[index]
    # 만약 한쪽 노드가 범위 밖이라면?
    # 범위 안쪽인 노드쪽에서의 최소, 최댓값만 도출해야함
    mid = (start + end) // 2
    left = find(start,mid,index*2)
    right = find(mid+1,end,index*2+1)
    return (min(left[0],right[0]),max(left[1],right[1]))

N,M = map(int,input().split())
integers = [int(input()) for _ in range(N)]
b = math.ceil(math.log2(N)) +1
node_n = 1 << b
trees = [0 for _ in range(node_n)]
make_seg(0,N-1,1)

for i in range(M):
    range1,range2 = map(int,input().split())
    range1 -= 1;range2 -= 1
    result = find(0,N-1,1)
    print(result[0],result[1])

``` 

#### 🎙 백준 2533 사회망 서비스(SNS)
> 트리 `DP`를 활용
> 1. 각 DP의 첫번째 인덱스는 얼리어답터가 아니고, 두번째 인덱스는 얼리어답터인 경우의 누적 갯수를 저장
> 2. DFS로 루트노드부터 탐색
> 3. DP의 루트노드에 저장된 얼리어답터의 최소값 출력

```python
# 깊이로 계산. h//2. 분기 될때마다 중복 제거를 위해 따로 처리 필요. 자식 노드에 저장된 값으로
# 계산하면 될듯. 자식 개수. 분기 될때 
# 1 2, 1 3/ 1개. 2 4 2개, 3 5 3 6 2개, 4 7 4 8 4 9 3개 
# 부모 자식중 하나만 얼리 어답터면 ㄱㅊ
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(node):
    for next in graph[node]:
        # 양방향. 부모가 아니면. 자식노드면 해당 노드의 dp값은 다 [0,1]
        # 넣거나 안넣거나.
        if not visited[next]:
            visited[next] = 1
            dfs(next)
            dp[node][0] += dp[next][1]
            # 지금 node가 아니면 자식노드가 얼어 일때의 값
            dp[node][1] += min(dp[next])
            # 지금 node가 얼어, 자식노드가 뭐든 상관 없.
        
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
# 지금 노드가 얼어일때랑 아닐때. 
dp = [[0,1] for _ in range(n+1)]
visited = [0]*(n+1)
visited[1] = 1
dfs(1)
print(min(dp[1]))

```

#### 👔 백준 2638 치즈
> 주로 `DFS`를 활용한 시뮬레이션 문제
> 1. 함수들은 아래와 같다.
>   - BFS : 치즈를 녹이는 함수(바로 전부 안녹이고, 한꺼번에 녹여야 탐색하면서 잘못될 여지 없음)
>   - contact_cheese : 치즈가 접촉한 횟수 기록(외부에서 2번 접촉해야 없앨 수 있음)하고, 확정된 치즈를 hubo set에 옮긴다.
>   - zero_trans: hubo에 있는 모든 치즈를 없애는 함수
>   - is_possible : 치즈가 1개라도 있으면 안되기에 전부 확인하는 함수
> 2. 치즈가 없을 때까지 위 함수들을 순차적으로 돌리고, 반복횟수만큼 time을 출력한다.

```python
import sys
from collections import deque

# 입력 파일을 열어서 stdin으로 설정합니다.
sys.stdin = open('input.txt')

# 상하좌우 이동을 위한 변수 설정
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 치즈를 녹이는 함수
def BFS(x, y, visited):
    # BFS를 위한 큐 설정
    queue = deque([[x, y]])
    # 현재 위치 방문 표시
    visited[x][y] = 1
    # BFS 탐색 시작
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            # 배열 범위 내에서 이동 가능하고, 방문하지 않은 위치인 경우
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 치즈가 아닌 경우, 방문 표시 후 큐에 추가
                if not arr[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                else:
                    # 치즈인 경우
                    # 접촉한 횟수를 기록
                    if contact_cheese.get((nx, ny)):
                        contact_cheese[(nx, ny)] += 1
                        # 두 번 이상 접촉한 경우, hubo에 추가
                        if contact_cheese.get((nx, ny)) >= 2:
                            hubo.add((nx, ny))
                    else:
                        contact_cheese[(nx, ny)] = 1

# 치즈를 없애는 함수
def zero_trans():
    # hubo에 있는 좌표들을 0으로 변환
    while hubo:
        i, j = hubo.pop()
        arr[i][j] = 0

# 치즈가 남아있는지 확인하는 함수
def possible(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return True
    return False

# 행과 열의 개수 입력
N, M = map(int, input().split())
# 치즈 상태 입력
arr = [list(map(int, input().split())) for _ in range(N)]
# 치즈 접촉 횟수 기록을 위한 딕셔너리 초기화
contact_cheese = {}
# 치즈가 접촉된 좌표를 기록할 set 초기화
hubo = set()

# 치즈가 모두 녹을 때까지 반복
cnt = 0
while possible(arr):
    # 치즈가 녹는 과정
    contact_cheese = {}  # 치즈 접촉 횟수 초기화
    BFS(0, 0, [[0] * M for _ in range(N)])  # BFS 탐색 및 치즈 접촉 횟수 계산
    zero_trans()  # hubo에 있는 좌표들을 0으로 변환
    cnt += 1  # 시간 증가

# 결과 출력
print(cnt)
```

#### ❤️‍🔥 백준 16946 벽 부수고 이동하기 4
> 그래프 탐색 문제이며, `BFS`를 주로 활용
> 1. grouping : 1로 둘러싸여있는 0의 그룹을 형성하고, 그룹의 크기를 반환하는 함수(이것을 zeros에 저장예정)
> 2. zeros에 0이거나(무리 형성이 안된 건), block가 0인 경우에만, 그 무리의 그룹을 만들어서, group_dict에 크기와 인덱스를 저장한다.
> 3. 이제 인접한 상하좌우의 그룹의 크기만 더해주면 된다. 중복된 무리에 대해서 더해주는 것을 막기위해 zeros의 값을 따로 저장해준다.
```py
import sys
from collections import deque

# 입력 파일을 열어서 stdin으로 설정합니다.
sys.stdin = open('input.txt')

# 상하좌우 이동을 위한 변수를 설정합니다.
dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 1로 둘러싸여 있는 0들의 그룹을 지정한다.
# group_dict에 각 무리의 정보를 저장해놓는다.
def grouping(x, y, num):
    # BFS를 위한 큐를 초기화합니다.
    queue = deque([[x, y]])
    # 해당 그룹의 번호를 부여하고, 해당 위치를 방문했음을 표시합니다.
    zeros[x][y] = num
    # 해당 그룹의 크기를 세기 위한 변수를 초기화합니다.
    cnt = 1
    # BFS 탐색을 시작합니다.
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색을 수행합니다.
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            # 배열 범위 내에 있고, 블록이 0이고, 방문하지 않은 위치인 경우
            if 0 <= nx < N and 0 <= ny < M and not blocks[nx][ny] and not zeros[nx][ny]:
                # 해당 위치를 현재 그룹으로 표시하고, 큐에 추가합니다.
                zeros[nx][ny] = num
                queue.append([nx, ny])
                # 그룹의 크기를 1 증가시킵니다.
                cnt += 1
    return cnt

# 입력을 받습니다.
N, M = map(int, input().split())
blocks = [list(map(int, list(input().strip()))) for _ in range(N)]
zeros = [[0] * M for _ in range(N)]

# 각 0들이 모여있는 그룹의 크기를 저장할 딕셔너리를 초기화합니다.
group_dict = {}

# 그룹의 번호를 나누는 작업을 수행합니다.
num = 0
for i in range(N):
    for j in range(M):
        # 블록이 0이고, 방문하지 않은 위치인 경우에 대해서만 그룹을 나눕니다.
        if not blocks[i][j] and not zeros[i][j]:
            num += 1
            # 그룹의 번호를 key로, 그룹의 크기를 value로 저장해서,
            # 나중에 인접한 곳의 번호에 해당하는 값만 더해주면 되게끔
            group_dict[num] = grouping(i, j, num)

# 변환된 결과를 저장할 리스트를 초기화합니다.
output = []
# 각 위치를 순회하며 변환을 수행합니다.
for i in range(N):
    result = ''
    # temp : 각 위치별 연결된 0의 갯수를 저장하는 임시 변수
    for j in range(M):
        temp = 0
        # 블록이 1인 경우, 주변의 그룹에 대해 크기를 확인하고 결과를 계산합니다.
        if blocks[i][j]:
            # breaks에 넣는 이유는 같은 무리면 패스하게끔 해서 중복되게 저장하지 않으려고
            breaks = set()
            temp += 1
            # 인접한 상하좌우만 탐색해서 그 그룹의 0의 개수만 더해주면 됨
            for k in range(4):
                ni = i + dr[k][0]
                nj = j + dr[k][1]
                if 0 <= ni < N and 0 <= nj < M and not blocks[ni][nj] and zeros[ni][nj] and zeros[ni][nj] not in breaks:
                    breaks.add(zeros[ni][nj])
                    temp += group_dict[zeros[ni][nj]]
        # 결과를 10으로 나눈 나머지를 계산하여 문자열에 추가합니다.
        temp %= 10
        result += str(temp)
    # 한 행의 결과를 저장합니다.
    output.append(result)

# 결과를 출력합니다.
sys.stdout.write('\n'.join(output))
```
