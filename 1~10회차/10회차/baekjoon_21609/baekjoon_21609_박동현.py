from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())

block = [list(map(int, input().split())) for _ in range(N)]

ans = 0
## 큰 블록 찾는 과정 (tmp : 큰 블록, max_value : 점수 합)

while True :
    max_value = 0
    max_zero = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if block[i][j] != "" and block[i][j] > 0 and not visit[i][j] :
                q = deque([(i,j)])
                cnt = 0
                zero = 0
                while q :
                    x,y = q.popleft()
                    for dt in range(4):
                        di = x + dx[dt]
                        dj = y + dy[dt]
                        if 0 <= di < N and 0 <= dj < N :
                            if not visit[di][dj] :
                                if block[i][j] == block[di][dj] or block[di][dj] == 0:
                                    visit[di][dj] = 1
                                    q.append((di,dj))
                                    cnt += 1
                                    if block[di][dj] == 0 :
                                        zero += 1
                for a in range(N):
                    for b in range(N):
                        if block[a][b] == 0 :
                            visit[a][b] = 0                                     

                if cnt > max_value :
                    max_value = cnt
                    tmp = (i,j)
                    max_zero = zero

                elif cnt == max_value and zero >= max_zero :
                    max_value = cnt
                    tmp = (i,j)
                    max_zero = zero
                
    if max_value > 1 :
        ans += max_value **2
    else :
        break
    # 블록 제거하기
    i,j = tmp
    q = deque([tmp])
    col = block[i][j]
    block[i][j] = ""
    while q :
        i , j = q.popleft()
        for dt in range(4):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < N and 0 <= dj < N :
                if block[di][dj] == 0 or block[di][dj] == col :
                    block[di][dj] = ""
                    q.append((di,dj))

    # 중력 작용하기
    temp = 0
    for c in range(N):
        for r in range(N - 1, -1, -1):
            # 아래 블록
            cur_r = r
            while cur_r > 0 and block[cur_r][c] == "":
                cur_r -= 1
            if cur_r != r and block[cur_r][c] != -1:
                temp = block[cur_r][c]
                block[cur_r][c] = ""
                block[r][c] = temp


    # 뒤집기
    block = [list(char) for char in zip(*block)][::-1]


    temp = 0
    for c in range(N):
        for r in range(N - 1, -1, -1):
            # 아래 블록
            cur_r = r
            while cur_r > 0 and block[cur_r][c] == "":
                cur_r -= 1
            if cur_r != r and block[cur_r][c] != -1:
                temp = block[cur_r][c]
                block[cur_r][c] = ""
                block[r][c] = temp
    
print(ans)