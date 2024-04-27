# 2239 스도쿠

# 백트래킹 (188번 반복) / 140452KB / 4024ms
def valid(r, c, n):
    for k in range(9):
        if arr[r][k] == n: return
        if arr[k][c] == n: return
    for i in range((r//3)*3, (r//3)*3+3):
        for j in range((c//3)*3, (c//3)*3+3):
            if arr[i][j] == n: return
    return 1

def solve(depth):
    if depth == len(zeros):
        for r in arr:
            print(*r, sep='')
        exit()

    r, c = zeros[depth]
    for n in range(1, 10):
        if valid(r, c, n):
            arr[r][c] = n
            solve(depth+1)
            arr[r][c] = 0

arr, zeros = [], []
for r in range(9):
    row = list(map(int, input()))
    for c, n in enumerate(row):
        if not n: zeros.append((r, c))
    arr.append(row)

solve(0)


# 완전 탐색 - 시간 초과 (405번 반복)
'''
def check(r, c):
    nums = {0,1,2,3,4,5,6,7,8,9}

    for k in range(9):
        nums.discard(arr[r][k])
        nums.discard(arr[k][c])
    
    if len(nums) == 1: return nums.pop()

    for i in range((r//3)*3, (r//3)*3+3):
        for j in range((c//3)*3, (c//3)*3+3):
            nums.discard(arr[i][j])

    if len(nums) == 1: return nums.pop()

    return 0

arr = [list(map(int, input())) for _ in range(9)]

while sum(sum(arr[i]) for i in range(9)) != 405:
    for r in range(9):
        for c in range(9):
            if not arr[r][c]:
                arr[r][c] = check(r, c)
for i in arr:
    print(*i)
'''