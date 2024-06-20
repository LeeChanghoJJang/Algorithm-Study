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
# 용해액들 순차적으로 
solution = sorted(map(int,input().split()))
# 최소값을 저장하기 위한 변수
min_val = float('inf')
# 좌측 끝부터
left = 0
# 오른쪽 끝부터 
right = N-1
# 최솟값일 때, 두 포인터 값을 저장하기 위한 result 선언
result = []
# 당연히 둘이 만나기 전에 끝내야 함 
while left < right:
    # 둘의 합을 cha로 저장
    cha = solution[left] + solution[right]
    # 0에 가까운 것이므로, 절대값이 가장 작은 경우에만 min_val에 저장하고, 그때의 포인터들을 result에 저장
    if abs(cha) < abs(min_val):
        min_val = cha
        result = [solution[left],solution[right]]
    # 0보다 작은경우에는 left 증가(음수값을 감소시키기 위함)
    if cha < 0:
        left +=1
    # 0보다 큰 경우에는 right 감소(양수값을 감소시키기 위함)
    elif cha > 0 :
        right -=1
    # 0인 경우
    else:
        break
print(*result)
