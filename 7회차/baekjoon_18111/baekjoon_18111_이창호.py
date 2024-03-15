import sys
sys.stdin = open('input.txt')
N,M,B = map(int,input().split())
# 제거 : 2초, 추가 : 1초 (추가 먼저한다)
arr =[]
for _ in range(N):
    arr.extend(list(map(int,input().split())))
obj = round(sum(arr)/(N*M))
maxi = max(arr)
min_time= int(1e9)

for target in range(obj-1,obj+1):
    time = 0
    block = B
    for earth in arr:
        if target < earth:
            time += 2*(earth- target)
            block += earth - target
        else:
            time += target-earth
            block -= target - earth
    if block < 0:
        continue
    if min_time >= time:
        min_time = time
        result = target
print(min_time,result)


