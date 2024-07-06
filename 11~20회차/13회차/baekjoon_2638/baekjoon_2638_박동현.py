# 1. 판의 가장자리는 치즈가 없다
# 2. 0,0 좌표를 기준으로 바깥을 구분할 수 있다.
# 3. 바깥을 -1로 바꾸고, -1과 1이 만나는 경우 없애는 방향으로 진행한다.

# -1 : 바깥 // 0 : 구멍 // 1 : 치즈 // 만나는 경우 : 2 (임시값)
from collections import deque


dr = (0,1),(1,0),(-1,0),(0,-1)

N,M = map(int,input().split()) # N : 세로 M : 가로
table = [ [*map(int,input().split())] for _ in range(N) ]

# 바깥 구분하기
q = deque([(0,0)])
while q :
    i,j = q.popleft()

    for dx,dy in dr:
        di,dj = i+dx, j+dy
        if 0 <= di < N and 0 <= dj < M and table[di][dj] == 0 :
            table[di][dj] = -1
            q.append((di,dj))

ans = 0 
while True : 
    tmp = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == 1:
                tmp += 1
    if tmp == 0 :
        print(ans)
        exit()
    ans+=1
# 치즈 녹이기
    for i in range(N):
        for j in range(M):
            if table[i][j] == 1 :
                # 노출도
                exp = 0 
                for dx,dy in dr :
                    di, dj = i+dx, j+dy
                    if 0 <= di < N and 0 <= dj < M and table[di][dj] == -1 :
                        exp += 1
                # 치즈가 2 칸 이상 공기에 노출되어 있으면 
                if exp > 1 :
                    table[i][j] = 2
                        
    # 녹은 치즈 처리하기
    for i in range(N):
        for j in range(M):
            if table[i][j] == 2:
                table[i][j] = -1

    # 구멍에 공기 통하는지 확인
    for i in range(N):
        for j in range(M):
            if table[i][j] == 0 :
                for dx,dy in dr :
                    di,dj = i + dx, j + dy
                    if 0 <= di < N  and 0 <= dj < M and table[di][dj] == -1:
                        table[i][j] = -1
                        q = deque([(i,j)])
                        while q :
                            x,y = q.popleft()
                            for dx,dy in dr:
                                di, dj = x+dx, y+dy
                                if 0 <= di < N and 0 <= dj < M and table[di][dj]==0:
                                    table[di][dj] = -1
                                    q.append((di,dj))
