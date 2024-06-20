n = int(input())    # n+1개의 I와 n개의 O로 이루어져 있는 Pn
m = int(input())    # S의 길이
word = input()
pattern = 'IO' * n + 'I'
# KMP 알고리즘

# 패턴 전처리
def KMP_table(pattern):
    lp = len(pattern)
    tb = [0 for _ in range(lp)]

    pidx = 0
    for idx in range(1, lp):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = tb[pidx-1]

        if pattern[idx] == pattern[pidx]:
            pidx += 1
            tb[idx] = pidx

    return tb

# KMP 실행 함수
def KMP(word, pattern):
    table = KMP_table(pattern)

    result = []
    pidx = 0

    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = table[pidx-1]

        if word[idx] == pattern[pidx]:
            if pidx == len(pattern)-1:
                result.append(idx-len(pattern)+1)
                pidx = table[pidx]
            else:
                pidx += 1

    return result

print(len(KMP(word, pattern)))

# 시간 초과
#
# Pn = 'IO' * n + 'I'
# l = n*2+1
#
# cnt = 0
# for i in range(m-l):
#     if s[i:i+l] == Pn:
#         cnt += 1
# print(cnt)