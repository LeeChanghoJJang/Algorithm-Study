## Algorithm Study 8회차 회의 (24.3.23.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 3월 23일 토요일 아침 10시 반
        - 장소 : 김해 커피팀버

    나. 차주 예정 일정
        - 시간 : 3월 30일 토요일 아침 9시 반  
        - 방식 : 김해 커피팀버  

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
    - SWEA 2382 미생물 격리
   ###### 2. 경태
    - SWEA 원자 소멸 시뮬레이션
   ###### 3. 예리
    - SWEA 5650 핀볼게임 
   ###### 4. 동현
    - 백준 1647 도시 분할 계획
   ###### 5. 상현
    - 백준 2239 스도쿠
  
### 🎁 문제 선정
   ###### 1. 창호
    - 백준 2098 외판원 순회(골드 1)
    - 백준 1541 잃어버린 괄호(실버 2)
   ###### 2. 예리
    - 백준 1774 우주신과의 교감(골드 3)
    - 백준 11286 절대값 힙(실버 1)
   ###### 3. 경태
    - SOFTEER 염기서열 커버(lv.3)
    - 백준 1620 나는야 포켓몬 마스터 이다솜(실버 4) 
   ###### 4. 동현
    - 백준 16236 아기상어(골드 3)
    - 백준 1072 게임(실버 3)
   ###### 5. 상현
    - 백준 27978 보물 찾기2(골드 3)
    - 백준 4358 생태학(실버 2)

### 🏅 스터디 내용 
#### 🎈 백준 1647 도시 분할 계획
> 첫번째 :`Kruskal` 알고리즘 활용
> 1. find 함수 : 무리의 대표 노드를 찾는 함수(최상위 노드)
> 2. union 함수 : 두 무리를 합쳐주는 함수
> 3. edges를 오름차순으로 정렬하여, 비용이 낮은 가중치부터 무리에 합한다.
> 4. 최소 스패닝 트리가 완성되면 다른 대표노드가 존재하지 않으므로 반복문이 종료된다.
```python
# 특정 값의 루트 찾는 함수
def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

# 하나의 트리로 합치는 함수
def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

# N: 집의 개수, M: 길의 개수
N, M = map(int, input().split())
# 간선 비용 기준 오름차순 정렬
edges = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[2])
# 각각의 트리 생성 (부모가 자기 자신)
parent = [i for i in range(N+1)]
# 비용 배열
costs = []
# 간선 순회
for s, e, cost in edges:
    if find(s) != find(e):
        union(s, e)
        costs.append(cost)

print(sum(costs[:len(costs)-1]))
```
> 두번째 :`Prim` 알고리즘 활용
> 1. 우선 연결정보를 graph로 만든다.(무향 그래프)
> 2. 최소힙을 구현하여, 전부 방문할 때까지 그리디하게 최소가중치를 더한다.
> 3. 방문하지 않은 곳이 없다면 종료
```python
def prim(visited):
    spanning_tree = []
    min_heap = [(0, 1)]
    result = []
    while min_heap:
        weight, start = heappop(min_heap)
        if not visited[start]:
            visited[start]=1
            spanning_tree.append((weight,start))
            result.append(weight)
            for next, edge_weight in graph[start]:
                if not visited[next]:
                    heappush(min_heap,(edge_weight,next))
    return sum(result) - max(result)


N,M = map(int,sys.stdin.readline().split())
graph = {i : [] for i in range(1,N+1)}
for i in range(M):
    start, end, cost = map(int,sys.stdin.readline().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))
print(prim([0] * (N+1)))
```

#### 🧰 백준 2239 스도쿠 
> `백트래킹`을 활용(단, 스도쿠 충족여부 검사는 별도 함수 구현)
> 1. is_possible 함수의 역할
>   - 가로검사, 세로검사, 그 좌표가 속하는 3*3 행렬 검사
> 2. 스도쿠에서 0을 만날 때마다, 넣을 수 있는 값인지 조사한 후, 가능한 값을 넣는다.
> 3. 백트래킹으로 모든 반복문을 순회해도 없을 경우에는 인덱스를 낮추며, 제대로 채워질 때까지 막는다.

