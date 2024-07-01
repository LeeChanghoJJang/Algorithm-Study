# 17626 Four Squares

n = int(input())

# 제곱 수는 1로 배열에 저장
DP = [4 if i**0.5%1 else 1 for i in range(n+1)]

# 제곱 수이면 패스
if DP[n] == 1: exit(print(1))

# 배열 순회
for i in range(1, n+1):
    # 최대 제곱근까지 순회
    for j in range(1, int(i**0.5)+1):
        # 최소 횟수 저장
        DP[i] = min(DP[i], DP[i-j**2] + 1)

print(DP[n])