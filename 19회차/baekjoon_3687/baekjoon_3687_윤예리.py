# 숫자 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 개수 = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

T = int(input())
min_num = [float('inf')] * 101
max_num = [0] * 101
max_num[2] = 1; max_num[3] = 7
min_num[2:8] = [1, 7, 4, 2, 6, 8]
nums = [1, 7, 4, 2, 0, 8]
# 최소값 저장
for i in range(8, 101):
    for j in range(2, 8):
        min_num[i] = min(min_num[i-j] * 10 + nums[j-2], min_num[i])
# 최대값 저장
for i in range(4, 101):
    if i%2:
        max_num[i] = int('7' + str(max_num[i-3]))
    else:
        max_num[i] = int(str(max_num[i-2]) + '1')


for tc in range(T):
    n = int(input())
    print(min_num[n], max_num[n])