import sys
sys.stdin = open('input.txt')

room = [[0] * 2 for _ in range(6)]
n, k = map(int, input().split())
for _ in range(n):
    # 남: 1, 여: 0
    s, y = map(int, input().split())

    room[y-1][s] += 1

result = 0
for i in range(6):
    for j in range(2):
        if room[i][j] > 0:
            result += ((room[i][j]-1)//k+1)

print(result)