T = int(input())

for i in range(T):
    N,M = map(int,input().split())  # A:N, B:M
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    # N > M :
    weight = abs(N-M)
    result = 0
    if N > M :
        for w in range(weight+1):
            s = 0
            for idx in range(len(Bj)):
                s += Ai[idx+w] * Bj[idx]
            if s > result:
                result = s
    else :
        for w in range(weight+1):
            s =0 
            for idx in range(len(Ai)):
                s += Bj[idx+w] * Ai[idx]
            if s > result:
                result = s
    print(f"#{i+1} {result}")