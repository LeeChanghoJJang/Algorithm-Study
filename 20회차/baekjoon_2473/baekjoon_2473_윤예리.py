import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

value = float('inf')
answer = []

for i in range(n-2):
    cur = arr[i]
    start = i+1
    end = n-1

    while start < end:
        total = cur + arr[start] + arr[end]

        if abs(total) <= abs(value):
            answer = [cur, arr[start], arr[end]]
            value = total
        
        if total == 0:
            exit(print(*answer))
        
        elif total < 0: start += 1
        else: end -= 1

print(*answer)