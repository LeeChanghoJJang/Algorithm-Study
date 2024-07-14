import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(N)]

# 최대 점수와 최소 점수를 위한 배열 초기화
max_dp = board[0][:]
min_dp = board[0][:]

for i in range(1, N):
    current_row = board[i]

    # 최대 점수 계산
    new_max_dp = [0] * 3
    new_max_dp[0] = current_row[0] + max(max_dp[0], max_dp[1])
    new_max_dp[1] = current_row[1] + max(max_dp[0], max_dp[1], max_dp[2])
    new_max_dp[2] = current_row[2] + max(max_dp[1], max_dp[2])

    # 최소 점수 계산
    new_min_dp = [0] * 3
    new_min_dp[0] = current_row[0] + min(min_dp[0], min_dp[1])
    new_min_dp[1] = current_row[1] + min(min_dp[0], min_dp[1], min_dp[2])
    new_min_dp[2] = current_row[2] + min(min_dp[1], min_dp[2])

    # 현재 dp 값을 갱신
    max_dp = new_max_dp
    min_dp = new_min_dp

print(max(max_dp), min(min_dp))
