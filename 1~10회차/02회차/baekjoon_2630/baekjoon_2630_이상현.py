# 백준 2630번 색종이 만들기

# 왼쪽 위 꼭지점의 좌표가 row, col인 N x N 사각형내에 잘라진 하얀색 색종이와
# 파란색 색종이의 개수를 구하는 함수
def count_(row, col, N) :
    global white, blue

    # 가장 왼쪽 위 종이의 색을 color 변수에 저장
    color = list_[row][col]

    for i in range(N) :
        for j in range(N) :

            # 만약 N x N 정사각형 안에 color와는 다른 색을 가진 색종이가
            # 존재한다면 현재의 정사각형을 4개로 분할하여 각각 count 함수 호출
            if color != list_[row + i][col + j]:
                count_(row, col, N // 2)
                count_(row, col + N // 2, N // 2)
                count_(row + N // 2, col, N // 2)
                count_(row + N // 2, col + N // 2, N // 2)

                # 정사각형 안의 종이들의 색이 모두 같을 때만
                # 하얀색 종이, 파란색 종이의 개수를 세어야 하므로
                # 다른 경우에는 return을 해줌
                return True

    if color == 0:
        white += 1

    else:
        blue += 1

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
white = blue = 0

# 처음에는 가장 큰 정사각형부터 계산
count_(0, 0, N)

print(f'{white}\n{blue}')