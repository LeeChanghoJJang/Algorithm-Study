import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())
    arr.append([start_month * 100 + start_day, end_month * 100 + end_day])

arr.sort()

last_day = 301
cnt = 0
tmp = 0

while arr:
    # 꽃은 매일 피어있어야 함
    if last_day >= 1201 or arr[0][0] > last_day:
        break

    for _ in range(len(arr)):
        if arr[0][0] <= last_day:
            # 제일 느리게 지는 꽃
            if tmp <= arr[0][1]:
                tmp = arr[0][1]
            
            arr.remove(arr[0])
        
        else:
            break

    last_day = tmp
    cnt += 1

if last_day < 1201: print(0)
else: print(cnt)