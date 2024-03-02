import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
cnt = 0
temp = [[0]*6 for _ in range(2)]
for _ in range(N):
    S, Y = map(int,input().split())
    temp[S][Y-1] +=1
for i in range(len(temp)):
    for j in range(len(temp[0])):
        cnt += (temp[i][j]-1)//K+1
print(cnt)