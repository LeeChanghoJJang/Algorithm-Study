# 9251 LCS (골드5)

str1, str2 = input(), input()
A, B = len(str1), len(str2)
DP, ans = [0] * B, 0

for i in range(A):
    cnt = 0
    for j in range(B):
        if cnt < DP[j]: cnt = DP[j]
        elif str1[i] == str2[j]: DP[j] = cnt + 1

print(max(DP))

'''
31120KB / 220ms
'''