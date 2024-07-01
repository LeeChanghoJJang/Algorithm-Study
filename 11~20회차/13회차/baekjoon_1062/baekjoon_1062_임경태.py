# 1062 가르침
from itertools import combinations

N, K = map(int, input().split())

# 가지치기
if K < 5: exit(print(0))
elif K == 26: exit(print(N))

wordLst = list()
wordSet = set()
ans = 0

# 각 단어마다 체크
for _ in range(N):
    nowSet = set(input()) - set("antic")
    nowLen = len(nowSet)

    # 가지치기
    if nowLen == 0: ans += 1; continue
    if nowLen > K-5: continue

    # 비트마스크 생성 (각 글자마다 특정 2진수 자리의 10진수 숫자로 변환)
    bitmask = 0
    for char in nowSet:
        bitmask += 1 << (ord(char) - ord('a'))

    wordLst.append(bitmask)
    wordSet |= nowSet

wordLen = len(wordSet)
wordSet = map(lambda x: 1 << (ord(x) - ord('a')), wordSet)

def compare(w):
    # 가르친 글자들 (서로 겹치지 않기 때문에 합계가 가능)
    teach = sum(w)
    cnt = 0

    # 가르친 글자로 단어를 커버할 수 있다면 카운트
    for word in wordLst:
        if teach & word == word:
            cnt += 1

    return cnt

# 글자 조합을 추출하여 가장 많은 단어를 커버할 수 있는 조합 찾기
print(ans + max(map(compare, combinations(wordSet, min(K-5, wordLen)))))