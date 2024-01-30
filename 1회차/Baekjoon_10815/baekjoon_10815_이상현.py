# 백준 10815번 숫자 카드

# 상근이가 가지고 있는 N개의 숫자 카드
N = int(input())
num_list = set(map(int, input().split()))

# 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수
M = int(input())
target_num = list(map(int, input().split()))

# target_num 의 각 숫자마다 상근이가 가지고 있으면 1을,
# 아니면 0을 공백으로 구분해 출력
for num in target_num:
    if num in num_list:
        print(1, end = ' ')
    else:
        print(0, end = ' ')