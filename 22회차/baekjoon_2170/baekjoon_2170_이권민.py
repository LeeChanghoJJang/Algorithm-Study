import sys
input = sys.stdin.readline
N = int(input())
lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort(key=lambda x:(x[0],x[1]))
sum = 0
for i in range(N-1):
    if lines[i][0] <= lines[i+1][0] <= lines[i][1]:
        if lines[i][1] < lines[i+1][1]:
            lines[i+1][0] = lines[i][0]
        else:
            lines[i+1] = lines[i]
        # 갱신
    else:
        sum += lines[i][1]-lines[i][0]
        # 출력
# 투포인터처럼 해도 돼

sum += lines[-1][1] - lines[-1][0]
    
    
print(sum)
    
    
