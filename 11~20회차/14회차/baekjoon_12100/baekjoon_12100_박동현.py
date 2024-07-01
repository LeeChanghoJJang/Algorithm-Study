# 전략 1) : 왼 오 위 아래 함수를 각각 구현 후 백트래킹 (비슷한 함수 네개 짜기 귀찮음)
# 전략 2) : 왼쪽으로 몰아서 합치는데, 그냥 배열을 돌려보기
# 뒤집기 방법 [list(row[::-1]) for row in zip(*arr)]

def move(arr):
    new_arr = [row[:] for row in arr]  # 원래 배열을 변경하지 않고 새로운 배열 생성
    for i in range(N):
        cnt = 0
        now = 0
        for j in range(N):
            if new_arr[i][j] == 0:
                continue

            if now == 0:
                now = new_arr[i][j]
            else:
                if now == new_arr[i][j]:
                    new_arr[i][cnt] = 2 * now
                    now = 0
                    cnt += 1
                else:
                    new_arr[i][cnt] = now
                    now = new_arr[i][j]
                    cnt += 1
            new_arr[i][j] = 0
        if now != 0:
            new_arr[i][cnt] = now

    return new_arr

def rotate(arr):
    return [list(row[::-1]) for row in zip(*arr)]

def backtrack(arr, cnt=0):
    global ans
    if cnt == 5:
        ans = max(max([max(row) for row in arr]), ans)
        return

    for _ in range(4):
        arr = rotate(arr)               # 각 depth 마다 배열을 4번 돌리면서(4번 돌리면 원위치) 
        backtrack(move(arr), cnt + 1)   # move 함수로 숫자를 합친 리스트를 들고 다시 백트래킹

N = int(input())
board = [ [*map(int,input().split())] for _ in range(N) ] 
ans = 0
backtrack(board)
print(ans)