## Algorithm Study 17회차 회의 (24.6.8.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 6월 8일 일요일 오후 7시  
        - 방식 : 디스코드

    나. 차주 예정 일정
        - 시간 : 6월 15일 토요일 오후 7시  
        - 방식 : 송삼 2층

    다. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 이창호 - 최지우 - 이권민 - 박동현 - 이상현 - 윤예리 - 임경태  (순서는 매번 랜덤으로 변경 예정) 
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
    - 프로그래머스 92343 양과 늑대(2022 KAKAO BLIND RECRUITMENT, Lv.3) 
   ###### 2. 예리
    - 백준 1079 마피아(골드 2) 
   ###### 3. 경태
    - 백준 13904 과제(골드 3)
   ###### 4. 동현
    - 백준 2812 크게 만들기(골드 3)
   ###### 5. 상현
    - 프로그래머스 17686 파일명 정렬(2028 KAKAO BLIND RECURITMENT, Lv.2)
   ###### 6. 지우
    - 프로그래머스 92345 - 사라지는 발판 (2022 KAKAO BLIND RECRUITMENT, Lv.3)
   ###### 7. 권민
    - 프로그래머스 60057 - 문자열 압축 (2020 KAKAO BLIND RECRUITMENT, Lv.2)

### 🤢 문제 선정
   ###### 1. 창호
    - 백준 2344 거울(골드 4) 
   ###### 2. 예리
    - 백준 11779 최소비용 구하기(골드 3) 
   ###### 3. 경태
    - 백준 2437 저울(골드 2)
   ###### 4. 동현
    - 백준 12689 뮤탈리스크(골드 4)
   ###### 5. 상현
    - 프로그래머스 92335 k진수에서 소수 개수 구하기(Lv.2)
   ###### 6. 지우
    - 백준 1339 단어 수학 (골드 4)
   ###### 7. 권민
    - 백준 24533 팰린드롬 게임(골드 4)

### 🏅 스터디 내용 
#### 🎈 백준 1079 마피아
> 백트래킹을 활용하여 문제 풀이
> `mapia` 함수 : 몇명 남았는지에 따라서 마피아가 보낼 최대 밤수 도출
> 남는 날이 없거나, 마피아 혼자 살아남았으면 백트래킹
> visited 대신 유죄지수와 살았는지 여부를 기준으로 백트래킹

```python
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
criminal = list(map(int, input().split()))

R = [
    list(map(int, input().split()))
    for _ in range(n)
]

eunjin = int(input())
is_alive = [True] * n

ans = 0
flag = False
def mafia(remain, nights):
    global ans, flag

    if flag:
        return

    ans = max(ans, nights)

    if remain == 0:
        return

    if remain == 1 and is_alive[eunjin]:
        flag = True
        return

    # 짝수명이 남았으면 밤이다.
    if remain % 2 == 0:
        for i in range(n):
            if not is_alive[i] or i == eunjin:
                continue
            is_alive[i] = False
            # 살아있는 사람들의 유죄 지수 변경
            for j in range(n):
                if not is_alive[j]:
                    continue
                criminal[j] += R[i][j]
            mafia(remain - 1, nights + 1)
            # 원상 복구
            for j in range(n):
                if not is_alive[j]:
                    continue
                criminal[j] -= R[i][j]
            is_alive[i] = True

    # 홀수명이 남았으면 낮이다.
    else:
        max_criminal = -1
        index = -1

        for i, c in enumerate(criminal):
            if not is_alive[i]:
                continue

            if max_criminal < c:
                index = i
                max_criminal = c

        if index == eunjin:
            return

        is_alive[index] = False
        mafia(remain - 1, nights)
        is_alive[index] = True

mafia(n, 0)

print(ans)
```
#### 🧰 백준 2812 크게 만들기
> 1. 주어진 number에서 수를 계속 뽑아 stack에 넣는다
> 2. 넣을 때마다 갯수를 체크하며, 만약 마지막 원소가 새 숫자보다 작은 경우 pop한다. 
> 3. 만약 전부 뽑아내지 못했다면, 처음부터 K개 만큼만 추려낸다. 

```python
import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
number = input().strip()

num_to_remove = K
stack = []

for digit in number:
    if num_to_remove and stack and stack[-1] <digit:
        stack.pop()
        num_to_remove-=1
    stack.append(digit)

if num_to_remove >0:
    stack = stack[:-num_to_remove]

print(''.join(stack))
```

#### ⚽ 백준 13904 과제
> 1. w의 최대힙을 구성한다.
> 2. pop을 했을 때, 해당 남은 일자에 우선적으로 값을 넣는다. 단, 해당 열이 차있을 경우에는 한칸씩 내려오면서 채운다.
> 3. 전칸이 차면 그 합을 도출한다.

