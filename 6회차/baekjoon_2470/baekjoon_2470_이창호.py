import sys
sys.stdin = open('input.txt')
# 시간초과 코드
# N = int(input())
# solution = list(map(int,input().split()))
# result = []
# min_val = float('inf')
# for left in range(N-1):
#     for right in range(left+1,N):
#         cha = solution[right] + solution[left]
#         if abs(cha) < abs(min_val):
#             min_val = cha
#             result = sorted([solution[right],solution[left]])
# print(*result)
#
N = int(input())
solution = sorted(map(int,input().split()))
# 투포인터 알고리즘
min_val = float('inf')
left = 0
right = N-1
result = []
while left < right:
    cha = solution[left] + solution[right]
    if abs(cha) < abs(min_val):
        min_val = cha
        result = [solution[left],solution[right]]

    if cha < 0:
        left +=1
    elif cha > 0 :
        right -=1
    else:
        break
print(*result)