```python
# 주어진 좌표에서 숫자 n이 유효한지 확인하는 함수
def is_possible(x, y, n):
    # 가로, 세로, 3x3 박스에 중복된 숫자가 있는지 확인
    for i in range(9):
        if arr[x][i] == n:  # 같은 행에 이미 n이 있는 경우
            return False
        if arr[i][y] == n:  # 같은 열에 이미 n이 있는 경우
            return False

    # 3x3 박스에 이미 n이 있는 경우
    ny = (y // 3) * 3
    nx = (x // 3) * 3
    for dx in range(3):
        for dy in range(3):
            if arr[nx + dx][ny + dy] == n:
                return False
    return True

# 백트래킹을 이용한 DFS 함수
def dfs(idx):
    # 0인 칸이 없는 경우, 즉 모든 칸이 채워진 경우에는 결과 출력 후 프로그램 종료
    if idx == len(zero):
        for row in arr:
            print(*row, sep='')
        exit(0)

    # 0인 칸에 대해 가능한 숫자를 넣어보고 DFS 호출하여 퍼즐 완성
    x, y  = zero[idx]  # 0인 칸의 좌표
    for i in range(1, 10):  # 1부터 9까지 가능한 숫자 시도
        if is_possible(x, y, i):  # 숫자 i가 유효한 경우
            arr[x][y] = i  # 해당 위치에 숫자 i를 넣음
            dfs(idx + 1)  # 다음 0인 칸으로 진행
            arr[x][y] = 0  # 백트래킹: 이전 상태로 돌아가기 위해 다시 0으로 초기화

N = 9
arr = []
# 스도쿠 퍼즐 입력 받기
for _ in range(N):
    row = list(input())
    row = list(map(int, row))  # 문자열로 입력 받은 숫자를 정수로 변환
    arr.append(row)

zero = []  # 0인 칸의 좌표를 저장할 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:  # 0인 칸인 경우
            zero.append((i, j))  # 좌표를 zero 리스트에 추가

dfs(0)  # DFS 탐색 시작
```

#### ⚽ swea 2382 미생물 격리
> `DP` 1차원 배열을 이용
1. 방향 딕셔너리 설정(ways)하여 델타탐색
2. 미생물 군집정보를 `info` 설정. key값이 좌표, value는 인덱스와 미생물 갯수
3. 처음 방문하는 곳이면 그대로 저장
4. 이전에 정보가 저장되어 있으면 비교하여 갯수가 더 큰 정보를 딕셔너리에 저장해주고, temp 배열에는 해당 인덱스는 0로, 나머지 인덱스에 갯수를 더해준다.
5. 정해진 시간만큼 이동 후, temp에 남아있는 cnt를 더해주면 끝.

```python
from collections import deque

# 이동 방향에 따른 좌표 변화량을 정의
ways = {1: (-1, 0),  # 상
        2: (1, 0),   # 하
        3: (0, -1),  # 좌
        4: (0, 1)}   # 우

# 테스트 케이스 반복
for tc in range(1, int(input()) + 1):
    # 입력 받기
    N, M, K = map(int, input().split())  # N: 배열 크기, M: 시간, K: 미생물 군집 수
    arr = [[0] * N for _ in range(N)]    # N x N 배열 초기화
    temp = deque([])                     # 미생물 군집 정보를 담을 deque 초기화

    # 초기 미생물 군집 정보 입력
    for _ in range(K):
        x, y, cnt, way = map(int, input().split())
        temp.append([x, y, cnt, way])

    # 시간 M만큼 반복
    for _ in range(M):
        info = {}  # 각 위치에 대한 미생물 군집 정보를 담을 딕셔너리 초기화

        # 모든 미생물 군집에 대해 처리
        for i in range(K):
            x, y, cnt, way = temp[i]
            nx = x + ways[way][0]  # 다음 위치 계산
            ny = y + ways[way][1]

            temp[i][0], temp[i][1] = nx, ny  # 미생물 군집의 위치 갱신

            # 만약 다음 위치가 배열의 경계에 닿았을 경우
            if nx in [0, N - 1] or ny in [0, N - 1]:
                # 방향 변경 및 미생물 수 감소
                if way <= 2: way = 3 - way
                elif way <= 4: way = 7 - way
                cnt //= 2
                temp[i][2],temp[i][3] = cnt, way

            # info 딕셔너리에 해당 위치의 미생물 군집 정보 추가
            if (nx, ny) not in info.keys():
                info[(nx, ny)] = [i, cnt]
            else:
                num, max_cnt = info[(nx, ny)]
                # 미생물 수가 더 많은 군집이 이미 있을 경우
                if temp[i][2] > max_cnt:
                    info[(nx, ny)] = [i, cnt]  # 현재 군집 정보 갱신
                    temp[i][2] += temp[num][2]  # 더 많은 미생물 수를 가진 군집의 미생물 수 추가
                    temp[num][2] = 0  # 원래 군집의 미생물 수 초기화
                else:
                    temp[num][2] += temp[i][2]  # 이미 있는 군집에 미생물 수 추가
                    temp[i][2] = 0  # 현재 군집의 미생물 수 초기화

    # 결과 계산
    result = 0
    for i in range(len(temp)):
        result += temp[i][2]

    # 결과 출력
    print(f'#{tc} {result}')
```

