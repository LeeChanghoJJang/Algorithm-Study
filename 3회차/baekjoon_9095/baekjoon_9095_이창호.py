import sys
sys.stdin = open('input.txt')
'1일 때는 1'
'2일 때는 2'
'3일 때는 4'
'4일 때는 7'
'5일 때는 13'
'6일 때는 24'
'7일 때는 44'
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    DP = [0] * max(N,3)
    DP[0] = 1
    DP[1] = 2
    DP[2] = 4
    if N>3:
        for x in range(3,N):
            DP[x] = DP[x-1] + DP[x-2] + DP[x-3]
        print(DP[-1])
    else:
        print(DP[N-1])