C,R = map(int,input().split())

K = int(input())

if C*R < K :
    print(0)
else :
    concert = [[0] * C for _ in range(R)]

    dx = [1,0,-1,0]     # 델타를 사용하여 달팽이를 그릴 예정
    dy = [0,1,0,-1]

    cnt = 0
    i, j = 0, 0
    dt = 0
    while True :
        # 카운트를 하나씩 올리면서 ij에 담음
        cnt += 1
        concert[i][j] = cnt
        # j,i 를 뽑는게 목표이므로 cnt를 1씩 올리면서 cnt가 지정된 K가 될때까지 반복
        if cnt == K :
            break
        # 다음 좌표로 이동
        i += dx[dt%4]
        j += dy[dt%4]

        # 변경 조건 1) 갈 자리에 숫자가 이미 들어가있는가?
        if 0 <= i < R and 0 <= j < C:
            if concert[i][j] != 0:
                i -= dx[dt%4]       # i, j에 더했던 값을 도로 물리고
                j -= dy[dt%4]
                dt += 1             # 델타 탐색 계수를 올린 뒤
                i += dx[dt%4]       # 델타를 바꿔 다시 탐색
                j += dy[dt%4]
        # 변경 조건 2) 갈 자리에 인덱스가 없는가?
        else :
            i -= dx[dt%4]           # 이하 동일
            j -= dy[dt%4]
            dt += 1
            i += dx[dt%4]
            j += dy[dt%4]
    # while문이 끝난 후 인덱스를 보정해 출력
    print(j+1, i+1)