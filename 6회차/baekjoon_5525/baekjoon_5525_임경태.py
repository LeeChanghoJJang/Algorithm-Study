# 5525 IOIOI

import sys
sys.stdin = open('input.txt')

# KMP 알고리즘 : 100점
def KMP(P, text):
    # IOIOI -> [0, 0, 1, 2, 3] 배열 생성
    lps = [0] * len(P)
    for i in range(1, len(P)):
        if P[lps[i-1]] == P[i]: lps[i] = lps[i-1] + 1

    cnt, j = 0, 0
    for i in range(len(text)):
        while j > 0 and text[i] != P[j]:
            j = lps[j - 1]
        if text[i] == P[j]:
            if j == len(P) - 1:
                cnt += 1
                j = lps[j]
            else:
                j += 1
    return cnt

N, M, S = int(input()), int(input()), input()
print(KMP('I'+'OI'*N, S))

# Brute-Force : 52점
'''
N, M, S = int(input()), int(input()), input()
char, cnt = 'I' + 'OI'*N, 0
for i in range(M-len(char)+1):
    if S[i:i+len(char)] == char:
        cnt += 1
print(cnt)
'''