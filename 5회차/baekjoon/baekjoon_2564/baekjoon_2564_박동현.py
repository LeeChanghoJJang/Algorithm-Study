i,j = map(int,input().split())

# i : 남북, j : 동서
# i : 12 // j : 34 

t = int(input())
# 1 : 북, 2 : 남, 3 : 서, 4 : 동
tc = [] 
for _ in range(t):
    store = list(map(int,input().split()))
    tc.append(store)

way,point = list(map(int,input().split()))
output = 0
for tway, tpoint in tc:
    if way == tway :
        output += abs(point-tpoint)
    
    elif way == 1:
        if tway == 2:
            output += min((i-point + i-tpoint), (point+tpoint)) + j
        elif tway == 3:
            output += point+tpoint
        elif tway == 4:
            output += i-point + tpoint


    elif way == 2:
        if tway == 1 :
            output += min((i-point + i-tpoint), (point+tpoint)) + j
        elif tway == 3:
            output += point + j-tpoint
        elif tway == 4:
            output += i-point + j-tpoint

    elif way == 3:
        if tway == 1:
            output += point+tpoint
        elif tway == 2:
            output += j-point + tpoint
        elif tway == 4:
            output += min((j-point+j-tpoint), (point+tpoint)) + i
    
    elif way == 4:
        if tway == 1:
            output += point + i-tpoint
        if tway == 2:
            output += j-point + i-point
        if tway == 3:
            output += min((j-point+j-tpoint), (point+tpoint)) + i

print(output)