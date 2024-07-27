# 2448 LCS 2
A = [""] + list(input())
B = [""] + list(input())

# LCS(최장 공통 부분 수열)를 저장할 2차원 리스트 초기화
LCS = [[""] * len(B) for _ in range(len(A))]

# LCS 계산
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            # 두 문자가 같으면 대각선 위 값에 해당 문자를 추가
            LCS[i][j] = LCS[i-1][j-1] + A[i]
        else:
            # 두 문자가 다르면 위쪽 또는 왼쪽 값 중 더 긴 문자열 선택
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

# 결과 추출
result = LCS[-1][-1]

# 결과 출력 (최장 공통 부분 수열의 길이와 문자열)
print(len(result), result, sep="\n")
