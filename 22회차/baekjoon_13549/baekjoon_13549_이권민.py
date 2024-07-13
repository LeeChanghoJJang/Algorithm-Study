from collections import deque
N,K = map(int, input().split())
# 전진,후진,순간이동

limit = 100001
time = [0]*limit
 
def bfs(x,y):
    q = deque()
    if x == 0 :
        q.append(1)
    else :
        q.append(x)
    
    while q:
        x = q.popleft()
        if y == x :
            return time[x]
        
        for nx in (x-1,x+1,x*2):
            if 0 <= nx < limit and time[nx]==0:
                if nx == 2*x :
                    time[nx] = time[x]
                    q.appendleft(nx)
                else : 
                    time[nx] = time[x] + 1
                    q.append(nx)
 
if N==0:
    if K==0:
        print(0)
    else:
        print(bfs(N,K)+1)
else :
    print(bfs(N,K))
