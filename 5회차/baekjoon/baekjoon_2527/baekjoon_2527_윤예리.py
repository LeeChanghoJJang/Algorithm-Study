import sys
sys.stdin = open('input.txt')

for _ in range(4):
    ls = list(map(int, input().split()))

    # 첫 번째 직사각형
    s1 = ls[:4]
    x1 = [i for i in range(s1[0], s1[2]+1)]
    y1 = [i for i in range(s1[1], s1[3]+1)]

    # 두 번째 직사각형
    s2 = ls[4:]
    x2 = [i for i in range(s2[0], s2[2]+1)]
    y2 = [i for i in range(s2[1], s2[3]+1)]

    x_len = min(len(x1), len(x2))
    y_len = min(len(y1), len(y2))

    intersection_x = 0
    intersection_y = 0

    for i in range(x_len):
        if x_len == len(x1):
            if x1[i] in x2:
                intersection_x += 1
        else:
            if x2[i] in x1:
                intersection_x += 1

    for j in range(y_len):
        if y_len == len(y1):
            if y1[j] in y2:
                intersection_y += 1
        else:
            if y2[j] in y1:
                intersection_y += 1

    # intersection_x = list(set(x1) & set(x2))
    # intersection_y = list(set(y1) & set(y2))

    if intersection_x > 1 and intersection_y > 1:       # 겹치는 부분이 직사각형
        print('a')
    elif intersection_x == 0 and intersection_y == 0:   # 겹치는 부분이 아예 없을 때
        print('d')
    elif intersection_x == 1 and intersection_y == 1:   # 점으로 겹칠 때
        print('c')
    elif (intersection_x > 1 and intersection_y == 1) or (intersection_x == 1 and intersection_y > 1):
        print('b')