t = int(input())

arr = list(map(int,input().split()))

max_idx = [1] * t
min_idx = [1] * t

for i in range(t-1):
    if arr[i+1] >= arr[i]:
        max_idx[i+1] += max_idx[i]
    if arr[i+1] <= arr[i]:
        min_idx[i+1] += min_idx[i]
    
a = max(max_idx)
b = max(min_idx)

print(max(a,b))