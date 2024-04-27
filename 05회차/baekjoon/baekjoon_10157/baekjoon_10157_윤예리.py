import sys
sys.setrecursionlimit(1000000)
# sys.stdin = open('input.txt')

def go_up(i, j, value):
    global east, west, north, south, max

    if value == max:
        return

    while i > north and value <= max:
        arr[i][j] = value
        i -= 1
        value += 1
    west += 1
    return go_right(i, j, value)

def go_right(i, j, value):
    global east, west, north, south, max

    if value == max:
        return

    while j < east:
        arr[i][j] = value
        j += 1
        value += 1
    north += 1
    return go_down(i, j, value)

def go_down(i, j, value):
    global east, west, north, south, max

    if value == max:
        return

    while i < south:
        arr[i][j] = value
        i += 1
        value += 1
    east -= 1
    return go_left(i, j, value)

def go_left(i, j, value):
    global east, west, north, south, max

    if value == max:
        return

    while j > west:
        arr[i][j] = value
        j -= 1
        value += 1
    south -= 1
    return go_up(i, j, value)



c, r = map(int, input().split())
arr = [[0] * c for _ in range(r)]

north = west = 0
south = r-1
east = c-1
max = r*c

go_up(r-1, 0, 1)
arr[r//2][c//2] = max
result = []

k = int(input())
for i in range(r):
    if k in arr[i]:
        result.append(arr[i].index(k))
        print(result[0]+1, r-i)
if not result:
    print(0)
