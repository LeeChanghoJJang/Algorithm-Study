import sys
sys.stdin = open('input.txt')
# 3행 3열 점검하는 함수
def check(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if arr1[x][y] =='1':
                arr1[x][y] = '0'
            else:
                arr1[x][y] = '1'

N, M = map(int,input().split())
# 입력 행렬
arr1 = [list(input()) for _ in range(N)]
# 비교 행렬
arr2 = [list(input()) for _ in range(N)]
cnt = 0
# 행과 열의 길이가 3이상인 경우에 모든 행렬 반복
if N >=3 and M>=3:
    for i in range(N-2):
        for j in range(M-2):
            if arr1[i][j] != arr2[i][j]:
                check(i,j)
                cnt += 1
#
else:
    cnt = -1
if arr1 != arr2:
    cnt =-1
print(cnt)