# 1891 / 사분면 / 골드4

# 인덱스 추적
def get_idx(n, i=0, r=0, c=0):
    if n < 1: return r-y, c+x
    if num[i] == '1': return get_idx(n//2, i+1, r, c+n)
    elif num[i] == '2': return get_idx(n//2, i+1, r, c)
    elif num[i] == '3': return get_idx(n//2, i+1, r+n, c)
    elif num[i] == '4': return get_idx(n//2, i+1, r+n, c+n)

# 사분면 번호 제작
def make_num(n, r, c, ans=''):
    if n < 1: print(ans)
    elif r < n and c >= n: make_num(n//2, r, c-n, ans+'1')
    elif r < n and c < n: make_num(n//2, r, c, ans+'2')
    elif r >= n and c < n: make_num(n//2, r-n, c, ans+'3')
    elif r >= n and c >= n: make_num(n//2, r-n, c-n, ans+'4')

d, num = input().split(); n = 2**(int(d)-1)
x, y = map(int, input().split())
row, col = get_idx(n)

if 0 <= row < 2*n and 0 <= col < 2*n:
    make_num(n, row, col)
else:
    print(-1)

'''
31120KB / 40ms
'''


# 메모리 초과
'''
def div_conq(n, i, j, quad):
    if len(quad) == d:
        arr[i][j] = quad
        return
    div_conq(n//2, i, j + n, quad + "1")
    div_conq(n//2, i, j, quad + "2")
    div_conq(n//2, i + n, j, quad + "3")
    div_conq(n//2, i + n, j + n, quad + "4")

d, num = map(int, input().split())
x, y = map(int, input().split())
N = int(4 ** (d / 2))
arr = [[0] * N for _ in range(N)]

div_conq(N//2, 0, 0, '')

for i in range(N):
    for j in range(N):
        if arr[i][j] == str(num):
            row, col = i, j
            break
try:
    print(arr[row-y][col+x])
except:
    print(-1)
'''