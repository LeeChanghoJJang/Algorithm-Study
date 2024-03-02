import sys
sys.stdin = open('input.txt')
M, N  = map(int,input().split())
width = [0,N]
heights = [0,M]
T = int(input())
for tc in range(T):
    cut1, cut2  = map(int,input().split())
    # 가로로 자르는 경우
    if cut1==0:
        width.append(cut2)
    # 세로로 자르는 경우
    elif cut1 ==1:
        heights.append(cut2)
# 순차적으로 넓이를 구하기 위해 소트
width.sort()
heights.sort()
max_val = 0
# 가로와 세로를 순차적으로 탐색 하여 길이 비교
for i in range(1,len(width)):
    for j in range(1,len(heights)):
        if max_val < (width[i] - width[i-1]) * (heights[j] - heights[j-1]):
            max_val = (width[i] - width[i-1]) * (heights[j] - heights[j-1])
print(max_val)
