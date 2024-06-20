import sys
sys.stdin = open('input.txt')

N = int(input())
sequence = list(map(int,input().split()))
result = 1
# 감소하는 길이 저장 
min_cnt = 1
# 증가하는 길이 저장
max_cnt = 1
for idx in range(1,N):
    # 뒷순서가 앞보다 길면 증가하는 수열 길이 증가
    # 그리고 둘중 높은 길이를 result에 저장하고 min_cnt 초기화
    if sequence[idx] > sequence[idx - 1]:
        max_cnt += 1
        if result < max(max_cnt, min_cnt):
            result = max(max_cnt, min_cnt)
        min_cnt = 1
    # 뒷순서가 앞보다 짧으면 감소하는 수열 길이 증가
    # 그리고 둘중 높은 길이를 result에 저장하고 max_cnt 초기화
    elif sequence[idx] < sequence[idx - 1]:
        min_cnt += 1
        if result < max(max_cnt, min_cnt):
            result = max(max_cnt, min_cnt)
        max_cnt = 1
    # 뒷과 앞이 같으면 둘다 증가시키고 result에 저장 
    else:
        max_cnt += 1; min_cnt += 1
        if result < max(max_cnt, min_cnt):
            result = max(max_cnt, min_cnt)
print(result)
