# SWEA 2806번 N-Queen

# 퀸을 현재 위치에 놓을 수 있는지 확인하는 함수
def is_valid(col):
    return all(row[i] != row[col] and abs(row[col] - row[i]) != col - i for i in range(col))


# 1열부터 시작해서 퀸을 차례대로 놓기 시작함
# 만약 N열까지 퀸을 놓는 데 성공했다면 cnt의 값에 1을 더해줌
def dfs(col, N):
    cnt = 0

    if col == N:
        return 1
    else:
        for i in range(N):
            # 퀸을 i + 1 행 col + 1 열에 놓음
            row[col] = i

            # 만약 그 칸에 퀸을 놓아도 아무런 문제가 없으면 다음 열로 넘어감
            if is_valid(col):
                cnt += dfs(col + 1, N)
    return cnt

T = int(input())

for tc in range(T):
    N = int(input())

    # row[num] 은 num + 1 열에 퀸이 위치한 행의 번호 - 1 을 나타냄
    row = [0] * N

    print(f'#{tc + 1} {dfs(0, N)}')