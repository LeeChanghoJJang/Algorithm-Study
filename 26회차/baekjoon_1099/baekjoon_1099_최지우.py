import sys
input = sys.stdin.readline

sentence = list(input().strip())
N = int(input())
words = [input().strip() for _ in range(N)]
dp = [1e9] * (len(sentence)+1)
dp[0] = 0

for idx in range(1, len(sentence)+1):
    for word in words:
        if idx - len(word) < 0:
            continue
    
        if idx - len(word) != 0 and dp[idx - len(word)] == 1e9:
            continue
        
        start = idx - len(word)
        sword = sorted(list(word))
        ssen = sorted(sentence[start:idx])
        if sword != ssen:
            continue
        
        cnt = 0
        for i in range(len(word)):
            if word[i] != sentence[start:idx][i]:
                cnt += 1
        dp[idx] = min(dp[idx], dp[idx - len(word)] + cnt)
        
print(dp[-1] if dp[-1] != 1e9 else -1)
