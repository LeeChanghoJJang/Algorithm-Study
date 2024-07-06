from copy import deepcopy

# 2차원 리스트를 시계 방향으로 90도 회전시키는 함수
def rotate(list_, size):
    new_list = deepcopy(list_)
    for row in range(size):
        for col in range(size):
            new_list[size - col - 1][row] = list_[row][col]
    return new_list

# 리스트를 왼쪽으로 이동시키고 병합하는 함수
def merge(list_):
    # 0이 아닌 숫자만 필터링
    temp = [i for i in list_ if i]

    for i in range(1, len(temp)):
        # 연속된 같은 숫자가 있다면 합치기
        if temp[i] == temp[i - 1]:
            temp[i - 1] *= 2
            temp[i] = 0
    # 0이 아닌 숫자만 남기고 나머지는 0으로 채움
    temp = [i for i in temp if i]
    return temp + [0] * (len(list_) - len(temp))

# 깊이 우선 탐색으로 최대 점수를 계산하는 함수
def dfs(list_, size, depth):
    # 현재 보드에서 가장 큰 값 찾기
    max_ = max([max(row) for row in list_])
    # 깊이가 0이면 현재 최대 값 반환
    if depth == 5:
        return max_

    # 네 방향으로 보드를 회전하면서 각각의 경우 계산
    for _ in range(4):
        new_list = [merge(row) for row in list_]
        # 현재 보드와 회전 후 보드가 다르다면 계속 탐색
        if new_list != list_:
            max_ = max(max_, dfs(new_list, size, depth + 1))
        # 보드를 시계 방향으로 90도 회전
        list_ = rotate(list_, size)
    return max_

# 입력 받기
N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]

# 깊이 우선 탐색 호출하여 결과 출력
print(dfs(list_, N, 0))