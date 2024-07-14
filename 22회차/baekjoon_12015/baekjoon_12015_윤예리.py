import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = [0]

for ai in arr:
    if answer[-1] < ai:
        answer.append(ai)
        continue

    left = 0
    right = len(answer)

    while left < right:
        mid = (left + right) // 2

        if answer[mid] < ai:
            left = mid + 1
        else:
            right = mid

    answer[right] = ai

print(len(answer)-1)