def dp(a,p):
    global ans
    tmp = 0
    b = B if a==A else A

    if a[j] == S[i]:
        for k in range(j-1,-1,-1):
            if b[k] == S[i-1]:
                tmp += DP[p][k]
        DP[1-p][j] = tmp
        if i == lens-1:
            ans += tmp

S,A,B = "0"+input(), "0"+input(), "0"+input()
lens, lena = len(S), len(A)
DP = [[0] * lena for _ in range(2)]
DP[0][0], DP[1][0] = 1,1

ans=0
for i in range(1, lens):
    for j in range(lena-1,-1,-1):
        dp(A,1)
        dp(B,0)
print(ans)