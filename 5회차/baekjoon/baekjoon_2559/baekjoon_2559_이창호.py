import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
ondo = list(map(int,input().split()))
cumulative_sum = [0] *(N+1)
# 처음에 sum으로 풀었으나, 시간초과로 DP로 전환 
# 누적합을 cumulative_sum 배열에 저장 
for i in range(1,N+1):
    cumulative_sum[i] = cumulative_sum[i-1] + ondo[i-1]
max_val = float('-inf')
# 누적합에서 인덱스 K 차이는 것을 빼면
# K개의 수열의 합을 지속적으로 비교하여 max_val에 저장가능 
for i in range(N-K+1):
    current_sum = cumulative_sum[i+K] - cumulative_sum[i]
    max_val = max(max_val,current_sum)
print(max_val)
