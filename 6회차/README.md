## Algorithm Study 6회차 회의 (24.3.10.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 3월 10일 일요일 저녁 8시
        - 장소 : 디스코드 통한 비대면 회의

    나. 차주 예정 일정
        - 시간 : 3월 16일 토요일 아침 9시  
        - 방식 : 디스코드 통한 비대면 회의

### 🎵 문제 선정 및 방식 
    가. 유형 :『유형』 별로 '각자' '상', '하' 문제 선정 
    나. 문제수 : 인당 2문제, 총 10문제
    다. 난이도 : 최대 백준 골드 이하 
    라. 코드 브리핑 && 리뷰 방식
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리

### 🤢 이번회차 풀이 문제
   ###### 1. 창호
    - 백준 1744 수묶기(골드 4) - 상
    - 백준 1080 행렬(실버 1) - 하
   ###### 2. 경태
    - 백준 1865 웜홀 (골드 3) - 상
    - 백준 5525 IOIOI(실버 1) - 하
   ###### 3. 예리
    - 백준 11066 파일 합치기(골드 3) - 상
    - 백준 1713 후보 추천하기(실버 1) - 하 
   ###### 4. 동현
    - 백준 2470 두 용액(골드 5) - 상
    - 백준 14235 크리스마스 선물(실버 3) - 하
   ###### 5. 상현
    - 백준 17406 배열돌리기4(골드 4) - 상
    - 백준 15663 N과 M(9)(실버 2) - 하

### 🎁 문제 선정
   ###### 1. 창호
    - 백준 11437 LCA(골드 3) - 상
    - 백준 14501 퇴사(실버 3) - 하
   ###### 2. 경태
    - 백준 14938 서강그라운드 (골드 4) - 상
    - 백준 9251 LCS(골드 5) - 하
   ###### 3. 예리
    - 백준 1202 보석도둑(골드 2) - 상
    - 백준 18111 마인크래프트(실버 2) - 하 
   ###### 4. 동현
    - 백준 1976 여행가자(골드 4) - 상
    - 백준 18352 특정 거리의 도시 찾기(실버 2) - 하
   ###### 5. 상현
    - 백준 17404 RGB거리2(골드 4) - 상
    - 백준 10844 쉬운 계단 수(실버 1) - 하


### 🏅 스터디 내용 
#### 🎈 백준 1080 행렬  
> 해결방법 : `그리디 알고리즘`을 이용해 푸는 문제라고 하지만, 왠만하면 `완전탐색`으로 풂
```python
N, M, cnt = map(int, input().split()), 0
A, B = [input() for _ in range(N)], [input() for _ in range(N)]
# 두 행렬값의 차 행렬을 만들어 모두 0 인지 체크
sub = [[abs(int(a) - int(b)) for a, b in zip(A[i], B[i])] for i in range(N)]

for i in range(N):
    for j in range(M):
        if sub[i][j]:  # 차이가 있고
            if i < N - 2 and j < M - 2:  # 뒤 부분에 충분히 바꿀만한 공간이 있으면 바꿈
                for ci in range(3):
                    for cj in range(3):
                        sub[i+ci][j+cj] = 1 - sub[i+ci][j+cj]
                cnt += 1
            else:  # 뒤 부분에 바꿀 공간이 없으면 불가능
                exit(print(-1))
print(cnt)
```

