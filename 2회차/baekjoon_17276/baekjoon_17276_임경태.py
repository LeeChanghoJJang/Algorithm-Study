# 17276 배열 돌리기

import sys
sys.stdin = open("input.txt")

# 회전시킬 숫자들을 다른 배열에 저장
def write_num():
    save = [[0] * 8 for _ in range(size//2)]

    for l in range(size//2):
        for r in range(8):
            ni = size//2 + di[r] * (l+1)
            nj = size//2 + dj[r] * (l+1)
            save[l][r] = arr[ni][nj]
    
    return save

# 숫자를 회전하기 위해 델타탐색 인덱스를 회전
def rotate_num():
    turn = (degree // 45) % 8

    # 시계 방향
    if turn > 0:
        for _ in range(turn):
            di.append(di.pop(0))
            dj.append(dj.pop(0))
    # 반시계 방향
    else:
        for _ in range(-turn):
            di.insert(0, di.pop())
            dj.insert(0, dj.pop())

    return di, dj

# 회전시킨 숫자들을 배열에 입력
def read_num():
    for l in range(size//2):
        for r in range(8):
            ni = size//2 + di[r] * (l+1)
            nj = size//2 + dj[r] * (l+1)
            arr[ni][nj] = save[l][r]
    
    return arr

# 메인 실행
for tc in range(int(input())):
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    size, degree = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(size)]

    save = write_num()
    di, dj = rotate_num()
    arr = read_num()

    for i in range(size):
        print(*arr[i])

'''
Python3 : 50236KB / 840ms
PyPy3 : 124192KB / 500ms
'''