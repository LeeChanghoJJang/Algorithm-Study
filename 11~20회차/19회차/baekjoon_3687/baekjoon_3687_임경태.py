# 3687 성냥개비
DP = [float('inf')] * 101
DP[2:9] = ["1", "7", "4", "2", "6", "8", "10"]

# 최소 숫자 찾기
for i in range(9, 101):
    for j in range(2, i-1):
        DP[i] = min(DP[i], int(str(DP[j]) + str(DP[i-j])))
        if j == 6:
            DP[i] = min(DP[i], int(str(DP[i-j]) + '0'))

# 최대 숫자 찾기
def find_max(N):
    return "7" + "1" * (N//2-1) if N & 1 else "1" * (N//2)

for _ in range(int(input())):
    N = int(input())
    print(DP[N], find_max(N))