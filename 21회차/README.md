## Algorithm Study 20회차 회의 (24.6.29.) 

### 💬 회의개요
    가. 금일 일정 
        - 시간 : 7월 6일 토요일 오후 7시  
        - 방식 : 디스코드

    나. 차주 예정 일정
        - 시간 : 7월 14일 일요일 오후 7시  
        - 방식 : 송삼 2층 회의실

    다. 변경사항
        1. 문제선정 : 인당 각 1문제 (총 7문제, 변동없음)
        2. 문제 브리핑 방식 변경 
            - ① 본인이 선정한 문제 파이썬으로 라이브 코딩(단, 이경우 추가로 자바로 브리핑해도 됨)
            - ② 본인이 선정한 문제 외에도 다른 사람이 선정한 문제 하나 더 브리핑 예정이며, 그 추가 문제 선정 방식은 자기 "앞"에 있는 사람이 선정한 문제로 정하여 추가로 브리핑 
            - 순서 : 임경태 - 이권민 - 이창호 - 이상현 - 최지우 - 윤예리 - 박동현 (순서는 매번 랜덤으로 변경 예정) 
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

### 🤢 문제 선정
   ###### 1. 창호
    - 백준 12015 가장 긴 증가하는 부분 수열2(골2)
   ###### 2. 예리
    - 백준 2096 내려가기(골 5)
   ###### 3. 경태
    - 백준 14462 소가 길을 건너간 이유 8 (골3)
   ###### 4. 동현
    - 백준 2023 신기한 소수(골5)
   ###### 5. 상현
    - 백준 29703 펭귄의 하루(골4)
   ###### 6. 지우
    - 백준 13549 숨바꼭질3(골5)
   ###### 7. 권민
    - 없음
    
### 🏅 스터디 내용 
#### 🎈 백준 1423 말이 되고픈 원숭이
> 1. `동적 계획법`을 이용하여 최대한 힘의 최댓값을 구하기
> 2. dp : 해당 훈련일자에 해당되는 힘의 변동분값
> 3. 현재 캐릭터별 힘의 값 + 힘의 변동분 => 총 힘의 값 도출
> 4. 점화식 
>   - dp[k + j - i] = 기존 j일에 레벨 변동분이 저장된 dp값. 즉 레벨변동분과 훈련일수의 합이 같을 때, 가장 큰값을 저장하기 위함
>   - dp[j] + q[k] - q[i] = 기존 j일에 해당되는 값에 현재의 힘의 변동분 

```python
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
p =list(map(int,input().split()))
q =list(map(int,input().split()))
d = int(input())

dp = [0] * 101

now = 0
for i in range(n):
    now += p[i] * q[i]
    p[i] = min(d,p[i])

for i in range(n):
    while p[i] > 0 :
        p[i]-=1
        for j in range(d,-1,-1):
            for k in range(i+1,n):
                if k + j- i <= d:
                    dp[k + j - i] = max(dp[k + j - i], dp[j] + q[k] - q[i])
print(dp[d] + r)


```
#### 🧰 백준 3190 뱀
> 1. 사과는 2로 나머지는 0으로, 이동한 곳이면 1로 저장한다.
> 2. 주어진 방향을 통해 게임을 진행한다.
>   - 이동칸에 사과가 있다면, 사과는 없어지고, 꼬리는 움직이지 않는다.
>   - 이동칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 몸길이는 변치 않는다. 

```python
from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:
        break

print(cnt)

```

#### ⚽ 백준 14938 서강그라운드
> 1. `다익스트라` 를 통해 각 출발지점부터 도착지점들까지 최소 비용을 저장한다.
> 2. 탐색범위 이내인 경우에만 아이템을 획득한다.
> 3. 가장 큰 경우를 출력한다.

```python
import sys
import heapq

def Dijkstra(start):
    dp = [100 for _ in range(n + 1)]
    INF = int(1e9)
    dp[start]=0
    heapq.heappush(heap,(start,0))
    while heap:
        now, wei  = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        for next, cost in graph[now]:
            next_cost = cost + wei
            if next_cost < dp[next]:
                dp[next] = next_cost
                heapq.heappush(heap,(next,next_cost))
    return dp

n, m, r =map(int,sys.stdin.readline().split())
t = dict(enumerate(map(int,sys.stdin.readline().split()),start=1))
heap = []
graph = [[] for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int,sys.stdin.readline().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

max_val = 0
for i in range(1,n+1):
    distances = Dijkstra(i)
    ans = 0
    for j in range(1,n+1):
        if distances[j] <= m:
            ans += t[j]
    if max_val < ans:
        max_val = ans
print(max_val)

```

#### 🖌 백준 16724 피리부는 사나이
> 1. 어디든 놓아도 갈 수 있는 세이프티존이 있다는 건 유니온 - 파인드처럼 대표 노드가 있다는 것과 같음
> 2. 이 과정을 `dfs`를 통해 몇 무리가 있는지 파악할 것임
> 3. 다른 무리일 때마다 다른 인덱스번호를 저장하여, 몇개의 무리가 도출되는지 확인

```python
import sys
input =sys.stdin.readline
def dfs(i,j,c):
    global r
    if visit[i][j] != -1:
        if visit[i][j] == c: r+=1
        return
    visit[i][j] = c
    dir = direction.index(Map[i][j])
    dfs(i+dx[dir],j+dy[dir],c)

n,m = map(int,input().split())
Map = [list(input()) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]
direction = ['L','R','U','D'] # (0,-1), (0,1), (-1,0), (1,0)
dx,dy = [0,0,-1,1],[-1,1,0,0]

r,c = 0,0
for i in range(n):
    for j in range(m):
        dfs(i,j,c)
        c+=1
print(r)
``` 

