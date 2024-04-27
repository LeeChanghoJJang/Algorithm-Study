#동1 서2 남3 북4
s = [] # 방향, 거리 저장 리스트
x = [] # 가로 길이 리스트
y = [] # 세로 길이 리스트

t = int(input())

for i in range(6):
    
    way,dist = map(int,input().split()) # 방향, 거리 입력
    s.append([way,dist])

    if s[i][0] == 3 or s[i][0] == 4: # 세로 저장
        x.append(s[i][1])

    if s[i][0] == 1 or s[i][0] == 2: # 가로 저장
        y.append(s[i][1])

left = [] # 남은 땅
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]:
        left.append(s[(i+1)%6][1])

print( ((max(x)*max(y)) - (left[0]*left[1])) * t )