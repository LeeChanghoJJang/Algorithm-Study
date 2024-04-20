import sys,math
# from heapq import heappush,heapify,heappop
N = int(input())
A_lst = [0]+ list(map(int,input().split()))
M = int(input())
node = math.ceil(math.log2(N))
node = 2**node

tree = [[float('inf'),-1] for _ in range(node*2)]
# for _ in range(M):
#     query = list(map(int,sys.stdin.readline().split()))
#     if query[0] == 1:
#         A_lst[query[1]] = query[2]
#     else:
#         heappop
for i in range(N):
    treeNum = i + node
    tree[treeNum] = [A_lst[i],i]
    
for i in range(node-1,0,-1):
    left,right = tree[2*i], tree[(2*i)+1]
    if left[0] <= right[0]:
        tree[i]= [left[0],left[1]]
    else:
        tree[i] = [right[0],right[1]]
        
def update(idx,value):
    treeNum = idx+node
    tree[treeNum][0] = value
    while treeNum!=1:
        treeNum = treeNum//2
        left,right = tree[2*treeNum], tree[(2*treeNum)+1]
        
        if left[0] <= right[0]:
            tree[treeNum] = [left[0],left[1]]
        else:
            tree[treeNum] = [right[0],right[1]]
            
for _ in range(M):
    query = list(map(int,sys.stdin.readline().split()))
    if query[0] == 1:
        print(tree[1][1]+1)
    else:
        update(query[1],query[2])
        
        
