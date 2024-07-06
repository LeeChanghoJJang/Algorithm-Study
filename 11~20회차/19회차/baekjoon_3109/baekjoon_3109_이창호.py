import sys

sys.stdin = open('input.txt')


def dfs(row, col):
    global cnt
    if col == C - 1:
        cnt = True
        return True

    if row < 0 or row >= R or col < 0 or col >= C or pipeline[row][col] == 'x':
        return False

    pipeline[row][col] = 'x'  # 방문 처리

    for next in [-1, 0, 1]:
        if dfs(row + next, col + 1):
            return True

    # 방문 처리 원상 복구할 필요 없음
    return False


R, C = map(int, input().split())
pipeline = [list(input().strip()) for _ in range(R)]
result = 0
for i in range(R):
    cnt = False
    if dfs(i, 0):
        result += 1
print(result)
