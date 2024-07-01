import sys
input = sys.stdin.readline  # 입력 시간을 줄이기 위해 sys.stdin.readline 사용

def dfs(row, col, memo, cnt):
    global max_  # 전역 변수 max_를 함수 내에서 사용

    max_ = max(max_, cnt)  # 최대 길이 업데이트

    # 상하좌우 이동
    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]

        # 범위를 벗어나거나 이미 방문한 알파벳인 경우에는 건너뜀
        if not (0 <= nrow < R and 0 <= ncol < C) or list_[nrow][ncol] in memo:
            continue
        dfs(nrow, ncol, memo + list_[nrow][ncol], cnt + 1)

R, C = map(int, input().split())  # 보드의 크기 입력
list_ = [list(input()) for _ in range(R)]  # 보드 입력
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]  # 상하좌우 이동에 대한 변화량
max_ = 0  # 최대 길이 초기화
dfs(0, 0, list_[0][0], 1)  # DFS 탐색 시작
print(max_)  # 결과 출력
