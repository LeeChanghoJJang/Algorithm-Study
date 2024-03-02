import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
ondo = list(map(int,input().split()))
cumulative_sum = [0] *(N+1)

for i in range(1,N+1):
    cumulative_sum[i] = cumulative_sum[i-1] + ondo[i-1]
max_val = float('-inf')

for i in range(N-K+1):
    current_sum = cumulative_sum[i+K] - cumulative_sum[i]
    max_val = max(max_val,current_sum)
print(max_val)