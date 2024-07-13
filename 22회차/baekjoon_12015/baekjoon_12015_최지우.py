n = int(input())
num = list(map(int, input().split()))

dp = [num[0]]

for i in num[1:]:
    start = 0
    end = len(dp) - 1

    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    
    if start >= len(dp):
        dp.append(i)
    else:
        dp[start] = i

print(len(dp))