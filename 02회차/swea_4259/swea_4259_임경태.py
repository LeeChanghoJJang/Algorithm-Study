# 4259 제곱수의 합 계산하기

for tc in range(int(input())):
    n = input()
    num_sum = 0

    # 문자열을 슬라이싱하여 밑과 지수를 나누어 계산
    for i in input().split():
        num_sum += int(i[:-1]) ** int(i[-1])

    print(f'#{tc+1} {num_sum}')

'''
44,780KB / 113ms
'''