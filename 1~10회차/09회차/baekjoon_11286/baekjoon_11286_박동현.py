import heapq
import sys
input = sys.stdin.readline


q = []
idx = dict()

for _ in range(int(input())):
    num = int(input())
    if num > 0 :
        heapq.heappush(q,num)

    elif num < 0 :
        heapq.heappush(q,-num)
        idx[-num] = idx.setdefault(-num,0) +1
    
    else :
        if q :
            a = heapq.heappop(q)
    
            if a in idx and idx[a]:
                idx[a] -= 1
                print(-a)
    
            else :
                print(a)
    
        else :
            print(0)