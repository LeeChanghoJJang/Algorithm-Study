def solution(board):
    o = x = p = 0

    for line in board:
        o += line.count('O')
        x += line.count('X')
        p += line.count('.')

    if o == x == 0:
        return 1

    if o < x or o > x + 1:
        return 0

    check = ttt(board)
    if 'O' in check and 'X' in check:
        return 0

    if o == x:
        if 'O' in check:
            return 0

    else:
        if 'X' in check:
            return 0

    return 1


def ttt(arr):
    win = []
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] and arr[i][0] != '.':
            win.append(arr[i][0])

        if arr[0][i] == arr[1][i] == arr[2][i] and arr[0][i] != '.':
            win.append(arr[0][i])

    center = arr[1][1]
    if center != '.':
        if arr[0][0] == arr[2][2] == center:
            win.append(center)
        if arr[2][0] == arr[0][2] == center:
            win.append(center)
    return win


board = ["...", "...", "..."]


print(solution(board))