```python
import sys
from heapq import *

sys.stdin = open('input.txt')
N = int(input())

heap = []
for i in range(N):
    d,w = map(int,input().split())
    heappush(heap,(-w,d))
result = [0] * (N+1)

while heap:
    now, day = heappop(heap)
    for i in range(min(day,N),0,-1):
        if result[i] == 0:
            result[i] = -now
            break
print(sum(result))
```

#### 🖌 프로그래머스 17686 파일명 정렬
> 1. 정규표현식을 이용(([0-9]+) : 숫자 하나이상을 포함하는지 여부, 괄호를 쓰고 split에 넣으면 그것까지 포함해서 분할)
> 2. 헤더부분을 글자로, 숫자부분을 정수로 변환하여 정렬한다.

```python
import re

def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]

    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sort]
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

#### 👔 프로그래머스 60057 문자열 압축
> 1. 겹치는 글자수를 기준으로 중첩반복문을 수행한다.
> 2. temp는 반복 기준이 되는 글자들이고, cnt는 반복 횟수이다. 
> 3. 만약 반복되면 compress에 횟수와 그 문자열을 적고, temp를 갱신한다.
> 4. 반복문을 종료했을 때, result에 최소의 길이를 갱신한다.

```python
def solution(s):
    result = float('inf')
    for i in range(1,len(s)+1):
        compress='';temp=s[:i];cnt=1
        for j in range(i,len(s)+i,i):
            if temp ==s[j:i+j]:
                cnt+=1
            else:
                if cnt !=1:
                    compress += f'{cnt}{temp}'
                else:
                    compress += temp
                temp = s[j:i+j]
                cnt=1
        result = min(result,len(compress))
    return result
```

#### ❤️‍🔥 프로그래머스 92343 양과 늑대
> 1. graph를 만들어 각 양과 늑대의 연결정보를 저장한다.
> 2. `DFS`를 통해 최대한 늑대에게 안잡아 먹힌 양의 갯수를 구한다.
> 3. 다음 노드가 양인 노드와 늑대인 노드를 나눠서 dfs를 수행하고, 양이 더 적은 경우에는 수행하지 않는다.
> 4. 최대한 양의 갯수를 갱신한다.

```py
from collections import deque,defaultdict

def solution(info,edges):
    graph = defaultdict(list)

    for parent,child in edges:
        graph[parent].append(child)

    max_sheep = 0

    def dfs(sheep,wolf,current,path):
        nonlocal max_sheep
        max_sheep = max(max_sheep,sheep)

        for node in path:
            for next_node in graph[node]:
                if next_node not in path:
                    if info[next_node]==0:
                        dfs(sheep+1,wolf,current,path|{next_node})
                    else:
                        if sheep > wolf + 1:
                            dfs(sheep,wolf+1,current,path|{next_node})

    dfs(1,0,0,{0})

    return max_sheep
```

#### ❤️‍🔥 프로그래머스 92345 사라지는 벌판
> 1. 방문하지 않은 곳과 보드가 있는 곳에만 방문한다.
> 2. 차례를 번갈아가면서할 때, 위치를 반대로 하면서 발판을 이동한다.
> 3. 더 이상 갈곳이 없으면, result[0]가 false면 이길수 있고, true면 진다. 그 당시의 turn을 반환한다.

```py
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def solution(board, aloc, bloc):
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


def in_range(board, y, x):
    if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
        return False
    return True


def is_finished(board, y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(board, ny, nx) and board[ny][nx]:
            return False
    return True


def solve(board, y1, x1, y2, x2):
    # can_win, turn
    if is_finished(board, y1, x1):
        return [False, 0]

    # 서로 두 위치가 같을 때 이번 턴에 움직이면 무조건 이기므로
    if y1 == y2 and x1 == x2:
        return [True, 1]

    min_turn = INF
    max_turn = 0
    can_win = False

    # dfs
    for i in range(4):
        ny = y1 + dy[i]
        nx = x1 + dx[i]
        if not in_range(board, ny, nx) or not board[ny][nx]:
            continue

        board[y1][x1] = 0
        result = solve(board, y2, x2, ny, nx)  # 차례가 바뀌기 때문에 위치를 바꿔준다.
        board[y2][x2] = 1

        # 이 시점에서는 result[0]이 False여야만 현재 턴에서 내가 이길 수 있다.
        if not result[0]:
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win:
            max_turn = max(max_turn, result[1])

    turn = min_turn if can_win else max_turn

    return [can_win, turn + 1]

```
