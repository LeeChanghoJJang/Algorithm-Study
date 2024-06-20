import copy
dx, dy = [0,1,0,-1],[1,0,-1,0]

def backtrack(i, result) :
    global min_value
    if i == K:                          # 백트래킹 완료 시
        for j in result:                # 최소값 비교
            if min_value > sum(j):
                min_value = sum(j)

    for idx in range(K):
        if visit[idx] == 0 :
            visit[idx]=1
            backtrack(i+1, rotate(*rot[idx], result))       # 백트래킹
            visit[idx]=0


def rotate(r,c,s, lst) :
    # 3 4 2 면 범위는 0<= i <= 4 , 1<= j <= 5
    # (3,4) > (2,3) 을 기준으로 2-s <= x <= 2+s
    r,c = r-1 ,c-1
    new_arr = copy.deepcopy(lst)
    for idx in range(1,s+1):
        dt = 0
        i = r-idx
        j = c-idx
        while True :            # 달팽이랑 비슷한 방식 사용 
            tmp=lst[i][j]
            i += dx[dt]
            j += dy[dt]
            new_arr[i][j] = tmp
            if not (r-idx<=i+dx[dt]<=r+idx and c-idx<=j+dy[dt]<=c+idx):
                dt += 1
            if dt == 4 :
                break
    return new_arr          # 수정된 리스트를 반환

N,M,K = map(int,input().split())    # N : 가로 / M : 세로 / K : 회전

arr = [list(map(int,input().split())) for _ in range(N)]
rot = [list(map(int,input().split())) for _ in range(K)]
min_value = 25001       # 최대값 (100 * 50 * 50)
visit = [0]*K

backtrack(0,arr)
print(min_value)