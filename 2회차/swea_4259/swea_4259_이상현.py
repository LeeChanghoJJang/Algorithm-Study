# SWEA 4259번 제곱수의 합 계산하기

T = int(input())
 
for tc in range(T):
    n = int(input())
    num_list = input().split()
 
    sum_ = 0

    # 입력받은 각 숫자마다 끝자리 수 전까지의 수를 끝자리 수만큼 제곱을 해주어
    # 모두 더한 합을 구한 후 출력
    for num in num_list:
        sum_ += int(num[:-1]) ** int(num[-1])
 
    print(f'#{tc + 1} {sum_}')