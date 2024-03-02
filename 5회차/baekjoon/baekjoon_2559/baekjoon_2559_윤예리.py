# import sys
# sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = list(map(int, input().split()))
window = sum(arr[:k])
answer = window

for i in range(k, n):
    window += arr[i] - arr[i-k]
    answer = max(window, answer)

print(answer)