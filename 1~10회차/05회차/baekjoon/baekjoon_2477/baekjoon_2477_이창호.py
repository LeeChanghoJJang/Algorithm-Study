import sys
sys.stdin = open('input.txt')

K = int(input())
lengths = []
directions = []
# 넓이를 구하기 위한 규칙성파악(육각형에서 들어가는 부분의 방향을 순서대로 기재
# ex) 4,2,4,2는 ㄱ자 모양의 왼쪽하단 부분
ranges = [[4,2,4,2],[2,3,2,3],[3,1,3,1],[1,4,1,4]]
for i in range(6):
    # 각 방향과 길이를 받음
    direction, length = map(int,input().split())
    # 모든 방향을 순서대로 모음
    directions.append(direction)
    # 모든 길이를 순서대로 모음
    lengths.append(length)

for i in range(len(lengths)):
    # 방향을 순서대로 봤을 때, a,b,c,d를 이용한 넓이를 구할 수 있음
    # 네 변의 길이만 필요하므로, directions의 4개를 순서대로 순회하면서 파악
    # 만약 ranges에 있는 패턴이 발견될 경우, a,b,c,d 지정하면 됨 
    if i<3 and directions[i:i+4] in ranges:
        a= lengths[i]
        b= lengths[i+1]
        c= lengths[i+2]
        d= lengths[i+3]
    # 육각형이므로, 3이 넘으면 뒷순서는 원형큐처럼 처음으로 돌아가야함
    elif i>=3 and directions[i:] + directions[:i-2] in ranges:
        a = lengths[i%6]
        b = lengths[(i + 1)%6]
        c = lengths[(i + 2)%6]
        d = lengths[(i + 3)%6]

print((a*(b+d)+(c*d))*K)