#### 🧰 백준 1713 후보 추천하기
> 첫번째 : 딕셔너리를 활용한 반복문
>    - 값을 추천수 > 인덱스의 순서로 우선순위 정렬 
```python
N, rec, pic = int(input()), input(), {}

for i, n in enumerate(input().split()):
    n = int(n)
    # pic는 pic.keys()와 동일
    if n in pic: pic[n][0] += 1  # 사진틀에 있으면 추천수 증가
    else:  # 사진틀에 없으면 사진 추가 [추천수, 순번]
        if len(pic) >= N:  # 공간이 없으면 최소 추천 수 사진 제거
            min_stu = min(pic.items(), key=lambda x: (x[1][0], x[1][1]))
            del pic[min_stu[0]]
        pic[n] = [1, i]
# 키값을 오름차순으로 소트 
print(*sorted(pic))
```
> 두번째 : 힙의 구조를 이용(추천수, 인덱스를 우선순위로)
```python
import sys
from heapq import *
sys.stdin = open('input.txt')
# 후보 최대 인원수
N = int(input())
# 주어지는 추천번호
student_num = int(input())
# 추천번호
student_list = list(map(int,input().split()))
# 순서와 횟수를 저장하기 위해 heap으로 저장
heap = []

for idx, num in enumerate(student_list):
    # heap의 정보를 계속 갱신하기 위한 임시 heap
    tmp_heap = []
    # 기존 번호와 추천된 번호가 같을 때 여부를 판단하기 위한 변수
    flg=0
    # heap에서 모두 꺼내서, 같은 넘버가 추천된 경우가 있다면 cnt 추가하고 임시 heap에 저장
    while heap:
        cnt,old_idx,std_num = heappop(heap)
        cnt +=1 if std_num ==num else 0
        heappush(tmp_heap,(cnt,old_idx,std_num))
        flg += std_num == num
    # flg가 그대로고, tmp_heap이 N으로 꽉찼으면? 하나 빼자
    if not flg and len(tmp_heap) == N:
        heappop(tmp_heap)
    # 그리고 새로운 원소로 채워넣는거지(순서는 그대로, 횟수는 0로)
    if not flg:
        heappush(tmp_heap,(0,idx,num))
    heap = tmp_heap
# 추천번호만 저장한 리스트를 저장 
answer_list = [x[-1] for x in heap]
answer_list.sort()
print(*answer_list)
```

#### ⚽ 백준 1744 수묶기
> `그리디 알고리즘`으로 양수와 음수를 애초에 정해서 큰수들을 더해가면서 최적해 찾기
```python
N, pos, neg, ans = int(input()), [], [], 0

for _ in range(N):
    n = int(input())
    if n > 1: pos.append(n)
    elif n < 1: neg.append(n)
    else: ans += 1

pos.sort(reverse=True); neg.sort()  # 절댓값이 큰 수 부터 정렬
# 2개씩 묶어 큰값을 더해주는 함수
def f(pn):
    global ans
    for i in range(0, len(pn), 2):
        if len(pn) <= i+1: ans += pn[i]
        else: ans += pn[i] * pn[i+1]

f(pos); f(neg); print(ans)
```

#### 🖌 백준 1865 웜홀
> `벨만 포드` 알고리즘을 이용하여 푸는 문제
> 핵심은 음수 순환 사이클이 있는지 여부가 핵심
> n-1번만큼 순환하여 값이 계속 갱신된다는 것은 양수보다 음수 사이클이 있다는 것

```python
def bellman_ford(start):
    global is_cycle
    dist[start] = 0
    # 전체 N번의 라운드 반복
    # N-1번까지 모든 정보가 업데이트됨 N번째부터는 음수순환이 아니라면 불변해야함
    for i in range(N):  
        for s, e, t in graph:  # 매 반복마다 모든 간선 확인
            if dist[s] != float('inf') and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                # N번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N - 1: is_cycle = True; return

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph, dist = [], [float('inf')] * (N+1)
    is_cycle = False

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append([S, E, T])
        graph.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append([S, E, -T])
    
    for i in range(1, N + 1):
        if dist[i] == float('inf'):
            bellman_ford(i)

    print('YES' if is_cycle else 'NO')
```   

#### 🎙 백준 2470 두 용액
> `투 포인터` 이용하는 방법
> 1. 수를 음수부터 오름차순으로 정렬
> 2. `투 포인터` 설정(left, right)
> 3. left, right를 더한 값이 0보다 클경우 right감소
> 4. 반대의 경우 left 증가. 중간중간 최저값이 나오는 경우 저장
```python
def tp():
    s, e = 0, -1
    min_v = abs(feat[s] + feat[e])
    ans = (feat[s], feat[e])

    while s < e:
        pls = feat[s] + feat[e]
        if min_v > abs(pls):
            min_v = abs(pls)
            ans = (feat[s], feat[e])
        # 인덱스 갱신
        if pls < 0: s += 1
        else: e -= 1

    return ans

N = int(input())
feat = sorted(map(int, input().split()))
print(*tp())
```
> 절대값이 큰 순으로 정렬하여 두칸씩 합을 비교
```python
N = int(input())
feat = sorted(map(int, input().split()), key=lambda x: abs(x))  # 용액의 절댓값 기준으로 정렬
min_v, temp = 1e+10, 0

for i in range(N-1):
    pls = abs(feat[i] + feat[i+1])  # 이웃한 두 수 비교
    if min_v > pls:
        min_v = pls; temp = i

print(min(feat[temp], feat[temp+1]), max(feat[temp], feat[temp+1]))
```

