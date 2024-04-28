import sys
from itertools import combinations

input = sys.stdin.readline


# anta 랑 tica 치려면 최소 a,c,i,n,t 는 필수로 있어야함  
# 비교용  = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
alphabet = [1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
comb = [i for i in range(26) if alphabet[i] != 1]

vital = {'a','c','i','n','t'}

N,K = map(int,input().split())

arr = [set(input().strip())-vital for _ in range(N)]

K -= 5 
if K < 0 : exit(print(0))

ans = 0 
for comb_case in list(combinations(comb, K)):
    tmp = alphabet[:]

    for i in comb_case:
        tmp[i] = 1
    
    cnt = 0
    for char in arr :
        for i in char :
            if tmp[ord(i) - ord('a')] != 1:
                break
        else :
            cnt += 1

    ans = max(ans, cnt)

print(ans)