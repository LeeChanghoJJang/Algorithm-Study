N, K = map(int, input().split())
result = 0

while bin(N).count('1') > K:
    N += 1
    result += 1

print(result)