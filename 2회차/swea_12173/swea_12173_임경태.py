# 12173 금화 모으기
# 숫자 합계의 최댓값을 구함 / 다중 경로를 효율적으로 탐색하기 위해 DP 사용

for tc in range(int(input())):
    N, M = map(int, input().split())
    coin = [list(map(int, input().split())) for _ in range(N)]
    DP = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            DP[i][j] = coin[i][j] + max(DP[i][j-1], DP[i-1][j])
    
    print(f'#{tc+1} {DP[-1][-1]}')