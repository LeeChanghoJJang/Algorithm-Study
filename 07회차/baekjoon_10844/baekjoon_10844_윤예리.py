# dp에 자식 노드의 개수를 계속 더해줌
n = int(input())
dp = [[0] * 10 for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)
print(dp)

# backtracking
# def backtraking(result, i):
#     if len(result) == n:
#         if result not in stepnum:
#             stepnum.append(result)
#             return
#
#     else:
#         if 0<=i+1<10:
#             backtraking(result+str(i), i+1)
#         if 0<=i-1<10:
#             backtraking(result+str(i), i-1)
#
#         else:
#             return
#
# n = int(input())
# stepnum = []
#
# for j in range(1, 10):
#     backtraking('', j)
#
# print(len(stepnum))