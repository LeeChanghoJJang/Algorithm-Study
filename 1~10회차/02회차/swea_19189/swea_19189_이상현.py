# SWEA 19189번 순열의 아름다움

T = int(input())

# 팩토리얼을 매번 계산하지 않기 위해 배열로 선언
fac = [1] * 250001

# dp 를 이용하여 접근
for tc in range(T):
    N, P = map(int, input().split())

    # 입력받은 수(N)까지만 팩토리얼을 계산해여 fac에 저장
    for num in range(2, N + 1):
        fac[num] = (fac[num - 1] * num) % P

    # 이 문제의 답의 일반항
    result = sum(fac[N - i + 1] * i * fac[i] for i in range(1, N + 1))

    print(f'#{tc + 1} {result % P}')

# ------------------------------------------------------------------------

# 시간 초과
#
# def fac(num, p, m = {}):
#     if num in m:
#         return m[num]
#
#     result = 1
#
#     for i in range(2, num + 1):
#         result = (result * i) % p
#
#     m[num] = result
#
#     return result
#
# T = int(input())
# print_result = []
#
# for _ in range(T):
#     N, P = map(int, input().split())
#     print_result.append(sum(fac(N - i + 1, P) * i * fac(i, P) for i in range(1, N + 1)))
#
# for tc, result in enumerate(print_result):
#     print(f'#{tc + 1} {result}')