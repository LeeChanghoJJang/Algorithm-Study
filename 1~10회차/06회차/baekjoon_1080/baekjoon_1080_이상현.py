# 백준 1080번 행렬

# row, col을 왼쪽 최상단 원소로 가지는 3x3 행렬의
# 모든 원소를 뒤집는 함수
def change(row, col):
    for r in range(3):
        for c in range(3):
            A[row + r][col + c] = +(not A[row + r][col + c])

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]
cnt = 0

# N 또는 M 중 하나라도 3보다 작은 값이 있다면
# 뒤집기를 실행할 수 없음
if N >= 3 and M >= 3:
    # (0, 0)에서 (N - 2, N - 2)까지 순회하며 그 위치에서
    # A의 행렬과 B행렬의 값이 다르다면 뒤집는 함수 실행 후
    # cnt의 값을 1 증가
    for row in range(N - 2):
        for col in range(M - 2):
            if A[row][col] != B[row][col]:
                change(row, col)
                cnt += 1

print(cnt if A == B else -1)