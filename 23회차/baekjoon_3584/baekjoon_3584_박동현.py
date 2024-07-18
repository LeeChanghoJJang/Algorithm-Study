# LCA (최소 공통 조상) 학습 먼저 해야 합니다
import sys
input = sys.stdin.readline


for _ in range(int(input())):

    N = int(input())
    parents = [0]*(N+1)

    for _ in range(N-1):
        a,b = map(int,input().split())
        parents[b]=a

    a,b = map(int,input().split())

    arr,brr = [0,a],[0,b]

    while parents[a]:
        arr.append(parents[a])
        a = parents[a]
    while parents[b]:
        brr.append(parents[b])
        b = parents[b]
    
    idx = -1
    while arr[idx]==brr[idx]:
        idx -= 1
    
    print(arr[idx+1])