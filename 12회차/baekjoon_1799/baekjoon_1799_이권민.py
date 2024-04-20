# # 해당 위치에 비숍이 존재할 때 최대값 해당 위치에 저장
# # visited 체크. 가능한 곳 차례대로 들어가보면서 dfs 들어갈때 visited 체크 나올때 풀고
# # 들어갈때 못가는 곳 갱신.

# def BackTrack(r,c,lst,cnt):
#   global max_cnt


#   if max_cnt < cnt:
    
#     max_cnt = cnt
#   for i in range(N):
#     for j in range(N):
#       if matrix[i][j] == 1 and (i+j not in lst or i-j not in lst):
#         # ban_pl_cnt로 종료조건 설정하려면 lst 로 if문 돌리면 안됨. 저기 matrix값은 0으로 설정이 안됐거든
#         matrix[i][j] = 0
#         lst.add(i+j)
#         lst.add(i-j)
#         BackTrack(i, j, lst, cnt+1)
#         lst.discard(i+j)
#         lst.discard(i-j)
#         matrix[i][j] =1
#         # i+j == i-j 인 경우

#         # 이번턴에서 셌다
        
  
    
  

# N = int(input())
# matrix = []
# for i in range(N):
#   matrix.append(list(map(int,input().split())))

# max_cnt = 0
# for i in range(N):
#   for j in range(N):
#     if matrix[i][j] == 1:
#       matrix[i][j] = 0
#       BackTrack(i, j, set([i+j, i-j]), 1)


# print(max_cnt)

# 우하향 대각선, 우상향 대각선 분류 후 따로 체크

# 대각선으로 된 순열 문제였구나


# 우상향 대각선당 비숍이 놓일 때마다 그 좌표에 해당하는 우하향 대각선을 체크
# 가능한 곳을 마이너스?
import sys

# 재귀 호출의 깊이 한계를 늘림
sys.setrecursionlimit(10 ** 8)

# 입력을 더 효율적으로 받기 위해 람다 함수로 재정의
input = lambda: sys.stdin.readline().rstrip()

# 입력으로 주어진 체스판의 크기
n = int(input())

# 체스판을 나타내는 이차원 리스트
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

# 우하향 대각선에 해당하는 좌표를 키로 가지는 딕셔너리
rd = {}
# 중앙을 기준으로 좌표를 표시
# (y,x) -> rd[x-y], 왼쪽 아래가 -(n-1), 오른쪽 위가 (n-1)
for i in range(-n + 1, n):
    rd[i] = 0  # 초기화

# 현재 좌표가 유효한 범위 내에 있는지를 확인하는 함수
def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 현재 대각선에서부터 끝 대각선까지 뽑힐 가능성이 있는 좌표의 개수를 반환하는 함수
# 같은 우하향 대각선에 있더라도
# 연산 수  줄이는 포인트. 이거 빼면 그냥 순열
def upper_bound(diag):
    able_rus = 0  # 가능한 우상향 대각선들의 개수
    for d in range(diag, 2 * n - 1):
        for y in range(d + 1):
            x = d - y
            # 현재 좌표가 유효하고, 비숍을 놓을 수 있으며, 우하향 대각선에 비숍이 없는 경우
            if in_range(y, x) and board[y][x] and rd[x - y] == 0:
                able_rus += 1
                break
    return able_rus

# 재귀적으로 모든 가능한 비숍의 배치를 탐색하는 함수
def f(diag, cnt):
    global ans

    # 최대로 놓을 수 있는 비숍의 개수를 갱신
    if ans < cnt:
        ans = cnt

    # 현재 대각선에서부터 끝 대각선까지 탐색
    if diag == 2 * n:
        return

    # 현재 대각선에서 최대로 더 놓을 수 있는 비숍의 개수를 상한으로 설정
    ub = upper_bound(diag)

    # 현재 비숍의 개수와 상한을 합쳐도 기존 최대 개수보다 작으면 더 이상 진행할 필요가 없음
    if ub + cnt <= ans:
        return

    # 현재 대각선에서 가능한 모든 비숍의 위치를 탐색
    # diag = x+y
    # 우하향 그래프 rd[x-y]
    for y in range(diag + 1):
        x = diag - y
        if in_range(y, x) and board[y][x] and rd[x - y] == 0:
            rd[x - y] = 1  # 비숍을 놓음
            f(diag + 1, cnt + 1)  # 다음 우상향 대각선으로 이동
            rd[x - y] = 0  # 비숍을 제거

    # 현재 대각선에서 비숍을 놓지 않는 경우
    f(diag + 1, cnt)

# 최대로 놓을 수 있는 비숍의 개수
ans = 0

# 첫 번째 대각선부터 시작하여 모든 가능한 경우 탐색
f(0, 0)

# 결과 출력
print(ans)



      
      
      
      