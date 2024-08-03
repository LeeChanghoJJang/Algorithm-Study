import sys
input = sys.stdin.readline 


dr = (0,-1),(-1,0),(0,1),(1,0)

M,N = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

visit =  [[0]*M for _ in range(N)]
data = dict()
cnt = 0
max_value = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            cnt += 1
            stack = [(i,j)]
            tmp = 0 
            while stack:
                x,y = stack.pop()

                if visit[x][y]: continue
                visit[x][y] = cnt
                tmp += 1
                for b in range(4):
                    if not arr[x][y]&2**b:
                        dx,dy = dr[b]
                        di,dj = x+dx,y+dy
                        if not visit[di][dj]:
                            stack.append((di,dj))
            data[cnt]=tmp
            max_value = max(max_value, tmp)
            

max_sum = 0
for i in range(N):
    for j in range(M):
        for dx,dy in dr:
            di,dj = i+dx,j+dy
            if 0<=di<N and 0<=dj<M:
                if visit[i][j] == visit[di][dj]: continue
                max_sum=max(max_sum, data[visit[i][j]]+data[visit[di][dj]])

print(cnt)
print(max_value)
print(max_sum)