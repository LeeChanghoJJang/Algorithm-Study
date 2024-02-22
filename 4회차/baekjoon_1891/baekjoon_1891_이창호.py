import sys
N, objective = map(int,sys.stdin.readline().split())
x,y = map(int,sys.stdin.readline().split())
def find_number(x,y,N):
    result = ''
    while N:
        if x >= 2 ** (N - 1) and y >= 2 ** (N - 1):
            result += '4'
            x -= 2 ** (N - 1)
            y -= 2 ** (N - 1)
        elif x >= 2 ** (N - 1) and y < 2 ** (N-1):
            result += '3'
            x -= 2 ** (N - 1)
        elif x < 2 ** (N - 1) and y < 2 ** (N-1):
            result += '2'
        elif x < 2 ** (N - 1) and y >= 2 ** (N-1):
            result += '1'
            y -= 2 ** (N - 1)
        if x<0 or y<0:
            return -1
        N-=1
    return result

def divided(objective,x,y,depth):
    while objective:
        k, v = divmod(objective,10)
        if v == 1:
            y += 2 ** (depth - 1)
        elif v== 2:
            pass
        elif v==3:
            x += 2 ** (depth - 1)
        elif v==4:
            x += 2 ** (depth - 1)
            y += 2 ** (depth - 1)
        depth+=1
        objective=k
    return [x,y]
location_x,location_y = divided(objective,0,0,1)
x_adj = location_x - y
y_adj = location_y + x
if x_adj < 0 or x_adj >= 2**N or y_adj < 0 or y_adj >= 2**N:
    print(-1)
else:
    print(find_number(x_adj,y_adj,N))