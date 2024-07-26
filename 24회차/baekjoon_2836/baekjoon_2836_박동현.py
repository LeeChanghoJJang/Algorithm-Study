import sys
input = sys.stdin.readline
N,M=map(int,input().split())
data=dict()
for _ in range(N):
    a,b=map(int,input().split())
    if a<b: continue
    data[b]=max(data.get(b,0),a)
start,end = 0,0
for s,e in sorted(data.items()):
    if end<s:
        M+=2*(end-start)
        start=s
    end=max(end,e)
print(M+2*(end-start))