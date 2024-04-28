import sys

input = sys.stdin.readline


def init_min(start,end,idx=1):
    if start == end :
        min_tree[idx] = arr[start]
    else :
        mid = (start+end) // 2 
        min_tree[idx] = min(init_min(start,mid,idx*2), init_min(mid+1,end,idx*2+1) )
    return min_tree[idx]

def find_min(start,end,idx,left,right):

    if start>right or end<left:
        return float('inf')
    
    if start >= left and end <= right :
        return min_tree[idx]

    mid = (start + end) // 2
    return min(find_min(start,mid,idx*2,left,right), find_min(mid+1,end,idx*2+1,left,right))

###

def init_max(start,end,idx=1):
    if start == end :
        max_tree[idx] = arr[start]
    else :
        mid = (start+end) // 2 
        max_tree[idx] = max(init_max(start,mid,idx*2), init_max(mid+1,end,idx*2+1) )
    return max_tree[idx]


def find_max(start,end,idx,left,right):

    if start>right or end<left:
        return -float('inf')
    
    if start >= left and end <= right :
        return max_tree[idx]

    mid = (start + end) // 2
    return max(find_max(start,mid,idx*2,left,right), find_max(mid+1,end,idx*2+1,left,right))

N,M = map(int,input().split())
arr = [ int(input()) for _ in range(N) ]
min_tree = [0] * (4*N)
max_tree = min_tree[:]

init_min(0,N-1)
init_max(0,N-1)
for i in range(M):
    a,b = map(int,input().split())
    print(find_min(0,N-1,1,a-1,b-1), end=" ")
    print(find_max(0,N-1,1,a-1,b-1), end=" ")
    print()
