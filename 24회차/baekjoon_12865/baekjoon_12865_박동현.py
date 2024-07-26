N, K = map(int,input().split())
DP = [[0] * (K+1) for _ in range(N+1)]
thing = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
# thing[n][0] : 무게 / thing[n][1] : 가치

# DP 의 세로는 각 물건을 넣는 경우를, 세로는 무게 1부터 무게 K 까지 물건 가치의 최대값을 나타낸다.

for i in range(N+1):
    for j in range(K+1):
        
        if j < thing[i][0]:             # 물건이 j보다 크면
            DP[i][j] = DP[i-1][j]       # DP의 이전 값을 출력 (이전에 그 이하로 담긴게 있다면 갱신되고 아니면 0을 받음)

        else :                          # 물건을 담을 수 있다면 
            # 지금 무게에서 물건을 하나 넣었을때(물건이 들어갈 공간을 비우고 그 당시 최대치에서 지금 가치를 더해서 최대치 출력)
            DP[i][j] = max(DP[i-1][j-thing[i][0]]+thing[i][1], DP[i-1][j])  

# 출력            
print(DP[N][K])