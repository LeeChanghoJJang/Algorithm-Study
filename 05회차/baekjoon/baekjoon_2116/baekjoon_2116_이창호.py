import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
# col 색깔 하나가 정해지면 나머지 하나를 정해주는 함수
def trans(col):
    if col in [1,3]:
        result = 4-col
    elif col in [0,5]:
        result = 5-col
    elif col in [2,4]:
        result = 6-col
    return result
# 주사위 한 면이 정해지면 일자로 세웠을 때 나머지 한면은 정해짐
def dice(row,value,result):
    global max_val
    if row == T:
        temp =0
        for i in range(T):
            temp += max(result[i])
        if max_val < temp:
            max_val = temp
        return

    for next_col in range(6):
        # 이전 주사위의 반대편 면에 해당되는 값의 열 인덱스를 찾음
        if dicer[row][next_col] == value:
            col = next_col
            # 거기에 반대위치에 있는 열
            col2 = trans(col)
            # 그 열의 값 
            value2 = dicer[row][col2]
            # 해당 열의값과 반대편의 값을 result에 추가
            result.append(eyes - {dicer[row][col],dicer[row][col2]})
            dice(row + 1, value2, result)
            result.pop()

T = int(input())
dicer = []
for tc in range(T):
    num1,num2,num3,num4,num5,num6 = map(int,input().split())
    dicer.append([num1,num2,num3,num4,num5,num6])
max_val = 0
eyes = set(range(1,7))
for i in range(1,7):
    dice(0,i,[])
print(max_val)
