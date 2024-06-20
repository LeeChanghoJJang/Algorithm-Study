N, K = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
max_ = -float('inf')

for i in range(N):
    num_list[i + 1] += num_list[i]

for i in range(K, N + 1):
    max_ = max(max_, num_list[i] - num_list[i - K])

print(max_)