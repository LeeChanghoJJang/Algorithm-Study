# 9095 1,2,3 더하기
# 목표 : n을 1,2,3의 합으로 나타내는 방법의 수 구하기
# 제한 : 0 < n < 11, 1000ms 이내
# 방법 : 이전의 수를 활용하여 다음 수를 예측 -> DP

DP = [0, 1, 2, 4] + [0] * 7

for c in range(int(input())):
    N = int(input())

    for i in range(4, N+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

    print(DP[N])

'''
31120KB / 40ms
'''