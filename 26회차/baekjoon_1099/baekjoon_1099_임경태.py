# 1099 알 수 없는 문장

sentence = " " + input()
n = int(input())
words = [input() for _ in range(n)]

# dp[i][j]: 문장의 i번째 문자부터 j번째 문자까지의 구간을 해석하는 데 필요한 최소 비용
dp = [[1000] * (len(sentence)) for _ in range(len(sentence))]
dp[0][0] = 0

# 단어 해석 비용 함수
def check(word1, word2, length):
    cnt = 0
    for i in range(length):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

for i in range(1, len(sentence)+1):
    # 앞서 연결될 수 있는 단어가 없음
    if dp[i-1][0] == 1000:
        continue

    for word in words:
        length = len(word)

        # 해석될 수 있는 단어
        if sorted(sentence[i:i+length]) == sorted(word):
            dp[i][i+length-1] = min(dp[i][i+length-1], dp[i-1][0] + check(sentence[i:i+length], word, length))
            # 맨 앞에 현재 길이까지의 최솟값 업데이트
            dp[i+length-1][0] = min(dp[i+length-1][0], dp[i][i+length-1])

print(dp[-1][0] if dp[-1][0] != 1000 else -1)
