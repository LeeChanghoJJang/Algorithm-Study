import sys
sys.stdin = open('input.txt')

def find_number(obj):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == obj:
                visited[i][j]=1

def Bingo():
    result = 0
    # 가로검사
    for i in range(5):
        if sum(visited[i])==5:
            result +=1

    # 세로검사
    for j in range(5):
        temp = 0
        for i in range(5):
            if visited[i][j] ==1:
                temp +=1
        if temp==5:
            result +=1

    # 대각선 검사
    temp1 = 0
    temp2 = 0
    for i in range(5):
        if visited[i][i] ==1:
            temp1 +=1
        if visited[i][4-i]==1:
            temp2 +=1
    # 5개 채워지면
    if temp1 ==5:
        result += 1
    if temp2 ==5:
        result +=1
    # 빙고가 3개 이상이면 True
    if result >=3:
        return True
    return False


bingo = [list(map(int,input().split())) for _  in range(5)]
moderator=[]
visited = [[0] * 5 for _ in range(5)]
# 사회자가 부르는 넘버를 그냥 순차적으로 부르기 위해 1차원 배열에 담음
for _ in range(5):
    moderator.extend(list(map(int,input().split())))

cnt= 0
# 사회자가 부르는거 순차적으로
for obj in moderator:
    cnt+=1
    find_number(obj)
    # 몇번째 불렀을 때 빙고인지
    if cnt >=5 and Bingo():
        print(cnt)
        break

