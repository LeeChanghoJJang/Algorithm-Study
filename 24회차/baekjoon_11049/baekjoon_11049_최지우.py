import sys
input = sys.stdin.readline

def solve(arr):
    n = len(arr) - 1  # 행렬의 개수
    dp = [[0] * n for _ in range(n)]

    # 행렬 체인의 길이를 2부터 n까지 반복
    for len_ in range(2, n+1):
        for i in range(n - len_ + 1):  # 시작 행렬의 인덱스
            j = i + len_ - 1  # 끝 행렬의 인덱스
            dp[i][j] = sys.maxsize  # 초기화할 때 큰 값으로 설정

            # i에서 j까지의 행렬 곱셈 중 최소값 찾기
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + arr[i] * arr[j+1] * arr[k+1]  # 행렬 곱셈 비용 계산
                dp[i][j] = min(dp[i][j], cost)  # 최소 비용 갱신
    
    return dp[0][n-1]


N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    if i == N-1:
        arr.extend([a, b])
        break
    arr.append(a)

print(solve(arr))
