import sys
sys.stdin = open('input.txt')
# 수빈 :N ,동생 : K
N, K = map(int,input().split())
# 수빈이 더 크면 2배는 쓸 수 없으므로 1씩 이동
if N>=K:
    print(N-K)
# 수빈이 동생보다 작을 때 아래 로직 적용
else:
    # 여유롭게 계산하고자 DP의 길이를 K의 2배정도까지 설정
    DP = [0]*2*(K+1)
    # N 밑으로는 1씩만 이동가능.
    for i in range(N):
        DP[i] = N-i
    # N보다 클 때 DP를 이용하여 누적 최소값을 더한다.
    for i in range(N+1,2*K+1):
        '''
        2로 나눠지는 경우
        1. 2로 나눈 수의 값 + 1
        2. 1뺀 값의 + 1
        '''
        if i%2 ==0:
            DP[i] = min(DP[i//2]+1,DP[(i-1)]+1)
        '''
        2로 안나눠지는 경우
        1. 1뺀 값을 2로 나눈 수의 값 + 2
        2. 1더한 값을 2로 나눈 수의 값 + 2
        3. 1뺀 값의 + 1
        '''
        else:
            DP[i] = min(DP[(i-1)//2]+2, DP[(i+1)//2] +2,DP[i-1]+1)
    print(DP[K])
'''
38824KB 136ms
'''
