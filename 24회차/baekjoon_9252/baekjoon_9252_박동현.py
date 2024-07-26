N, M = list(input()), list(input())
lenn,lenm = len(N), len(M)

DP = [[0,[]] for _ in range(lenm)]         # DP의 각 인덱스를 M의 원소라 치고

for i in range(lenn):
    cnt = 0 
    tmp = ""
    for j in range(lenm):
        if cnt < DP[j][0]: 
            cnt = DP[j][0]
            tmp = DP[j][1]
        elif N[i] == M[j]: 
            DP[j][0] = cnt+1
            DP[j][1] = tmp+N[i]
a = max(DP, key = lambda x: x[0])

print(a[0])
if a[1]: print(a[1])