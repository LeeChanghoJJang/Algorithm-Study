'''
위 아래 집의 색이 달라야 함
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = float('inf')
for k in range(3):      # RGB 거리 1번 코드를 R, G, B 경우 나눠서 3번 돌린다.
    memo = [[float('inf')] * 3 for _ in range(n)]
    memo[0][k] = arr[0][k]

    for i in range(1, n):
        memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + arr[i][0]    # r
        memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + arr[i][1]    # g
        memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + arr[i][2]    # b

    for c in range(3):      # 마지막 색이랑 처음 색이 다를 때 min 값 고려
        if k != c:
            result = min(result, memo[-1][c])

# 최종 작은 수
print(result)