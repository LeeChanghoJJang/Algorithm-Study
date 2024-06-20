T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    i = 0
    j = 0
    cnt = 0

    def max_coins(N, M, grid):
        dp = [[0] * M for _ in range(N)]

        # 초기값 설정
        dp[0][0] = grid[0][0]

        # 첫 행 초기화
        for j in range(1, M):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 첫 열 초기화
        for i in range(1, N):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 나머지 부분 계산
        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[N - 1][M - 1]


    def main():
        T = int(input("테스트 케이스의 개수 입력: "))

        for _ in range(T):
            N, M = map(int, input().split())
            grid = [list(map(int, input().split())) for _ in range(N)]

            result = max_coins(N, M, grid)
            print(result)

    # 그리디하게 해볼랬는데 안되넹 ㅎ..까비
    # while i < n or j < m:
    #     cnt += a[i][j]
    #     if i == n - 1 and j == m - 1:
    #         break
    #     elif i == n-1:
    #         j += 1
    #     elif j == m-1:
    #         i += 1
    #     else:
    #         if a[i+1][j] > a[i][j+1]:
    #             i += 1
    #         else:
    #             j += 1
    print(f'#{tc} {cnt}')
