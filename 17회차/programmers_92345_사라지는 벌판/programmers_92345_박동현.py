n,m = 0,0
move = [(0,1),(0,-1),(1,0),(-1,0)]
visit = [[0]*5 for _ in range(5)]
def OOB(x,y):
    return x < 0 or x >= n or y < 0 or y >= m

# 결과값이 
def play(board,curx,cury,opx,opy):
    global visit
    if visit[curx][cury]: return 0
    canWin = 0
    for mov in move:
        dx, dy = mov
        nx, ny = curx + dx, cury + dy
        if OOB(nx,ny) or visit[nx][ny] or board[nx][ny] == 0 : continue
        # 방문처리
        visit[curx][cury] = 1
        opResult = play(board,opx,opy,nx,ny)+1
        # 방문처리 끝
        visit[curx][cury] = 0

        # 현재 저장된 값 패배인데 상대가 졌다고 하면 이기는 경우로 저장
        if canWin % 2 == 0 and opResult % 2 == 1 : canWin = opResult
        # 현재 저장된 값 패배인데 상대가 이겼다고 하면 최대한 늦게 지는 횟수 선택
        elif canWin % 2 == 0 and opResult % 2 == 0 : canWin = max(canWin,opResult)
        # 현재 저장된 값 승리인데 상대가 졌다고 하면 최대한 빨리 이기는 횟수 선택
        elif canWin % 2 == 1 and opResult % 2 == 1 : canWin = min(canWin,opResult)
    return canWin

def solution(board, aloc, bloc):
    global n,m
    n, m = len(board), len(board[0])
    return play(board,aloc[0],aloc[1],bloc[0],bloc[1])