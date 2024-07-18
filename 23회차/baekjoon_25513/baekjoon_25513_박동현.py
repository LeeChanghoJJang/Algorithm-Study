from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

arr = [[*map(int,input().split())] for _ in range(5)]
i,j = map(int,input().split())


ans = 0 
# 단순 1 2 3 4 5 6 순회 bfs
for x in range(1,7):
    check = False
    visit = dict()
    visit[(i,j)]=1
    q = deque([(i,j)])
    while q:
        i,j = q.popleft()

        if arr[i][j] == x:
            check = True
            break

        for dx,dy in dr:
            di,dj = i+dx,j+dy
            if 0<=di<5 and 0<=dj<5 and (di,dj) not in visit and arr[di][dj] != -1:
                q.append((di,dj))
                visit[(di,dj)] = visit[(i,j)] + 1

    if check:
        ans += visit[(i,j)]-1
    else :
        exit(print(-1))
print(ans)