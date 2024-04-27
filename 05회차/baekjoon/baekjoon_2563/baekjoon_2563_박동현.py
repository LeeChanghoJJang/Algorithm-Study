paper = [[0 for x in range(100)] for x in range(100)]

t = int(input())
for i in range(t) :
    x,y = map(int,input().split())
    for j in range(x,x+10) :
        for k in range(y, y+10) :
            paper[j][k] = 1

output = 0
for l in paper :
    output+=sum(l)
print(output)