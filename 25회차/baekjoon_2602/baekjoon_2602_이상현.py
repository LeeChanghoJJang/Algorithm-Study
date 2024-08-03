import sys
sys.stdin = open('input.txt')

target = input()
list_ = [input() for _ in range(2)]

len_target = len(target)
len_list = len(list_[0])

dp = [[[0] * 2 for _ in range(len_target)] for _ in range(len_list)]

for i in range(len_list):
    for j in range(len_target):
        for k in range(2):
            if list_[k][i] == target[j]:
                if j == 0:
                    dp[i][j][k] = 1
                else:
                    for l in range(i):
                        dp[i][j][k] += dp[l][j - 1][1 - k]

result = 0
for i in range(len_list):
    for j in range(2):
        result += dp[i][-1][j]

print(result)
