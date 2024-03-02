N = int(input())
list_ = list(map(int, input().split()))
result = []

for i in range(N):
    result.insert(list_[i], i + 1)

print(*result[::-1])