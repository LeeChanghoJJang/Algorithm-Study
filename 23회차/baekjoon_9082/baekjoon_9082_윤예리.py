import sys
input = sys.stdin.readline

T = int(input())

def solution(x):
    global answer

    for nx in (x-1, x, x+1):
        if 0 <= nx < n:
            if nums[nx] <= 0: return

    answer += 1
    for nx in (x-1, x, x+1):
        if 0 <= nx < n:
            nums[nx] -= 1

for tc in range(T):
    n = int(input())
    nums = list(map(int, input().strip()))
    arr = list(input())
    answer = 0

    for i in range(n):
        if arr[i] == '*':
            answer += 1

            for ni in (i-1, i, i+1):
                if 0 <= ni < n: nums[ni] -= 1

    # print(nums)
    for i in range(n):
        solution(i)

    print(answer)