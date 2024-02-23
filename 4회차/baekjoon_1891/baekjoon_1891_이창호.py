import sys
# N은 objective의 길이
N, objective = map(int,sys.stdin.readline().split())
# objective에서 이동한 좌표 길이 
x,y = map(int,sys.stdin.readline().split())
# 좌표를 사분면 값으로 변환(밑에 함수의 역산)
def find_number(x,y,N):
    result = ''
    while N:
        # 4사분면에 있는 경우
        if x >= 2 ** (N - 1) and y >= 2 ** (N - 1):
            result += '4'
            x -= 2 ** (N - 1)
            y -= 2 ** (N - 1)
        # 3사분면에 있는 경우
        elif x >= 2 ** (N - 1) and y < 2 ** (N-1):
            result += '3'
            x -= 2 ** (N - 1)
        # 2사분면에 있는 경우
        elif x < 2 ** (N - 1) and y < 2 ** (N-1):
            result += '2'
        # 1사분면에 있는 경우
        elif x < 2 ** (N - 1) and y >= 2 ** (N-1):
            result += '1'
            y -= 2 ** (N - 1)
        # 범위르 초과한 경우 
        if x<0 or y<0:
            return -1
        N-=1
    return result

# 사분면 값을 좌표로 변환
def divided(objective,x,y,depth):
    # objective를 한자리씩 축출하여 위치이동 
    while objective:
        k, v = divmod(objective,10)
        # 맨 뒷자리가 1인경우에는 y의 좌표가 젤 작은 사분면의 길이의 반만큼 늘어남 (처음에는 거즘 1)
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
# 주어진 사분면 위치의 좌표값 도출 
location_x,location_y = divided(objective,0,0,1)
# 거기서 이동한 좌표값
x_adj = location_x - y
y_adj = location_y + x
# 만일 이동했을 때 범위를 초과한 경우에는 -1 출력
if x_adj < 0 or x_adj >= 2**N or y_adj < 0 or y_adj >= 2**N:
    print(-1)
else:
    # 그 외에는 좌표값을 사분면의 위치로 변환 
    print(find_number(x_adj,y_adj,N))
