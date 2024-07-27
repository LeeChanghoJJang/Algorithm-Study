import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

a, b = input().strip(), input().strip()
la = len(a)
lb = len(b)
dp = [[0] * (lb+1) for _ in range(la+1)]
for i in range(1,la+1):
    for j in range(1,lb+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[la][lb])
# LCS 추적하여 출력
if dp[la][lb] != 0:
    lcs = []
    x, y = la, lb
    while x > 0 and y > 0:
        if a[x - 1] == b[y - 1]:
            lcs.append(a[x - 1])
            x -= 1
            y -= 1
        elif dp[x - 1][y] >= dp[x][y - 1]:
            x -= 1
        else:
            y -= 1
    print(''.join(reversed(lcs)))
