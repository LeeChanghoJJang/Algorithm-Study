import sys
input = sys.stdin.readline
from collections import defaultdict

# 문장 받아주기
sent = list(input().rstrip())
N = int(input())
words = []
alpha = dict()

# 비교할 단어들 저장해주기
# 단어들마다 들어가는 알파벳으로 기록해준다.
# 딕셔너리로 저장해야 o n e 와 e n o 가 같은 철자라는 것을 확인 가능함
for i in range(N):
    word = input().rstrip()
    words.append(word)
    alpha[word] = defaultdict(int)
    for w in word:
        alpha[word][w] += 1

# dp 사용해주는데
# dp의 인덱스는 해석된 단어의 인덱스
# neotow에서 two를 비교했다면 -> dp[5]에 기록된다.
# dp 갱신은 앞선 단어를 해석하는데 필요한 값 + 현재 비교한 단어의 값 vs 기록되어 있는
# 최초 값이 존재하지 않으므로 임의의 0번 인덱스에 0 추가
dp = [0] + [1000] * len(sent)

# 문장의 중간에 비교해야되는 값이 있으므로
# 1글자씩 늘려주면서 비교해준다 -> neotow이면 n, ne, neo, neot, neoto ---
for start in range(len(sent)):
    for end in range(start, len(sent)):
        temp = defaultdict(int)
        comp = sent[start:end+1]
        for c in comp:
            temp[c] += 1

        # 현재 문장에서 자른 단어와 철자가 같은 단어가 있는지 체크
        # 딕셔너리끼리 비교해준다.
        for word in words:
            if alpha[word] != temp:
                continue

            # 철자 같다면 해석비용
            cnt = 0
            for j in range(len(word)):
                if word[j] != comp[j]:
                    cnt += 1

            # 임의의 0번 인덱스를 추가하였으므로 end+1에 기록해준다.
            dp[end+1] = min(dp[end+1], dp[start] + cnt)

print(dp[-1] if dp[-1] != 1000 else -1)