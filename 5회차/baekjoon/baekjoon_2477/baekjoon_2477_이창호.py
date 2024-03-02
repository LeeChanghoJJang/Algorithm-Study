import sys
sys.stdin = open('input.txt')

K = int(input())
lengths = []
directions = []
ranges = [[4,2,4,2],[2,3,2,3],[3,1,3,1],[1,4,1,4]]
for i in range(6):
    direction, length = map(int,input().split())
    directions.append(direction)
    lengths.append(length)

for i in range(len(lengths)):
    if i<3 and directions[i:i+4] in ranges:
        a= lengths[i]
        b= lengths[i+1]
        c= lengths[i+2]
        d= lengths[i+3]
    elif i>=3 and directions[i:] + directions[:i-2] in ranges:
        a = lengths[i%6]
        b = lengths[(i + 1)%6]
        c = lengths[(i + 2)%6]
        d = lengths[(i + 3)%6]

print((a*(b+d)+(c*d))*K)
