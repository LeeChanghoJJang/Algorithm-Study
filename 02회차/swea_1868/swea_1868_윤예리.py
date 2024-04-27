# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(str, input())) for _ in range(N)]
#     answer = [[0] * N+2 for _ in range(N+2)]
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '*':
#                 answer[i][j] = '*'
#
#     for i in range(N):
#         for j in range(N):
#             if answer[i][j] == 0:
#                 if

def count_clicks(N, minefield):
    clicks = 0
    revealed = [['.'] * N for _ in range(N)]

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N

    def count_adjacent_mines(x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and minefield[nx][ny] == '*':
                    count += 1
        return count

    def reveal(x, y):
        nonlocal clicks
        if not is_valid(x, y) or revealed[x][y] == 'c':
            return

        revealed[x][y] = 'c'
        clicks += 1

        if minefield[x][y] == '0':
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    reveal(x + dx, y + dy)

    for i in range(N):
        for j in range(N):
            if minefield[i][j] == '.':
                adjacent_mines = count_adjacent_mines(i, j)
                if adjacent_mines == 0:
                    reveal(i, j)

    return clicks

def main():
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        minefield = [input() for _ in range(N)]

        result = count_clicks(N, minefield)
        print(f"#{tc} {result}")