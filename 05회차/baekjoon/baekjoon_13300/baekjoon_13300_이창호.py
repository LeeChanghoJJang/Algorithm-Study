import sys
sys.stdin = open('input.txt')
# N : 학생수, K : 한방에 최대 인원수
N,K = map(int,input().split())
cnt = 0
# 6학년까지, 남여방을 temp에 저장 
temp = [[0]*6 for _ in range(2)]
# S가 0은 여자, 1은 남자
# 인덱스 에러 방지를 위해 학년은 1빼서 저장 
for _ in range(N):
    S, Y = map(int,input().split())
    temp[S][Y-1] +=1
# 최소방은 1개이며, K개 단위로 1개씩 가산하여 cnt에 저장
for i in range(len(temp)):
    for j in range(len(temp[0])):
        cnt += (temp[i][j]-1)//K+1
print(cnt)
