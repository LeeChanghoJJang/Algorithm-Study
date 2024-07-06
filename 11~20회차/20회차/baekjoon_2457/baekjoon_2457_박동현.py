import sys
input = sys.stdin.readline

# 달력 완
calendar = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# s : 3월 1일
s = 1
for i in range(3): s += calendar[i]
# e : 11월 30일
e = 30
for i in range(11): e += calendar[i]

data = []
for _ in range(int(input())):
    m1,d1, m2,d2 = map(int,input().split())
    date1 = d1
    for i in range(m1):
        date1 += calendar[i]
    date2 = d2
    for i in range(m2):
        date2 += calendar[i]
    data.append((date1,date2))
data.sort()
cnt,end = 0,s
while data :
    if e < end or end < data[0][0] : break

    tmp = -1
    
    for _ in range(len(data)):
        if data[0][0] <= end:
            if tmp <= data[0][1] : tmp = data[0][1]
            data.pop(0)
        else : break
    
    end = tmp
    cnt += 1

print(cnt if end >e else 0)