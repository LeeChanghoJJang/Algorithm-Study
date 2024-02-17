# 빨리 끝나고,
# 빨리 시작하는 사람들 순으로
n = int(input())
meeting = []
for _ in range(n):
    start_time, end_time = map(int, input().split())
    meeting.append([start_time, end_time])
# 끝나는 순으로 sort, 끝나는 시간이 같다면 시작 시간으로 sort
meeting.sort(key= lambda x:(x[1], x[0]))

count = 1
end_time = meeting[0][1]

for i in range(1, n):
    if meeting[i][0] >= end_time:   # 끝나는 시간 이후 시작 된다면 count
        count += 1
        end_time = meeting[i][1]
print(count)