#### 🖌 백준 5648 원자 소멸 시뮬레이션
> 전형적인 시뮬레이션 문제. 
> 1. 0.5초일 때도 감안해야 하므로, 전체 판의 길이를 두배로 확장한다.
> 2. atoms에 원자들의 정보를 담는다(방향과 에너지) 
> 3. 델타탐색을 이용하여 atoms의 원자를 이동시킨다.
> 4. pos에 atom이 있으면 그 위치에 atom을 저장한다.
> 5. 만약 pos의 키값이 주어진 범위를 벗어나면 제거한다.
> 6. 두 개 이상 pos에 저장되면 결과값에 양측 에너지를 저장한다.
```python
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
 
for tc in range(int(input())):
    atoms = []
    for _ in range(int(input())):
        x, y, d, e = map(int, input().split())
        atoms.append([2*x, 2*y, d, e])
    ans = 0

    # 시간 경과
    while len(atoms) > 1:
        pos = {}
        # 위치 이동
        for atom in atoms:
            atom[0] += dx[atom[2]]
            atom[1] += dy[atom[2]]
            # 위치 저장
            if (atom[0], atom[1]) in pos: pos[(atom[0], atom[1])].append(atom)
            else:  pos[(atom[0], atom[1])] = [atom]

        for key, value in pos.items():
            # 배열 이탈
            if not (-2001 < key[0] < 2001 and -2001 < key[1] < 2001):
                atoms.remove(value.pop())
            # 충돌 소멸
            elif len(value) > 1:
                for atom in value:
                    ans += atom[3]
                    atoms.remove(atom)
 
    print(f'#{tc+1}', ans)
``` 

#### 🎙 백준 5650 핀볼게임
> 시뮬레이션 문제
> 1. block : 블록이 위치하면 방향을 전환하는 딕셔너리
> 2. finds_hole : 웜홀 위치를 찾는 함수(키값 6~10 사이에 위치정보 담음)
> 3. DFS : 아래 조건을 충족하는 경우 누적된 cnt 반환
>   - 처음 x,y위치로 돌아오는 경우
>   - 블록이나 벽에 닿는 경우 (이때는 누적된 cnt가 아닌 2*cnt-1)
>   - 블랙홀을 만나는 경우
> 4. 핀볼 판에 값이 0인 경우에만 본 DFS를 실행

```python

# 블록의 방향을 저장한 딕셔너리
block = {1:{1:0,2:3},2:{2:1,3:0},3:{0:1,3:2},4:{0:3,1:2},5:{}}
# 상하좌우 이동을 위한 방향 리스트
dr = [(0,1),(1,0),(0,-1),(-1,0)]

# 웜홀 위치를 찾는 함수
def finds_hole(arr):
    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if 6 <= idx <= 10:
                worm_hole[idx].add((i,j))

# 핀볼 이동을 위한 DFS 함수
def DFS(x,y,dir):
    cnt = 0
    original_x, original_y = x,y
    while 1:
        nx = x + dr[dir][0]
        ny = y + dr[dir][1]
        if [original_x,original_y] == [nx,ny]:  # 처음 출발한 위치로 돌아온 경우
            return cnt
        if not (0<= nx < N and 0<= ny < N) or arr[nx][ny]==5:  # 범위를 벗어나거나 블랙홀인 경우
            cnt += 1
            return 2*cnt-1
        else:
            if arr[nx][ny] == -1:  # 블럭의 끝에 도달한 경우
                return cnt
            elif arr[nx][ny] == 0:  # 빈 공간으로 이동한 경우
                x, y= nx, ny
            elif 1 <= arr[nx][ny] <= 4:  # 블록을 만난 경우
                dir = block[arr[nx][ny]].get(dir)
                cnt += 1
                if dir == None:  # 블록의 방향 변환을 할 수 없는 경우
                    return cnt*2-1
                x,y = nx,ny
            elif 6 <= arr[nx][ny] <= 10:  # 웜홀을 만난 경우
                x,y = list(worm_hole[arr[nx][ny]]-{(nx,ny)})[0]
    return cnt

for tc in range(1,int(input())+1):
    N = int(input())  # 보드의 크기 N을 입력받음
    arr = [list(map(int,input().split())) for _ in range(N)]  # N*N 보드의 정보를 입력받음
    worm_hole = {i: set() for i in range(6, 11)}  # 웜홀의 위치를 저장하기 위한 딕셔너리 초기화
    finds_hole(arr)  # 웜홀의 위치를 찾는 함수 호출
    max_val = 0  # 최대 점수 초기화
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==0:  # 빈 공간일 경우에만 핀볼 이동을 시작함
                for k in range(4):  # 상하좌우 방향으로 이동을 시작함
                    max_val = max(max_val,DFS(i,j,k))  # 최대 점수를 업데이트함
    print(f"#{tc} {max_val}")  # 결과 출력
```