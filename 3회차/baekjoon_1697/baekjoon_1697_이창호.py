import sys
sys.stdin = open('input.txt')
# 수빈 :N ,동생 : K
N, K = map(int,input().split())
# 순간이동시 2*X
if N>=K:
    print(N-K)
else:
    DP = [0]*2*(K+1)
    for i in range(N):
        DP[i] = N-i

    # 각자 K//2까지 범위만 두배씩 한것과 min값 비교해서 저장
    for i in range(N+1,2*K+1):
        if i%2 ==0:
            DP[i] = min(DP[i//2]+1,DP[(i-1)//2]+2,DP[(i+1)//2]+2,DP[(i-1)]+1)
        else:
            DP[i] = min(DP[(i-1)//2]+2, DP[(i+1)//2] +2,DP[i-1]+1)
    print(DP[K])



