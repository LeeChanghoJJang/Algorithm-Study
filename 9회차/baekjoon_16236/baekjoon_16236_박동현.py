from collections import deque
dx = [-1 , 0 , 0 , 1]
dy = [ 0, -1 , 1 , 0]
N = int(input())

# 리스트 받으면서 상어 위치 찾기
seas = []
for i in range(N):
    tmp = list(map(int,input().split()))
    if 9 in tmp :
        start = (i,tmp.index(9))
    seas.append(tmp)
# 아기 상어 키우기
lv = 2 
exp = 0

cnt = 0 
q = deque([start])

while q :
    visit = [[-1]*N for _ in range(N)]  # visit
    x,y = q[0][0], q[0][1]              # 시작점 설정
    visit[x][y] = 0                     # visit 변경
    seas[x][y] = -1                     # -1 이 seas에서 아기상어의 현재 위치
    food_legth=0                        
    food = []                           # 밥통
    # BFS
    while q :
        i,j = q.popleft()

        for dt in range(4):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < N and 0 <= dj < N:
                if visit[di][dj] == -1 and seas[di][dj] <= lv:
                    visit[di][dj] = visit[i][j] + 1
                    # 지금 밥이 없다면
                    if not food :
                        # 밥 거리 저장
                        food_length = visit[di][dj]
                        # q 에 넣어두기
                        q.append((di,dj))
                    # 먹을 것 발견 시 (밥거리랑 저장된거랑 같은지 비교 (사실 필요없어보이는데 한 부분에서 오류나서 넣어봄))
                    if 0 < seas[di][dj] < lv and food_length == visit[di][dj]:
                        # 밥
                        food.append((di,dj))
    # 밥이 있으면
    if food :
        # 밥 sort
        food.sort()
        # 맨 앞 좌표가 가장 짧고, 가장 위의, 가장 왼쪽의 밥
        di,dj = food[0][0], food[0][1]
        # 먹이 0 으로 변경
        seas[di][dj] = 0
        # 경험치 +1 
        exp += 1
        # di,dj를 시작점으로 q 새로 생성
        q = deque([(di,dj)])
        # 이동거리 cnt에 저장
        cnt += visit[di][dj]
        # 레벨업 확인
        if lv == exp :
            lv += 1
            exp = 0 
        # pprint(seas)
        # pprint(visit)
        # print('cnt:',cnt, ",lv:", lv, ",exp:", exp)

print(cnt)