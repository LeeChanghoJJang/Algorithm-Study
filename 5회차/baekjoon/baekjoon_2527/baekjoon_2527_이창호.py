import sys
sys.stdin = open('input.txt')
def solution(left_square, right_square):
    x1, y1, x2, y2 = left_square[0], left_square[1], left_square[2], left_square[3]
    p1, q1, p2, q2 = right_square[0], right_square[1], right_square[2], right_square[3]

    # 공통부분 없음
    if (x2 < p1) or (p2 < x1) or (q1 > y2) or (y1 > q2):
        return "d"

    # 점 1개에서 만날 때
    if (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2) or (x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1):
        return "c"

    # 변이 만날 때
    if p1 == x2 or x1 == p2 or y1 == q2 or y2 == q1:
        return "b"

    # 나머지 직사각형(겹칠때)
    return "a"


for _ in range(4):
    temp = list(map(int, input().split()))
    left_square = [temp[i] for i in range(4)]  # 왼쪽 직사각형
    right_square = [temp[i] for i in range(4, 8)]  # 오른쪽 직사각형
    print(solution(left_square, right_square))