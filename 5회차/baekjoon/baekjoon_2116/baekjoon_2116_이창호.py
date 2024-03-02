import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
def trans(col):
    if col in [1,3]:
        result = 4-col
    elif col in [0,5]:
        result = 5-col
    elif col in [2,4]:
        result = 6-col
    return result

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
        if dicer[row][next_col] == value:
            col = next_col
            col2 = trans(col)
            value2 = dicer[row][col2]
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
