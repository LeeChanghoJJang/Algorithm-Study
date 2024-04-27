x,y = map(int,input().split())

z = int(y*100//x)
count = 1
if z >= 99 :
    exit(print(-1))
while True :
    if z == int(y*100//x) :
        y+=100
        x+=100
        count+=100
    else :
        break
    
while True :
    count-=1
    y-=1
    x-=1
    if z == int(y*100//x) :
        break
print(count)