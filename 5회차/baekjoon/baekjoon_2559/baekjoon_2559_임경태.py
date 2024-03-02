import sys
sys.stdin = open('input.txt')

# 풀이 1 : 누적합
N, K = map(int, input().split())
temp = [0] + list(map(int, input().split()))
max_v = -float('inf')

for i in range(N):
    temp[i+1] += temp[i]

for i in range(N-K+1):
    max_v = max(max_v, temp[i+K] - temp[i])

print(max_v)


# 풀이 2 : 슬라이딩 도어
N, K = map(int, input().split())
temp = list(map(int, input().split()))
sum_temp = [sum(temp[:K])]

for i in range(1, N-K+1):
    sum_temp.append(sum_temp[-1] - temp[i-1] + temp[i+K-1])

print(max(sum_temp))