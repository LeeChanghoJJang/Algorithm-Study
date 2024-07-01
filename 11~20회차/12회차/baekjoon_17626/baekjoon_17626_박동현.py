N = int(input())
DP = [float('inf')]*(N+1)
sqrt = []
for i in range(1,N+1):
    sq = i**2 
    if sq > N :
        break
    sqrt.append(sq)
    DP[sq]=1
    if sq == N : 
        exit(print(1))

for m in sqrt :
    for _ in range(3):
        for i in range(1,N+1):
            if DP[i] != 0 and i+m<N+1:
                DP[i+m] = min(DP[i+m], DP[i]+1)

print(DP[-1])
            