N = int(input())
num_list = list(map(int, input().split()))
dp_increase = [1] * N
dp_decrease = [1] * N

for i in range(1, N):
    if num_list[i] >= num_list[i - 1]:
        dp_increase[i] = dp_increase[i - 1] + 1

    if num_list[i] <= num_list[i - 1]:
        dp_decrease[i] = dp_decrease[i - 1] + 1

print(max(max(dp_increase), max(dp_decrease)))