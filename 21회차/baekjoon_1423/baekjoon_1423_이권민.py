import sys

# 재귀 호출 한도 설정 (필요에 따라 조정)
sys.setrecursionlimit(10000)

def solve(level, upgraded, remainDays):
    if remainDays < 0 or level >= n:
        return -1

    if mem[level][upgraded][remainDays] != -1:
        return mem[level][upgraded][remainDays]

    if level == n - 1:  # 마지막 레벨
        mem[level][upgraded][remainDays] = (characters[level] + upgraded) * powers[level]
        return mem[level][upgraded][remainDays]

    maxCount = min(characters[level] + upgraded, remainDays)
    res = 0
    for count in range(maxCount + 1):
        nextResult = solve(level + 1, count, remainDays - count)
        if nextResult == -1:
            continue

        currPower = powers[level] * (characters[level] + upgraded - count)
        result = nextResult + currPower
        res = max(res, result)

    mem[level][upgraded][remainDays] = res
    return res

# 입력 처리
n = int(input())
characters = list(map(int, input().split()))
powers = list(map(int, input().split()))
d = int(input())

# DP 메모리 초기화
mem = [[[-1 for _ in range(d + 1)] for _ in range(d + 1)] for _ in range(n)]

# 결과 출력
print(solve(0, 0, d)) 