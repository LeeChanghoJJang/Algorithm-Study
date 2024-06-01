# 1052 물병

N, K = map(int, input().split())
ans = 0

# 이진수에서 1의 개수 찾기
while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    ans += 2**idx
    N += 2**idx

print(ans)