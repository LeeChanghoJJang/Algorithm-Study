# 9251 LCS (골드5)

str1, str2 = input(), input()
A, B = len(str1), len(str2)
DP, ans = [0] * B, 0

# 비교하는 문자열이 있는 배열 순회
for i in range(A):
    # 공통 부분의 카운트
    cnt = 0
    # 비교대상 배열의 문자열 순회
    for j in range(B):
        if cnt < DP[j]: cnt = DP[j]
        # 두 문자열이 같다면 카운트 + 1을 DP에 추가
        elif str1[i] == str2[j]: DP[j] = cnt + 1

print(max(DP))

'''
31120KB / 220ms
'''