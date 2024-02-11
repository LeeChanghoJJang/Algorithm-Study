# 백준 14888번 연산자 끼워넣기

# 모든 경우의 수를 탐색
# temp는 현재까지 계산한 결과를 나타내고, index는 num_list에서
# 현재까지 계산에 사용된 수의 개수를 나타냄
def dfs(temp, index):
    global n, min_, max_, num_list, operator_list

    # num_list의 모든 수를 계산에 사용했으면 최솟값, 최댓값을 저장
    if index == n:
        min_, max_ = min(min_, temp), max(max_, temp)
        return True

    for i in range(4):
        if operator_list[i] > 0:
            operator_list[i] -= 1

            # 더하기
            if i == 0:
                dfs(temp + num_list[index], index + 1)

            # 빼기
            elif i == 1:
                dfs(temp - num_list[index], index + 1)

            # 곱하기
            elif i == 2:
                dfs(temp * num_list[index], index + 1)

            # 나누기
            else:
                # 문제에서 나눗셈은 몫만 취한다고 함
                if temp >= 0:
                    dfs(temp // num_list[index], index + 1)

                # 문제에서 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 
                # 그 몫을 음수로 바꾼 것과 같다고 했음
                else:
                    dfs(-(-temp // num_list[index]), index + 1)
                    
            # 그 전의 상태로 돌아가야하기 때문에 연산자의 개수를 원래대로 복구
            operator_list[i] += 1

n = int(input())
num_list = list(map(int, input().split()))

# 연산자의 개수를 operator_list에 배열의 형태로 저장
operator_list = list(map(int, input().split()))

# 문제에서 식을 계산한 결과가 항상 -10억보다 크거나 같고, 10억보다 작거나 같다고 함
min_ = 10 ** 9
max_ = -min_

dfs(num_list[0], 1)

print(f'{max_}\n{min_}')