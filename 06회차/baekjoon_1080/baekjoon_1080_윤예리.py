def change(r, c):
    for i in range(3):
        for j in range(3):
            A[r+i][c+j] = 1 - A[r+i][c+j]

def count_():
    cnt = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                change(i, j)
                cnt += 1

            if A == B:
                return cnt
    return -1


n, m = map(int, input().split())

A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]
if A == B:
    print(0)
else:
    print(count_())

# 3x3을 행 별로 비교해서 2행 이상 B와 다르면 3x3을 바꾼다.
# def find():
#     global result
#
#     for i in range(n - 2):
#         for j in range(m - 2):
#             if A == B:
#                 return
#
#             cnt = 0
#             for k in range(3):
#                 if A[i + k][j:j + 3] != B[i + k][j:j + 3]:
#                     cnt += 1
#
#             if cnt > 1:
#                 result += 1
#                 for r in range(3):
#                     for c in range(3):
#                         A[i+r][j+c] = 1 - A[i+r][j+c]
#
#     if A == B:
#         return
#     else:
#         result = -1
#
# n, m = map(int, input().split())
# if n < 3 or m < 3:
#     exit(print(-1))
#
# A = [list(map(int, input())) for _ in range(n)]
# B = [list(map(int, input())) for _ in range(n)]
# result = 0
# find()
# print(result)




# 가로 한 줄 / 세로 한 줄이 B와 다르면 3x3을 바꾼다.
# 틀렸습니다.
#
# for i in range(n-2):
#     for j in range(m-2):
#         if A == B:
#             break
#
#         # 가로 한 줄이 다 B와 반대면 바꾼다.
#         check = 0
#         for k in range(j, j+3):
#             # if 1 - A[i][k] == B[i][k]:
#             if abs(A[i][k] - 1) == B[i][k]:
#                 check += 1
#         if check == 3:
#             for r in range(i, i+3):
#                 for c in range(j, j+3):
#                     A[r][c] = abs(A[r][c] - 1)
#             cnt += 1
#
#         else:        # 세로도 확인
#             check = 0
#             for k in range(i, i+3):
#                 # if 1 - A[k][j] == B[k][j]:
#                 if abs(A[k][j] - 1) == B[k][j]:
#                     check += 1
#             if check == 3:
#                 for r in range(i, i+3):
#                     for c in range(j, j+3):
#                         A[r][c] = abs(A[r][c] - 1)
#                 cnt += 1
#
# if A == B:
#     print(cnt)
# else:
#     print(-1)