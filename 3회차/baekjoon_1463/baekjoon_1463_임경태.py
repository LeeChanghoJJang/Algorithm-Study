# 1463 1로 만들기

# 목표 : 연산 사용 횟수의 최솟값 구하기
# 연산 : 3으로 나누어 떨어지면 3으로 나눔 / 2로 나누어 떨어지면 2로 나눔 / 1을 뺌
# 제한 : 1 <= N <= 1,000,000 , 시간 150ms 이내 => O(NlogN) 이내

'''
풀이 1 : O(N) / 39056KB / 504ms
'''
N = int(input())
DP = [0] * (N+1)

for n in range(2, N+1):
    if n % 3 == 0 and n % 2 == 0:
        DP[n] = min(DP[n//3], DP[n//2]) + 1
    elif n % 3 == 0:
        DP[n] = min(DP[n-1], DP[n//3]) + 1
    elif n % 2 == 0:
        DP[n] = min(DP[n-1], DP[n//2]) + 1
    else:
        DP[n] = DP[n-1] + 1

print(DP[N])

'''
풀이 2 : O(N) / 38932KB / 548ms
'''
N = int(input())
DP = [0] * (N+1)

for n in range(2, N+1):
    DP[n] = DP[n-1] + 1
    if n % 2 == 0:
        DP[n] = min(DP[n], DP[n//2] + 1)
    if n % 3 == 0:
        DP[n] = min(DP[n], DP[n//3] + 1)

print(DP[N])