import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    tree = [[0,0] for _ in range(N+1)]
    for _ in range(N-1):
        parent, child = map(int, input().split())
        tree[child][0] = parent
        tree[parent][1] = child
    child_1,child_2 = map(int, input().split())
    tem1,tem2 =child_1, child_2
    while tem1 != 0 or tem2!= 0:
        if tem1 == tem2:
            
            print(tem1)
            break
        if tem2 == 0:
            tem2 = child_2
            tem1 = tree[tem1][0]
        else:
            tem2 = tree[tem2][0]
        
        
# 두 노드의 깊이를 맞춤. 그리고 2*(n-1)만킁ㅁ 올라감
    
            
