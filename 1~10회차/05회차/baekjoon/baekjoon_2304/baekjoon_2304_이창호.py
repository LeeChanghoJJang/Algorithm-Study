import sys
sys.stdin = open('input.txt')

N = int(input())
pillars = []

# 입력 받기
for _ in range(N):
    position, height = map(int, input().split())
    pillars.append((position, height))

# 위치를 기준으로 오름차순으로 정렬
pillars.sort()

max_height_index = 0

# 가장 높은 기둥 찾기
for i in range(1, N):
    if pillars[i][1] > pillars[max_height_index][1]:
        max_height_index = i
result = pillars[max_height_index][1]
height = pillars[0][1]
# 왼쪽 부분에서 물이 차지하는 면적 계산
for i in range(max_height_index):
    if height < pillars[i+1][1]:
        result += height *(pillars[i+1][0] - pillars[i][0])
        height = pillars[i+1][1]
    else:
        result += height * (pillars[i + 1][0] - pillars[i][0])

height = pillars[-1][1]
# 오른쪽 부분에서 물이 차지하는 면적 계산
for i in range(N-1, max_height_index, -1):
    if height < pillars[i-1][1]:
        result += height *(pillars[i][0] - pillars[i-1][0])
        height = pillars[i-1][1]
    else:
        result += height * (pillars[i][0] - pillars[i-1][0])

print(result)




