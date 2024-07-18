N,M = map(int,input().split())
arr = [int(input()) for _ in range(N)]

maxv = M**2*N
DP = [maxv]*(N+1)   #줄은 최대 N 개 나뉨

def note(idx=0):
    if DP[idx] < maxv:
        return DP[idx]

    res = M - arr[idx]

    for i in range(idx+1, N+1):
        if res >= 0:
            if i==N:
                DP[idx]=0; break
            DP[idx] = min(DP[idx], res**2+note(i))
            res -= arr[i]+1
    
    return DP[idx]

print(note())

# 어떻게하는지 이제 진짜 모르겠음.