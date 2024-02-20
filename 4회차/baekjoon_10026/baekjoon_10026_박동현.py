from collections import deque

t = int(input()) # 그림의 크기를 받음

pic = [list(input()) for _ in range(t)]


# 1) 일반인이 보는 경우
#### RG : 1, B: 2로 바꾸고, 적록색약 기준으로 새롭게 재편

dil = [1,0,-1,0]
djl = [0,1,0,-1]

pic_lst = ["R","G","B"]
normal_cnt = 0
visit = [[0 for _ in range(t+1)] for _ in range(t+1)]

for pix in pic_lst:                 # R,G,B 마다 한번씩 순회하면서 탐색
    for i in range(t) :             # i,j 로 2차원 전체를 탐색하면서 리스트를 변조
        for j in range(t) :
            if pic[i][j] == pix:    # i,j 에서 R,G,B 중 한 값을 찾았을 때 시작
                start = [i,j]
                q = deque()
                q.append(start)

                while q :                       # BFS를 시행하면서
                    ti, tj = q.popleft()
                    if pic[ti][tj] == pix :
                        visit[ti][tj] = 1
                        if pix in "RG":         # R 또는 G 인 경우 1로
                            pic[ti][tj] = 1
                        else :                  # B 인 경우 2로 리스트를 바꾸고
                            pic[ti][tj] = 2

                    for idx in range(4) :       # 델타 탐색을 하며 추가적으로 탐색
                        di = ti + dil[idx]
                        dj = tj + djl[idx]
                        if 0 <= di < t and 0 <= dj < t :
                            if pic[di][dj] == pix and visit[di][dj] == 0 :
                                if pix in "RG":
                                    pic[di][dj] = 1
                                else :
                                    pic[di][dj] = 2
                                q.append([di,dj])                  
                
                normal_cnt += 1                 # 하나를 찾았다는 것이 한 스팟을 찾고, 이어진 지역을 모두 탐색했다는 뜻이므로 한 구역을 전부 탐색한 것

# 2) 색약이 보는 경우

abnormal_cnt = 0

visit = [[0 for _ in range(t+1)] for _ in range(t+1)]       # 새로 visit를 짜고 

for modi_pix in range(1,3):                 # 이제 1 또는 2의 경우만 발생
    for i in range(t) :                     # 위와 같이 전역 탐색하는 방식
        for j in range(t) :
            if pic[i][j] == modi_pix:
                start = [i,j]
                q = deque()
                q.append(start)

                while q :
                    ti, tj = q.popleft()
                    if pic[ti][tj] != 0 and pic[ti][tj] == modi_pix :
                        visit[ti][tj] = 1
                    for idx in range(4) :
                        di = ti + dil[idx]
                        dj = tj + djl[idx]
                        if 0 <= di < t and 0 <= dj < t :
                            if pic[di][dj] == modi_pix and visit[di][dj] == 0 :
                                pic[di][dj] = 0
                                q.append([di,dj])
            
                abnormal_cnt += 1

print(normal_cnt, abnormal_cnt)
# 함수 선언할"껄" 34164kb / 108ms