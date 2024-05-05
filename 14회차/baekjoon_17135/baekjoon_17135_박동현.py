from collections import deque

def find(i,j):

    result = [(i,j)]
    q = deque([(i,j)])
    visit = [[0] * M for _ in range(N)]
    # 여기 부분 수정하면 끝
    if not castle[i][j] :
        while q :
            i,j = q.popleft()

            for dt in range(3):
                di = i + dx[dt]
                dj = j + dy[dt]
                if 0 <= di < N and 0 <= dj < M :
                    visit[di][dj] = visit[i][j] + 1
                    if visit[di][dj] == D :
                        break
                    if castle[di][dj] :
                        result.append((di,dj))
                        break
                    q.append([di,dj])

    return result



dx = [0,-1,0]
dy = [-1,0,1]

N,M,D = map(int,input().split())
# N 세로 M 가로 D 사정거리

temp = [list(map(int,input().split())) for _ in range(N)]

ans = 0 
# 완탐
for a in range(M-2) :
    for b in range(a+1,M-1):
        for c in range(b+1,M):
            cnt = 0
            # a b c  = 궁수 1 2 3
            castle = [row[:] for row in temp]

            for i in range(N-1,-1,-1):
                # 왜 세트 ? (55)
                tmp = set()
                for l in (a,b,c) :
                    # 각 궁수들의 사정거리 내 적을 찾기
                    targets = find(i,l)     
                    
                    for x,y in targets:

                        if castle[x][y] == 1 :
                            # 같은 적이 여러 궁수에게 공격당할 수 있다
                            tmp.add((x,y))
                            break
                # 세트에 담긴 적들 제거
                for x,y in tmp:
                    castle[x][y] = 0
                    cnt += 1
            # 탐색 종료 시 max값 비교 
            ans = max(ans,cnt)
print(ans)