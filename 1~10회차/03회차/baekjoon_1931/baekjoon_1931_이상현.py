# 백준 1931번 회의실 배정

# 
N = int(input())
time_table = [tuple(map(int, input().split())) for _ in range(N)]
time_table.sort(key = lambda x : (x[1], x[0]))
cnt = 0
temp = -1

for start, end in time_table:
    if start >= temp:
        cnt += 1
        temp = end

print(cnt)