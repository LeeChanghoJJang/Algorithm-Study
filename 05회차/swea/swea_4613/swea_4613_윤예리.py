import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]
    min_value = n*m

    # 순열 구하기
    ls = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                ls.append([i, j, k])

    for i in ls:
        cnt = 0

        # 흰 색
        for j in range(i[1]):
            for k in range(m):
                if arr[j][k] != 'W':
                    cnt += 1
        # 파란색
        for j in range(i[1], i[2]):
            for k in range(m):
                if arr[j][k] != 'B':
                    cnt += 1
        # 빨간색
        for j in range(i[2], n):
            for k in range(m):
                if arr[j][k] != 'R':
                    cnt += 1

        if cnt < min_value:
            min_value = cnt

    print(min_value)