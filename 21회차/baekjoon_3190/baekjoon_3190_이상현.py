# import sys
# sys.stdin = open('input.txt')

N = int(input())
K = int(input())
list_ = [[0] * N for _ in range(N)]
rotation_list = [0] * 10000

for _ in range(K):
    row, col = map(int, input().split())
    list_[row - 1][col - 1] = 2

L = int(input())

for _ in range(L):
    X, C = input().split()
    rotation_list[int(X)] = C

snake = []
snake.append([0, 0])
list_[0][0] = 1

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
nrow = ncol = time = 0
idx = 1

while True:
    time += 1
    nrow = nrow + drow[idx]
    ncol = ncol + dcol[idx]

    if not (0 <= nrow < N and 0 <= ncol < N) or list_[nrow][ncol] == 1:
        break

    if list_[nrow][ncol] == 2:
        snake.append([nrow, ncol])
        list_[nrow][ncol] = 1

    elif list_[nrow][ncol] == 0:
        snake.append([nrow, ncol])
        list_[nrow][ncol] = 1

        row, col = snake.pop(0)
        list_[row][col] = 0

    if rotation_list[time] == 'D':
        idx = (idx + 1) % 4
    elif rotation_list[time] == 'L':
        idx = (idx + 3) % 4

print(time)