import sys
sys.stdin = open('input.txt')
M, N  = map(int,input().split())
width = [0,N]
heights = [0,M]
T = int(input())
for tc in range(T):
    cut1, cut2  = map(int,input().split())
    if cut1==0:
        width.append(cut2)
    elif cut1 ==1:
        heights.append(cut2)
width.sort()
heights.sort()
max_val = 0
for i in range(1,len(width)):
    for j in range(1,len(heights)):
        if max_val < (width[i] - width[i-1]) * (heights[j] - heights[j-1]):
            max_val = (width[i] - width[i-1]) * (heights[j] - heights[j-1])
print(max_val)
