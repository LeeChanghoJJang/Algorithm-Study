import sys
input = sys.stdin.readline

def lcs(s1, s2):
    x, y = len(s1), len(s2)
    dp = [[0] * (y+1) for _ in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    res_len = dp[x][y]
    print(res_len)

    res_str = []
    while x > 0 and y > 0:
        if s1[x-1] == s2[y-1]:
            res_str.append(s1[x-1])
            x -= 1
            y -= 1
        elif dp[x-1][y] > dp[x][y-1]:
            x -= 1
        else:
            y -= 1

    print(''.join(reversed(res_str)))

s1 = input().strip()
s2 = input().strip()
lcs(s1, s2)

