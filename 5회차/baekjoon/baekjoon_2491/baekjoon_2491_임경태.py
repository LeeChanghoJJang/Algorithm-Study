import sys
sys.stdin = open('input.txt')

N = int(input())
seq = list(map(int, input().split()))
DP1, DP2 = [1] * N, [1] * N

for i in range(N-1):
    if seq[i+1] >= seq[i]: DP1[i+1] += DP1[i]
    if seq[i+1] <= seq[i]: DP2[i+1] += DP2[i]

print(max(max(DP1), max(DP2)))