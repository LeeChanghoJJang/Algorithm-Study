import sys
import copy
from itertools import permutations

sys.stdin = open('input.txt')
dx = [1,0,-1,0]
dy = [0,-1,0,1]
# rotation 함수 정의 
def rotation(x,y,wing,arr2,arr):
    x-=1
    y-=1
    visited = [[0] * M for _ in range(N)]
    visited[x][y] =1
    # 처음에 있었던 x,y를 저장하는 이유는
    # 순회하면서 nx,ny와 처음 x,y의 차이를 벗어난 경우를 활용할 것이기 때문
    original_x, original_y = x,y
    # 바깥쪽부터 순차적으로 반복문 돌리기
    for s in range(wing,0,-1):
        i = 0
        # 순회 시작점을 바깥쪽부터 하기 때문에, 바꿔줌 
        trans_y = y + s
        cnt = 0
        # 바깥쪽을 돌때는 8의 배수만큼만 돌면 되더라고(합차공식 쓰면 이유 알게됨)
        while cnt < s*8:
            nx,ny  = x + dx[i], trans_y + dy[i]
            # 주어진 행렬의 범위를 벗어나지 않거나, wing의 범위를 벗어나지 않는 다면 
            if 0 <=nx < N and 0<= ny <M and abs(nx - original_x) <= s and abs(ny-original_y) <=s and not visited[nx][ny]:
                cnt +=1
                visited[nx][ny]=1
                arr2[nx][ny] = arr[x][trans_y]
                x, trans_y = nx,ny
            else:
                # 방향전환
                i =(i+1)%4
    return arr2

N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
orders = []
# 여기에는 중심점과 날개정보를 저장
for i in range(K):
    orders.append(tuple(map(int,input().split())))

min_val = int(1e9)
# 더 간단하게도 가능할 것 같으나, 직관적인게 안떠올라서 이대로 함
for i in permutations(orders,K):
    # arr2 : 변경용, arr3 : 비교용
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)
    for x,y,wings in i:
        arr2 = rotation(x,y,wings,arr2,arr3)
        arr3 = copy.deepcopy(arr2)
    for j in arr2:
        temp_sum = sum(j)
        if min_val > temp_sum:
            min_val = temp_sum

print(min_val)
