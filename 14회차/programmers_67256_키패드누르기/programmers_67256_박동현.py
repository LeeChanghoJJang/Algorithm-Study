# 키패드 누르기
from collections import deque


dr = (1,0),(0,1),(0,-1),(-1,0)

def bfs(position,number):
    arr = [[1,2,3],
          [4,5,6],
          [7,8,9],
          ["*",0,"#"]]
    
    visit = [[0]*3 for _ in range(4)]
    for i in range(4):
        for j in range(3):
            if arr[i][j] == position:
                q = deque([(i,j)])
                visit[i][j] = 1

    while q :
        x,y = q.popleft()
        
        if arr[x][y] == number:
            return visit[x][y]

        for dx,dy in dr :
            di,dj = x+dx, y+dy
            if 0<=di<4 and 0<=dj<3:
                if not visit[di][dj] :
                    visit[di][dj] = visit[x][y] + 1
                    q.append((di,dj))

    

def solution(numbers, hand):
    answer = ''
    leftP = "*"
    rightP = "#"
    
    if hand == "right" : hand = "R"
    else : hand = "L"
    
    for number in numbers:
        
        if number in [1,4,7]:
            answer += "L"
            leftP = number
            
        elif number in [3,6,9]:
            answer += "R"
            rightP = number
            
        else :
            l = bfs(leftP, number)
            r = bfs(rightP, number)
            if l > r :
                answer += "R"
                rightP = number
            elif r > l :
                answer += "L"
                leftP = number
            else :
                answer += hand
                if hand == "R":
                    rightP = number
                else : leftP = number
    return answer