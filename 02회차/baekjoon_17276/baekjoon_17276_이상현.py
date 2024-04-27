# 백준 17276번 배열 돌리기

# 달팽이 숫자를 이용하여 접근
T = int(input())

# 시계 방향으로 45도 회전을 하는 함수를 정의
def rotation_45deg(temp, d):
    n = len(matrix)
    visited = [[0] * n for _ in range(n)]
    num = []
    num_list = []
    row = col = 0
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0

    # 달팽이 숫자처럼 배열의 바깥쪽부터 각 수를 탐색하여 회전해야하는 수를 
    # 따로 num_list에 저장
    for i in range(1, n * n + 1):
        visited[row][col] = 1

        if row == n // 2 or col == n // 2 or row == col or row == n - 1 - col:
            num.append(temp[row][col])

        if len(num) and len(num) % 8 == 0:
            num_list.append(num)
            num = []

        nrow, ncol = row + d[direction][0], col + d[direction][1]

        if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol]:
            row, col = nrow, ncol

        else:
            direction += 1
            direction %= 4
            row, col = row + d[direction][0], col + d[direction][1]

    # num_list에 저장된 회전해야할 수를 회전해줌(순서를 바꿔줌)
    for list_ in num_list:
        list_.insert(0, list_.pop())
        list_.reverse()

    index = row = col = direction = 0
    visited = [[0] * n for _ in range(n)]


    # 달팽이 숫자처럼 배열의 각 수를 탐색하여 회전해야하는 수를 업데이트
    for i in range(1, n * n):
        visited[row][col] = 1

        if row == n // 2 or col == n // 2 or row == col or row == n - 1 - col:
            temp[row][col] = num_list[index].pop()

        if len(num_list[index]) == 0:
            index += 1

        nrow, ncol = row + d[direction][0], col + d[direction][1]

        if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol]:
            row, col = nrow, ncol

        else:
            direction += 1
            direction %= 4
            row, col = row + d[direction][0], col + d[direction][1]

    return temp

for tc in range(T):
    n, d = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # d의 범위가 -360 에서 360까지이므로 360을 더해 양수로 변환해줌
    # 그 후 360으로 나눈 나머지를 d에 할당
    d = (d + 360) % 360

    while d > 0:
        matrix = rotation_45deg(matrix, d)
        d -= 45

    [print(*row) for row in matrix]