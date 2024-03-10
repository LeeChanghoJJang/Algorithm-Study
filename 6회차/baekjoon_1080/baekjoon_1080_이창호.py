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
# 바뀐 횟수를 저장하기 위한 변수 cnt 저장
cnt = 0
# 행과 열의 길이가 3이상인 경우에 모든 행렬 반복
if N >=3 and M>=3:
    # 시작점을 기준, 3행 3열크기를 고려하여 모든 행렬 순회 
    for i in range(N-2):
        for j in range(M-2):
            # 하나라도 불일치 할경우, check 함수를 통해 모두 변경 
            if arr1[i][j] != arr2[i][j]:
                check(i,j)
                cnt += 1
# 작은 경우에는 바꿀수 없으므로 -1
else:
    cnt = -1
# 순회했음에도 불구하고, 불일치하다면 -1
if arr1 != arr2:
    cnt =-1
print(cnt)
