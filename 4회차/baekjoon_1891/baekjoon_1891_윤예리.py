'''
1. 첫 줄에 도착한 사분면 번호를 좌표값으로 계산한다.
2. 이동시킨다.
3. 이동한 좌표의 사분면 번호를 계산한다.
'''

# 조각 위치 찾는 함수
def pos(num, index, i, j, size):
    # print(i, j)
    if size == 0:
        return i, j

    if num[index] == '1':      # 1사분면
        return pos(num, index+1, i, j+size, size//2)
    elif num[index] == '2':    # 2사분면
        return pos(num, index+1, i, j, size//2)
    elif num[index] == '3':    # 3사분면
        return pos(num, index+1, i+size, j, size//2)
    elif num[index] == '4':    # 4사분면
        return pos(num, index+1, i+size, j+size, size//2)

# 사분면 찾는 함수
def find(i, j, size, result):
    # print(result)
    if size == 0:
        return result
    else:
        if 0<=i<size and size<=j<size*2:    # 1사분면
            return find(i, j-size, size//2, result+'1')
        elif 0<=i<size and 0<=j<size:       # 2사분면
            return find(i, j, size//2, result+'2')
        elif size<=i<size*2 and 0<=j<size:    # 3사분면
            return find(i-size, j, size//2, result+'3')
        elif size<=i<size*2 and size<=j<size*2:      # 4사분면
            return find(i-size, j-size, size//2, result+'4')

d, quad = map(int, input().split())
x, y = map(int, input().split())
q = str(quad)

r, c = pos(q, 0, 0, 0, 2**(d-1))
# print(r, c)
new_r = r-y
new_c = c+x
# print(r, c, new_r, new_c)
if 0<=new_r<2**d and 0<=new_c<2**d:
    print(find(new_r, new_c, 2**(d-1), ''))
else:   # 존재하지 않는 사분면인 경우에는 -1을 출력한다.
    print(-1)


