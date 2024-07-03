import sys

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
rx = [1,0,-1,0]
ry = [0,1,0,-1]


R,C,T = map(int,input().split())                            # R : 세로 C : 가로 T : 시간

cleaner = []                                                # cleaner : 공청기 위치

room = []                                                   # room : 집
for idx in range(R):
    rom = list(map(int,input().split()))
    room.append(rom)
    if rom[0] == -1 :                                       # 공청기 위치 찾는 시퀀스
        cleaner.append((idx,0))

# 여기부터 while 문
## 확산
        
cnt = 0 
while cnt != T :
    dust = []                                               # 먼지 위치
    for i in range(R):
        for j in range(C):

            if room[i][j] :
                dust.append((i,j,int(room[i][j]/5)))        # i,j 좌표값과 확산되는 값 같이 저장


    for i,j,k in dust:                                      # 먼지 위치를 순회하면서

        for dt in range(4):                                 # 델타 탐색을 하고
            di = i + dx[dt]
            dj = j + dy[dt]
                                                            # 위치에 갈 수 있다면 (리스트 범위를 벗어나지 않고 공청기 칸으로 가지 않고)
            
            if 0 <= di < R and 0<= dj < C and room[di][dj] != -1 :
                room[di][dj] += k                           # 확
                room[i][j] -= k                             # 산

    ## 바람
    upper, under = cleaner                                  # upper : 공청기 윗칸  under : 공청기 아래칸

    x,y,dr = *upper,0

    while dr != 4 :                                         # upper 부분 조작
        if 0 <= x+dx[dr] <= upper[0] and 0 <= y+dy[dr] < C:
            if room[x][y] == -1 :
                room[x+dx[dr]][y+dy[dr]] = 0

            else :
                if room[x+dx[dr]][y+dy[dr]] == -1 :
                    room[x][y] = 0 

                else :
                    room[x][y] = room[x+dx[dr]][y+dy[dr]]

            x += dx[dr]
            y += dy[dr]

        else :
            dr += 1
        
    p,q,rr = *under,0

    while rr != 4 :                                         # under 부분 조작
        if under[0] <= p+rx[rr] < R and 0 <= q+ry[rr] < C:
            if room[p][q] == -1 :
                room[p+rx[rr]][q+ry[rr]] = 0

            else :
                if room[p+rx[rr]][q+ry[rr]] == -1 :
                    room[p][q] = 0 

                else :
                    room[p][q] = room[p+rx[rr]][q+ry[rr]]

            p += rx[rr]
            q += ry[rr]

        else :
            rr += 1
    cnt +=1

# 출력
ans =0 
for rom in room:
    ans += sum(rom)
print(ans+2)