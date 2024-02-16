import sys
sys.stdin = open('input.txt')
# 아래 문장이 모든걸 말해준다.
'''
1일 때는 1
2일 때는 2
3일 때는 4
4일 때는 7
5일 때는 13
6일 때는 24
7일 때는 44
즉, 전단계와 전전단계와 전전전단계의 합이 이후 단계라는 규칙성을 파악할 수 있음
전단계에서 1을 더해준것과
전전단계에서 2를 더해준것과
전전전단계에서 3을 더해준것과 개수가 같아서 인것 같음 
'''
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    # max는 0,1,2의 경우[실제값 1,2,3]를 감안하여 설정
    DP = [0] * max(N,3)
    DP[0] = 1
    DP[1] = 2
    DP[2] = 4
    # N이 3보다 클 때! (적어도 3개의 초기값은 있어야 되니까)
    if N>3:
        for x in range(3,N):
            DP[x] = DP[x-1] + DP[x-2] + DP[x-3]
        print(DP[-1])
    else:
        print(DP[N-1])
