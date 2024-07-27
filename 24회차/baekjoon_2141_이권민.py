import sys
input = sys.stdin.readline
N = int(input())
people_n = 0
vil = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    people_n += vil[i][1]
vil.sort(key= lambda x: x[0])
# 특정 위치로 가면 해당 위치의 거리들 제외하고 해당 위치에서 거리의 절댓값. 첫번째의 경우 점점 커짐
# 특정 위치일 때 거리값을 표현식으로 표현 가능할듯
# 첫번쨰는 vil[1][0]*vil[1][1]*|vil[i][0]-vil[1][0]|
# 근데 N이 10만인데?
count = 0
for i in range(N):
    count += vil[i][1]
    if count >= people_n/2:
        print (vil[i][0])
        break