import sys
sys.stdin = open('input.txt')

c, r = map(int, input().split())    # 종이 가로, 세로
n = int(input())    # 점선 개수
hor = [0]
ver = [0]
for _ in range(n):
    # 0: 가로, 1: 세로
    dir_, num = map(int, input().split())
    if dir_ == 0:
        hor.append(num)
    else:
        ver.append(num)
hor.sort()
hor.append(r)
ver.sort()
ver.append(c)

area = []
for i in range(len(hor)-1):
    for j in range(len(ver)-1):
        width = hor[i+1]-hor[i]
        height = ver[j+1]-ver[j]
        area.append(width*height)
print(max(area))


