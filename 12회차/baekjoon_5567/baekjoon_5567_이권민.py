from collections import deque
n =int(input())
m = int(input())
friendship = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    friendship[a].append(b)
    friendship[b].append(a)
visited=[0]*(n+1)

deq = deque([[1,0]])
visited[1] = 1
cnt = 0
while deq:
    
    cur,depth = deq.popleft()
    
    if friendship[cur]:
        for friend_num in friendship[cur]:
            if visited[friend_num] == 0:
                visited[friend_num] = 1
                cnt += 1
                if depth < 1:
                    deq.append([friend_num,depth + 1])
            
            
print(cnt)
    

    