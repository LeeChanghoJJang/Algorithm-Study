import sys
sys.stdin = open('input.txt')

N = int(input())
sequence = list(map(int,input().split()))
result = 1
min_cnt = 1
max_cnt = 1
for idx in range(1,N):
    if sequence[idx] > sequence[idx - 1]:
        max_cnt += 1
        if result < max(max_cnt, min_cnt):
            result = max(max_cnt, min_cnt)
        min_cnt = 1
    elif sequence[idx] < sequence[idx - 1]:
        min_cnt += 1
        if result < max(max_cnt, min_cnt):
            result = max(max_cnt, min_cnt)
        max_cnt = 1
    else:
        max_cnt += 1; min_cnt += 1
        if result < max(max_cnt, min_cnt):
            result = max(max_cnt, min_cnt)
print(result)