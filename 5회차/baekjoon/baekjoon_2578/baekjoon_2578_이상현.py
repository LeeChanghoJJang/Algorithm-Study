def chk_bingo():
    cnt = sum(row.count(0) == 5 for row in bingo)
    cnt += sum(col.count(0) == 5 for col in list(zip(*bingo)))
    cnt += all(bingo[row][row] == 0 for row in range(5))
    cnt += all(bingo[row][4 - row] == 0 for row in range(5))

    if cnt >= 3:
        return True
    return False

bingo = [list(map(int, input().split())) for _ in range(5)]
is_bingo = False
dict_ = {}

for row in range(5):
    for col in range(5):
        dict_[bingo[row][col]] = (row, col)

for i in range(5):
    target_list = list(map(int, input().split()))

    for j, target in enumerate(target_list):
        chk = dict_[target]
        bingo[chk[0]][chk[1]] = 0

        if chk_bingo():
            is_bingo = True
            print(5 * i + j + 1)
            break

    if is_bingo:
        break