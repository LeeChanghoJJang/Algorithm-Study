
def backtrack(i=0,j=0,cnt=1):
    global ans
    ans = max(ans,cnt)
    for dx,dy in dr :
        di,dj = i+dx, j+dy
        if 0 <= di < N and 0 <= dj < M and not visit[ord(arr[di][dj])-65] :
            visit[ord(arr[di][dj])-65] = True
            backtrack(di,dj,cnt+1)
            visit[ord(arr[di][dj])-65] = False

ans = 0

N,M = map(int,input().split())

arr = [list(input()) for _ in range(N)]

visit = [False] * 26

visit[ord(arr[0][0])-65] = 1

backtrack()

print(ans)


###########


from collections import deque

dr = ((1,0),(0,1),(-1,0),(0,-1))

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

visit = [[set() for _ in range(M)] for _ in range(N)]  # set 는 O(1)


q = deque([(0, 0, arr[0][0], 1)])
visit[0][0].add(arr[0][0])

while q :
    i, j , tmp, cnt = q.popleft()
    cnt = max(cnt, len(tmp))
    
    for dx,dy in dr :
        di, dj = i+dx , j +dy

        if 0 <= di < N and 0 <= dj < M and arr[di][dj] not in tmp:

            if tmp+arr[di][dj] not in visit[di][dj] :
                visit[di][dj].add((tmp + arr[di][dj]))
                q.append((di, dj, tmp + arr[di][dj], cnt+1))

print(cnt)