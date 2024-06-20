N, M = map(int, input().split())

# 소수 판별법: 2부터 x-1까지의 수로 나누었을 때,
# 나누어 떨어지는 수가 하나도 없을 것

# 아래 코드는 시간 초과임
# for i in range(N, M+1):
#     total = []
#     for j in range(2, i):
#         total.append(i % j)
#     if 0 not in total:
#         print(i)

# 아래 코드도 시간 초과임.......................
# arr = []
# for i in range(N, M+1):
#     arr.append(i)

# for i in arr:
#     for j in range(2, i):
#         if i % j == 0:
#             arr[arr.index(i)] = 0
#             break
#         else:
#             continue
        
# for a in arr:
#     if a != 0:
#         print(a)

# 에라토스테네스의 체
def is_prime(num):
    if num < 2:
        return False

    # i로 나누었을 때 나누어 떨어지면 i의 배수로도 나누어떨어짐
    # 따라서 i**0.5 까지만 나누어봄
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(N, M+1):
    if is_prime(i):
        print(i)

# 시간초과가 뜬 코드들의 시간복잡도: O(N^2)
# 정답 코드의 시간복잡도: O(N * sqrt(M))
