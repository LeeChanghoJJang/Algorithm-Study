import sys
input = sys.stdin.readline
n = int(input())


def draw_stars(n):
    star = [[' ' for _ in range(2*n - 1)] for _ in range(n)]

    def fill_triangle(x, y, size):
        if size == 3:
            star[x][y] = '*'
            star[x+1][y-1] = star[x+1][y+1] = '*'
            for i in range(5):
                star[x+2][y-2+i] = '*'
        else:
            new_size = size // 2
            fill_triangle(x, y, new_size)
            fill_triangle(x + new_size, y - new_size, new_size)
            fill_triangle(x + new_size, y + new_size, new_size)

    fill_triangle(0, n-1, n)
    return star


star = draw_stars(n)
for row in star:
    print(''.join(row))
