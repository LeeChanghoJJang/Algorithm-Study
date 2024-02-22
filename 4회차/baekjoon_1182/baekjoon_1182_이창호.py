# 첫번째 방법
import sys
N,S = map(int,sys.stdin.readline().split())
integers = tuple(map(int,sys.stdin.readline().split()))
cnt=0
def back(start,result):
    global cnt
    if result == S and start>0:
        cnt +=1

    for end in range(start,N):
        back(end+1,result+integers[end])

back(0,0)
print(cnt)

# 두번째 방법
import sys
N,S = map(int,sys.stdin.readline().split())
integers = tuple(map(int,sys.stdin.readline().split()))
cnt=0
for row in range(1,1<<N):
    result = 0
    for col in range(N):
        if row & (1<<col):
            result += integers[col]
    if result == S:
        cnt +=1
print(cnt)