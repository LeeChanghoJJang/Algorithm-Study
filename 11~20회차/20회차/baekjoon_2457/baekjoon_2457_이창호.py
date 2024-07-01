import sys
sys.stdin = open('input.txt')

n = int(input())
flower = [list(map(int,input().split())) for i in range(n)]
flower.sort()

i = 0
result = 0
latest_end = (3,1)

while i < n:
    sm,sd,em,ed = flower[i]
    if (sm,sd) <= latest_end < (em,ed):
        max_end = (em,ed)
        while i < n-1:
            nsm,nsd,nem,ned = flower[i+1]
            if latest_end < (nsm,nsd):
                break
            if max_end < (nem,ned):
                max_end = (nem,ned)
            i +=1

        # 찾은 꽃 심기
        result +=1
        latest_end = max_end

        if (11,30) < latest_end:
            exit(print(result))
    i+=1
print(0)
