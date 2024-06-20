import sys
sys.stdin = open('input.txt')

N = int(input())
max_nums = []

# 현재 수의 절반 이상 수에서 순회
for n in range(N//2, N+1):
    nums = [N, n]
    # 전 전 숫자에서 전 숫자 빼기
    while nums[-2] >= nums[-1]:
        nums.append(nums[-2] - nums[-1])
    # 최대 수열보다 현재 수열의 원소 수가 많다면 갱신
    if len(nums) > len(max_nums):
        max_nums = nums

print(len(max_nums))
print(*max_nums)