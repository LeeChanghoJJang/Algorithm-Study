import sys
sys.stdin = open('input.txt')
N,M,B = map(int,input().split())
# 제거 : 2초, 추가 : 1초 (추가 먼저한다)
arr =[]
# 어차피.. 1차원으로 구현해도 노상관
for _ in range(N):
    arr.extend(list(map(int,input().split())))
# 목표치를 평균으로 둔다 
obj = round(sum(arr)/(N*M))
maxi = max(arr)
min_time= int(1e9)

# 목표부터 최대값까지 순회(같으면 높은 값을 출력해야하기 때문)
for target in range(obj-1,maxi+1):
    time = 0
    block = B
    # 현재 위치의 높이
    for earth in arr:
        # 목표치가 현재 땅보다 낮은경우 : 블록 제거(2초 소요)
        if target < earth:
            time += 2*(earth- target)
            block += earth - target
        # 목표치가 현재 땅보다 높은 경우 : 블록 추가(1초 소요)
        else:
            time += target-earth
            block -= target - earth
    # 한번씩 순회했는데 마이너스면.. 다음 목표치로 변경
    if block < 0:
        continue
    # 최소 시간을 저장하고, 그 때의 평탄화된 땅 높이를 저장 
    if min_time >= time:
        min_time = time
        result = target
print(min_time,result)


