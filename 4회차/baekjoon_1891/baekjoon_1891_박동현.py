depth, num = input().split()
depth = int(depth)
num = list(num)
a,b = map(int,input().split())

x,y=0,0 #초기 좌표

n=depth # 사이즈 계수 
for i in num:
    i=int(i)
    n-=1 #사이즈를 줄여나감
    size=2**n # =변의 길이

    if i==1: #1사분면
        y+=size
    elif i==2: #2사분면
        pass
    elif i==3: #3사분면
        x+=size
    elif i==4: #4사분면
        x+=size
        y+=size


#좌표를 이동
x-=b    # 4사분면이 양쪽을 더해 반대로 계산함
y+=a

answer=""
# 역산 과정
for i in range(depth):
    limit = 2**(depth-i) #변의 길이
    half = 2**(depth-i-1) #변의 길이의 반

    if 0<=x<half and 0<=y<half: #2사분면
        answer += "2"
    elif 0<=x<half and half<=y<limit: #1사분면
        y -= half
        answer += "1"
    elif half<=x<limit and 0<=y<half: #3사분면
        x -= half
        answer += "3"
    elif half<=x<limit and half<=y<limit: #4사분면

        x -= half
        y -= half
        answer += "4"


if len(answer) == depth:  # 유효하지 않은 경우 답과 길이가 달라짐
    print(answer)
else:
    print(-1)