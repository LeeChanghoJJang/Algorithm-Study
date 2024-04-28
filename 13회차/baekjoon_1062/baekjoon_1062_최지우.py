import sys
from itertools import combinations
input = sys.stdin.readline


def word_to_bin(word):
    bit = 0
    for char in word:
        bit |= 1 << ord(char) - ord('a')
    return bit


N, K = map(int, input().split())

base = word_to_bin('acint')
words = [input().strip() for _ in range(N)]
words = list(map(word_to_bin, words))

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    K -= 5
    result = 0
    alpha = [1 << i for i in range(26) if not (base & 1 << i)]
    for c in combinations(alpha, K):
        learn = sum(c) | base
        cnt = 0
        for x in words:
            if x & learn == x:
                cnt += 1
        result = max(result, cnt)
    print(result)