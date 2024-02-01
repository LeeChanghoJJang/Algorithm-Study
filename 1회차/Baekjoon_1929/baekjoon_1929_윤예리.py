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