#### 🎙 백준 17144 미세먼지 안녕
> 1. 청정기의 위치를 찾아서 vac에 저장
> 2. 확산 함수를 만들고, 공기청정기가 아니면 사방으로 확산
> 3. 업과 다운함수를 통해 각 미세먼지를 이동시킨다. 만약 모서리에 닿으면 방향을 전환하고, 청정기에 도달하면 끝난다.

```python
import sys
sys.stdin = open('input.txt')
r, c, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
input =sys.stdin.readline
vac = []
for i in range(r):
    if maps[i][0] == -1:
        vac.append(i)       # 청정기의 위치를 찾음


def spread(maps, sp_maps):      # 먼지 분산
    for i in range(r):
        for j in range(c):
            if maps[i][j] != -1 and maps[i][j] > 0:
                sp_dust = maps[i][j] // 5
                for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] != -1:
                        sp_maps[ny][nx] += sp_dust
                        maps[i][j] -= sp_dust
                sp_maps[i][j] += maps[i][j]

    return sp_maps      # 새로운 맵에 넣음


def up():       # 위쪽 바람
    dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
    dir = 0
    before = 0      # 이전 값을 저장
    y, x = vac[0], 1        # 바로 오른쪽부터 시작
    while True:
        ny, nx = y + dy[dir], x + dx[dir]       # 움직임
        if y == vac[0] and x == 0:
            maps[y][x] = 0      # 만약 청정기에 도달하면 0으로 만들고 끝냄
            break
        if not (0 <= ny < r and 0 <= nx < c):       # 모서리에 도달하면 방향을 전환함
            dir += 1
            continue
        maps[y][x], before = before, maps[y][x]     # 현재 값을 저장하고, 이전 값을 현재 위치에 넣음
        y, x = ny, nx


def down():     # 아래쪽 바람
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    dir = 0
    before = 0
    y, x = vac[1], 1
    while True:
        ny, nx = y + dy[dir], x + dx[dir]
        if y == vac[1] and x == 0:
            maps[y][x] = 0
            break
        if not(0 <= ny < r and 0 <= nx < c):
            dir += 1
            continue
        maps[y][x], before = before, maps[y][x]
        y, x = ny, nx

def count(maps):
    sum = 0
    for i in range(r):
        for j in range(c):
            sum += maps[i][j]
    return sum

for _ in range(t):
    maps = spread(maps, [[0] * c for _ in range(r)])
    up()
    down()
print(count(maps))

```

#### 👔 프로그래머스 1829 카카오프렌즈 컬러링북
> 1. `search` 함수 : 같은 컬러인 경우에만 계속해서 탐색하는 `bfs`함수
> 2. 방문하지 않거나, 0이 아닌겨우만 탐색한다.

```java
import java.util.*;

class Solution {
    static boolean[][] visit;
    static int[][] map;
    static List<Integer> list;
    static int N, M;
    public int[] solution(int m, int n, int[][] picture) {
        N = n;
        M = m;
        map = picture;
        list = new ArrayList();
        visit = new boolean[m][n];

        for(int i = 0 ; i < m; ++i){
            for(int j = 0 ; j < n; ++j){
                if(!visit[i][j] && map[i][j] != 0){
                    search(i,j);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = list.size();
        answer[1] = list.stream().max(Integer::compare).get();

        return answer;
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public void search(int startX, int startY){
        int count = 1;
        visit[startX][startY] = true;
        Queue<int[]> q = new ArrayDeque();
        q.add(new int[] {startX, startY});
        while(!q.isEmpty()){
            int[] cur = q.poll();
            for(int d = 0; d < 4; ++d){
                int nextX = cur[0] + dx[d];
                int nextY = cur[1] + dy[d];
                if(0 <= nextX && nextX < M && 0 <= nextY && nextY < N){
                    if(!visit[nextX][nextY] && map[nextX][nextY] == map[startX][startY]){
                        visit[nextX][nextY] = true;
                        q.add(new int[] {nextX, nextY});
                        count++;
                    }
                }
            }
        }
        list.add(count);
    }
}
```

#### ❤️‍🔥 프로그래머스 250136 석유시추
> 1. 각 영역들을 같은 무리들끼리 같은 숫자로 저장한다.
> 2. 각 영역의 크기를 딕셔너리에 해당 키에 저장한다.
> 3. 석유 시추를 위해 각 열에서 시추관을 꼽는다.
> 4. 각 행에 해당 번호가 저장되어 있으면 그 영역을 더해주며, 최댓값을 갱신한다.

```py
from collections import deque

def solution(land):
    n,m = len(land), len(land[0])
    locations = dict({0:0})
    dr = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = [[False] * m for _ in range(n)]
    idx = 1

    def bfs(i,j,idx):
        cnt = 1
        queue = deque([[i,j]])
        land[i][j]=idx
        visited[i][j]=True
        while queue:
            x,y = queue.popleft()
            for j in range(4):
                nx = x + dr[j][0]
                ny = y + dr[j][1]
                if 0<= nx < n and 0<= ny < m and not visited[nx][ny] and land[nx][ny]==1:
                    visited[nx][ny] = True
                    land[nx][ny]=idx
                    queue.append((nx,ny))
                    cnt+=1
        return cnt

    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and not visited[i][j]:
                locations[idx] = bfs(i,j,idx)
                idx+=1
    result = 0
    for i in range(m):
        temp =set()
        for j in range(n):
            temp.add(land[j][i])
        result = max(result,sum(map(lambda x : locations[x], temp)))

    return result



```
