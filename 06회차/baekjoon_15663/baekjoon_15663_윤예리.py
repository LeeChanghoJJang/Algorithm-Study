from itertools import permutations
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ls = sorted(list(set(permutations(arr, m))))
for i in ls:
    print(*i)

# 출력 문제로 오답
# def per(result = [], i = 0):
#     if len(result) == m:
#         if result in total:
#             pass
#         else:
#             total.append(result)
#         return
#
#     if i < len(arr):
#         per(result+[arr[i]], i+1)
#         per(result, i+1)
#
# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# total = []
#
# for i in range(n):
#     per()
#     arr.append(arr.pop(0))
#
# for t in sorted(total):
#     print(*t)
