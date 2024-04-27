# 백준 2630번 색종이 만들기
import sys
sys.stdin = open('input.txt')

n = int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
cnt_0 = cnt_1 = 0
def judge(x,y, N):
    global cnt_0
    global cnt_1
    check = True
    if N==1:
        if arr[x][y]==1:
            cnt_1 +=1
        else:
            cnt_0 +=1
        return
    else:
        for i in range(x,x+N):
            for j in range(y,y+N):
                if arr[i][j] !=arr[x][y]:
                    check = False
                    break
            if check ==False:
                judge(x + N // 2, y, N // 2)
                judge(x, y + N // 2, N // 2)
                judge(x + N // 2, y + N // 2, N // 2)
                judge(x, y, N // 2)
                break
        else:
            if arr[x][y] ==1:
                cnt_1 +=1
            else:
                cnt_0 +=1
            return


judge(0,0,n)
print(cnt_0)
print(cnt_1)
