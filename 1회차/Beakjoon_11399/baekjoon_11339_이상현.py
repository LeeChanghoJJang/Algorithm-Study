# 백준 11339번 ATM

# 시간이 적게 걸리는 사람이 먼저 인출할수록
# 사람들이 기다려야하는 시간의 합이 줄어듦.
N = int(input())
time_list = sorted(list(map(int, input().split())))

# 앞사람의 시간을 더한 값을 저장 후 이 과정을 반복
for index in range(N - 1):
    time_list[index + 1] += time_list[index]

# 사람들이 기다린 시간의 총합
print(sum(time_list))