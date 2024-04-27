t = int(input())

for i in range(t):
    N = int(input())
    C = list(map(int,input().split()))
    cnt = 0
    result = 0 
    for idx in range(1,N):
        if C[idx-1] < C[idx] :
            cnt += 1
        else :
            if cnt > result:
                result = cnt
            cnt = 0
    if cnt >= result:
        result = cnt
    print(f"#{i+1} {result+1}")
