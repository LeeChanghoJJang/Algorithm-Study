import sys
input = sys.stdin.readline

def solve(N, M, K, arr):
    black = [[0] * (M+1) for _ in range(N+1)]
    white = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(M):
            if not (i+j) % 2:
                if arr[i][j] == 'B':
                    black[i+1][j+1] = black[i+1][j] + black[i][j+1] - black[i][j]
                    white[i+1][j+1] = white[i+1][j] + white[i][j+1] - white[i][j] + 1
                else:
                    black[i+1][j+1] = black[i][j+1] + black[i+1][j] - black[i][j] + 1
                    white[i+1][j+1] = white[i][j+1] + white[i+1][j] - white[i][j]
            else:
                if arr[i][j] == 'B':
                    black[i+1][j+1] = black[i][j+1] + black[i+1][j] - black[i][j] + 1
                    white[i+1][j+1] = white[i][j+1] + white[i+1][j] - white[i][j]
                else:
                    black[i+1][j+1] = black[i][j+1] + black[i+1][j] - black[i][j]
                    white[i+1][j+1] = white[i][j+1] + white[i+1][j] - white[i][j] + 1

    min_cost = float('inf')
    
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            black_sum = black[i+K-1][j+K-1] - black[i-1][j+K-1] - black[i+K-1][j-1] + black[i-1][j-1]
            white_sum = white[i+K-1][j+K-1] - white[i-1][j+K-1] - white[i+K-1][j-1] + white[i-1][j-1]
            min_cost = min(min_cost, black_sum, white_sum)
    
    return min_cost

N, M, K = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

result = solve(N, M, K, arr)
print(result)