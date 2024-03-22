# # 완탐? 백트?
# # 1 : 오른쪽에서 온 경우 위로 90도 나머지 180도     if dr == 0 : dr = 3 else : dr = (dr+2)%4
# # 2 : 오른쪽에서 온 경우 아래로 90도 나머지 180도   if dr == 0 : dr = 1 else : dr = (dr+2)%4

# # 3 : 왼쪽에서 온 경우 아래로 90도 나머지 180도 if dr == 2  : dr = 1 else : dr = (dr+2)%4
# # 4 : 왼쪽에서 온 경우 위로 90도 나머지 180도   if dr == 2 : dr = 3 else : dr = (dr+2)%4

# # 5 : 방향 180도 

# # 6 ~ 10 : 웜홀 (반대 방향으로)
# # -1 : 블랙홀 (종료조건)
# # 출발지 귀환도 종료조건
# # 벽에 부딪히면 반대로 돌아감

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# for tc in range(int(input())):
#     N = int(input())
#     games = []
#     hole = {}
#     for idx in range(N):
#         game = list(map(int,input().split()))
#         # 웜홀의 경우 미리 리스트에 담아두기
#         for x in range(6,11):
#             for y in range(N):
#                 if game[y] == x :
#                     hole[x] = hole.setdefault(x,[]) + [[idx,y]]
#         games.append(game)

#     ans = 0
#     for i in range(N):
#         for j in range(N):
#             if games[i][j] == 0 :
#             # 시작
#                 for dr in range(4): # 방향마다 순회
#                     di,dj = i,j
#                     tmp = 0
#                     while True:    # 종료조건 1) 출발지로 귀환 2) 블랙홀
#                         di += dx[dr]
#                         dj += dy[dr]
                    
#                         if not (0 <= di< N and 0 <= dj < N) :
#                             dr = (dr+2)%4                               # 반대방향으로
#                             di += dx[dr]
#                             dj += dy[dr]
#                         # 벽 조건
#                         if 1 <= games[di][dj] <= 5 :
#                             if games[di][dj] == 1 :
#                                 if dr == 0:
#                                     dr = 3
#                                     if di == 0 :
#                                         dr = 2
#                                         dj += 1
#                                         tmp+=1
#                                 elif dr == 1:
#                                     dr = 0
#                                     if dj == N-1 :
#                                         dr = 3
#                                         di -= 1
#                                         tmp+=1
#                                 else :
#                                     dr = (dr+2)%4
#                                 tmp += 1
#                             if games[di][dj] == 2 :
#                                 if dr == 0:
#                                     dr = 1
#                                     if di == N-1 :
#                                         dr = 2
#                                         dj += 1
#                                         tmp+=2                                    
#                                 elif dr == 1:
#                                     dr = 0
#                                     if dj == N-1 :
#                                         dr = 1
#                                         di += 1
#                                         tmp+=2
#                                 else :
#                                     dr = (dr+2)%4
#                                 tmp += 2
#                             if games[di][dj] == 3 :
#                                 if dr == 2:
#                                     dr = 1
#                                     if di == N-1 :
#                                         dr = 2
#                                         dj += 1
#                                         tmp+=2                                     
#                                 elif dr == 1:
#                                     dr = 2
#                                 else :
#                                     dr = (dr+2)%4
#                                 tmp += 3
#                             if games[di][dj] == 4 :
#                                 if dr == 2:
#                                     dr = 3
#                                 elif dr == 3:
#                                     dr = 2
#                                 else :
#                                     dr = (dr+2)%4
#                                 tmp += 4
#                             if games[di][dj] == 5 :
#                                 dr = (dr+2)%4
#                                 tmp += 5

#                         if games[di][dj] > 5 :      # 웜홀 조건
#                             for item in hole[games[di][dj]]:
#                                 if [di,dj] != item :
#                                     di,dj = item[0],item[1]

#                         if (di,dj) == (i,j) or games[di][dj] == -1:
#                             break
#                     ans = max(tmp,ans)
#     print(ans)

# 터짐