#### 👔 백준 5525 IOIOI
> KMP 알고리즘 이용 
```python
def KMP(P, text):
    lps = [0] * len(P)
    for i in range(1, len(P)):
        # 패턴의 현재 인덱스의 문자가 이전 인덱스 문자에 이어서 접두사와 일치하는 부분이 있으면
        if P[lps[i-1]] == P[i]:
            # 일치부분이 1개 증가하는 것
            lps[i] = lps[i-1] + 1

    # lps 배열 적용 부분 -> KMP
    # 일치했다는 사실을 어떻게 이용할 것인가?
    # 문자 : ABCDABCDABEE
    # 패턴 : ABCDABE
    # < 바로 아래단계로 이동 (lps[5] == 2 이므로) >
    # 문자 : ABCDABCDABEE
    # 패턴 :     ABCDABE
    cnt, j = 0, 0  # cnt: 일치하는 부분의 개수 / j: 패턴에서 비교하고 있는 부분
    for i in range(len(text)):  # i: 문자열에서 비교하고 있는 부분
        # 일치했던 정보와 lps배열을 이용하여 중간 단계를 뛰어넘는 부분
        # while 문을 이용하는 이유 : 주어진 정보로 최대한 중간 단계를 뛰어넘기 위해
        # 패턴의 처음부분을 조사하지 않고 있으며 텍스트와 패턴이 일치하지 않는다면
        while j > 0 and text[i] != P[j]:
            j = lps[j - 1]
        # 텍스트와 패턴이 일치하면
        if text[i] == P[j]:
            # 패턴의 인덱스가 끝까지 도달했다면
            if j == len(P) - 1:
                #  패턴 글자에 해당하는 부분이 있다는 것이므로 카운트 +1 하고 다음으로 점프하여 탐색 진행
                cnt += 1
                j = lps[j]
            # 패턴의 인덱스가 진행중이라면 문자열의 다음부분과 패턴의 다음부분을 비교하기 위해 인덱스 증가
            else:
                j += 1
    return cnt

N, M, S = int(input()), int(input()), input()
print(KMP('I'+'OI'*N, S))
```
> 문자열이 IOI인 것을 이용
> 1. I를 기준으로 split
> 2. O가 몇개가 연속되는지 여부를 기준으로 판단하기 위해 딕셔너리에 저장
> 3. 최종적으로 N개 이상 O가 있는 값을 가진 키의 갯수를 구하고, result값에 가산
```python
N = int(input())
input()
S = input().strip('O').split('I')
dict_ = {}
temp = result = 0

for elem in S:
    if elem == 'O':
        temp += 1
    else:
        if temp in dict_:
            dict_[temp] += 1
        else:
            dict_[temp] = 1
        temp = 0

for key, value in dict_.items():
    if key >= N:
        result += (key - N + 1) * value

print(result)
```
---
#### 📀 백준 11066 파일합치기 
> 어려운 `DP` 문제
> 1. 2차원 배열에 각 행과 열의 합을 통해 누적합 도출
> 2. 2칸 이상부터 누적된 파일의 합 중 작은 값을 가산해줘야 함
```python
import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    k = int(input())
    f = list(map(int,input().split()))

    d = [[0] * k for _ in range(k)]
    # 첫번째는 각 행과 열을 더했을때 누적합을 D에 저장
    for i in range(k-1):
        d[i][i+1] = f[i] + f[i+1]
        for j in range(i+2, k):
            d[i][j] = d[i][j-1] + f[j]
    # 2칸이상 누적합부터
    for n in range(2,k):
        for i in range(k-n):
            j = i+n
            costs = [d[i][x] + d[x+1][j] for x in range(i,j)]
            d[i][j] += min(costs)

    print(d[0][k - 1])  # 모든 장을 합치는데 필요한 최소 비용
```
#### 🧏‍♀️ 백준 14235 크리스마스 선물
> `최대힙`을 이용하여 순차적으로 선물을 꺼냄. 우선순위대로 저장  
```python
from heapq import *

n = int(input())
value_heapq = []

for _ in range(n):
    a, *gift_list = list(map(int, input().split()))

    # a가 0이라면 가치가 가장 큰 선물을 pop한 후
    # 그 값을 출력
    # 만약 선물 상자가 비었다면 -1을 출력
    if a == 0:
        if value_heapq:
            print(-heappop(value_heapq))
        else:
            print(-1)
            
    # a가 0이 아니라면 선물을 충전하는 곳이므로
    # 선물의 가치를 저장하는데 최대힙을 이용하기 위해
    # 부호를 반대로 해줌
    else:
        for gift in gift_list:
            heappush(value_heapq, -gift)
```
#### ❤️‍🔥 백준 15663 N과 M(9)
> `DFS` 이용하여 순열 도출 
```python
def per(i, arr):
    if len(arr) == M:
        global ans; ans.add(tuple(arr))
        return
    for j in range(i, N):
        num[i], num[j] = num[j], num[i]
        per(i+1, arr + [num[i]])
        num[i], num[j] = num[j], num[i]

N, M = map(int, input().split())
num = list(map(int, input().split()))
ans = set()
per(0, [])
for p in sorted(ans): print(*p)
```
> `itertools` 이용하여 순열 도출 
```python
from itertools import permutations
N, M = map(int, input().split())
perms = sorted(set(permutations(map(int, input().split()), M)))
for p in perms: print(*p)
```
#### ❤️‍🔥 백준 17406 배열돌리기4
> `델타탐색` 이용 
```python
from itertools import permutations as per
from copy import deepcopy

ds = ((1, 0), (0, 1), (-1, 0), (0, -1))

def rotate(r, c, s):  # row, column, seal
    for l in range(1, s+1):
        i, j = r-l-1, c-l-1
        temp = B[i][j]
        for di, dj in ds:
            for _ in range(2*l):
                B[i][j] = B[i+di][j+dj]
                i += di; j += dj
        B[i][j+1] = temp


N, M, K = map(int, input().split())  # row_num, column_num, oper_num
A = [list(map(int, input().split())) for _ in range(N)]  # array
oper = [list(map(int, input().split())) for _ in range(K)]  # operation
ans = 5e+4

for p in per(oper, K):  # 각 연산 순열로 순회
    B = deepcopy(A)
    [rotate(r, c, s) for r, c, s in p]
    ans = min(ans, min(map(sum, B)))

print(ans)

```
> `행`단위로 배열돌리기 수행 
```python
from itertools import permutations

# (r, c, s) 회전 연산을 수행하는 함수
def rotation_func(r, c, s):
    for depth in range(s):
        temp1 = temp[r - 1 - (s - depth)][c - 1 - (s - depth)]

        for row in range(r - 1 - (s - depth), r - 1 + (s - depth)):
            temp[row][c - 1 - (s - depth)] = temp[row + 1][c - 1 - (s - depth)]
        for col in range(c - 1 - (s - depth), c - 1 + (s - depth)):
            temp[r - 1 + (s - depth)][col] = temp[r - 1 + (s - depth)][col + 1]
        for row in range(r - 1 + (s - depth), r - 1 - (s - depth), -1):
            temp[row][c - 1 + (s - depth)] = temp[row - 1][c - 1 + (s - depth)]
        for col in range(c - 1 + (s - depth), c - 1 - (s - depth), -1):
            temp[r - 1 - (s - depth)][col] = temp[r - 1 - (s - depth)][col - 1]

        temp[r - 1 - (s - depth)][c - (s - depth)] = temp1

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
rotation_list = [list(map(int, input().split())) for _ in range(K)]
rotation_list = permutations(rotation_list)
min_ = float('inf')

for rotation in rotation_list:
    # 원본 matrix를 변환하지 않기 위해 matrix를 복사하여
    # temp에 저장
    temp = [row[:] for row in matrix]

    for r, c, s in rotation:
        rotation_func(r, c, s)

    min_ = min(min_, min(sum(row) for row in temp))

print(min_)
```
