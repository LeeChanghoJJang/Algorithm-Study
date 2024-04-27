sero,garo,t= map(int,input().split()) # 세로, 가로, 테케

test_list = [[0 for _ in range(garo)] for _ in range(sero)]

# 테스트 리스트 색칠하기
for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    for idx in range(y1, y2):
        for jdx in range(x1, x2):
            test_list[idx][jdx] = 1

# 결과 담을 리스트 (len과 요소로 정답 추출)
result = []

# 델타 탐색
di = [0,1,0,-1]
dj = [1,0,-1,0]

# DFS 비슷한거 실행
for i in range(sero):                                               # 리스트 전역을 순회하면서
    for j in range(garo):                                           # 1. 0인 부분을 찾고
        if test_list[i][j] == 0:                                    # 2. 근처의 모든 0을 1로 바꾼다.
            stack = [(i,j)]                                         # 끊기는 부분마다 (while 탐색 종료 시점) 리스트에 크기를 담는다.
            count = 0

            while stack :
                tc = stack.pop()
                if test_list[tc[0]][tc[1]] == 0:                    # 0을 찾은 경우, 그 값을 1로 바꾸고 count를 하나 올린다.
                    test_list[tc[0]][tc[1]] = 1
                    count += 1

                for dlt in range(4):                                # 델타 탐색을 통해 주변의 0을 검색한다.
                    dlt_i = tc[0]+di[dlt]
                    dlt_j = tc[1]+dj[dlt]
                    
                    if 0<= dlt_i < sero and 0<= dlt_j < garo:
                        if test_list[dlt_i][dlt_j] == 0 :
                            stack.append((dlt_i,dlt_j))             # tc 주변 4방향의 점을 순회하며 0인 경우 stack에 튜플로 담아 while 탐색을 반복한다.
            else :
                result.append(count)
result.sort()
print(len(result))                                                  
print(*result)