# 1182 / 부분수열의 합 / 실버2

"""
방법 1 : combination 라이브러리 이용 / 31120KB / 360ms
# """
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

# 1 ~ N개의 부분집합 생성 후 합 계산
for i in range(1, N + 1):
    for j in combinations(nums, i):
        if sum(j) == S:
            cnt += 1

print(cnt)

"""
방법 2: 완전탐색 & 백트래킹 이용 / 31120KB / 280ms
"""
def backtrack(idx, sum_v):
    if idx < N:
        sum_v += nums[idx]

        # 합이 조건을 만족한다면 카운트
        if sum_v == S:
            global cnt
            cnt += 1

        # 현재 인덱스의 숫자 포함
        backtrack(idx + 1, sum_v)
        # 현재 인덱스의 숫자 미포함
        backtrack(idx + 1, sum_v - nums[idx])

N, S = map(int, input().split())
nums = tuple(map(int, input().split()))
cnt = 0; backtrack(0, 0)
print(cnt)
