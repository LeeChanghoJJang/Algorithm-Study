import sys
input = sys.stdin.readline  # 입력 시간을 줄이기 위해 sys.stdin.readline 사용

def dfs(diag_cnt, bishop_cnt):
    global max_, len_  # 전역 변수 max_와 len_을 함수 내에서 사용

    # 가지치기
    if max_ > (bishop_cnt + (len_ - diag_cnt + 1) // 2):
        return

    # 모든 대각선을 다 탐색했을 때
    if diag_cnt >= len_:
        max_ = max(max_, bishop_cnt)  # 현재까지의 비숍 개수와 최댓값을 비교하여 업데이트
        return

    # 현재 대각선에서 가능한 모든 위치에 대해 탐색
    for nrow, ncol in diag_list[diag_cnt]:
        if visited[nrow - ncol]:
            continue

        visited[nrow - ncol] = True  # 해당 대각선 위치를 방문했음을 표시
        dfs(diag_cnt + 2, bishop_cnt + 1)  # 다음 대각선으로 이동하며 비숍 개수를 증가시킴
        visited[nrow - ncol] = False  # 재귀 호출이 끝난 후 방문 표시를 초기화하여 다른 위치에서도 탐색 가능하도록 함

    dfs(diag_cnt + 2, bishop_cnt)  # 현재 대각선에 비숍을 놓지 않고 다음 대각선으로 이동

n = int(input())  # 체스판의 크기 입력
list_ = [list(map(int, input().split())) for _ in range(n)]  # 체스판 입력 받음
len_ = 2 * n - 1  # 대각선 개수 계산
diag_list = [[] for _ in range(len_)]  # 대각선에 해당하는 위치들을 담을 리스트 초기화
visited = [False] * len_  # 해당 대각선 위치를 방문했는지 여부를 저장할 리스트 초기화

# 대각선에 해당하는 위치들을 diag_list에 추가
for row in range(n):
    for col in range(n):
        if list_[row][col]:  # 비숍이 있는 위치라면
            diag_list[row + col].append((row, col))  # 해당 위치를 대각선 리스트에 추가

max_ = 0  # 최대 비숍 개수 초기화
dfs(0, 0)  # 대각선이 짝수인 경우의 DFS 탐색 시작
result = max_  # 결과 값 저장

max_ = 0  # 최대 비숍 개수 초기화
dfs(1, 0)  # 대각선이 홀수인 경우의 DFS 탐색 시작
result += max_  # 결과 값에 대각선이 홀수인 경우의 최대 비숍 개수를 더함

print(result)  # 결과 출력
