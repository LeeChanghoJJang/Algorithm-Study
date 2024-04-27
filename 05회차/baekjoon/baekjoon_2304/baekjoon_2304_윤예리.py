import sys
sys.stdin = open('input.txt')
#
# n = int(input())
# col = []
#
# # 값 받아오기
# for _ in range(n):
#     l, h = map(int, input().split())
#     col.append((l, h))
#
# # 기둥 높이를 나타낸 리스트(arr) 만들기
# width = max(col)[0]
# height = max(col, key=lambda x:x[1])[1]
# arr = [0] * (width+1)
# for i in col:
#     arr[i[0]] = i[1]
#
# k = 0
# result = 0
# while k <= height:
#     for left in range(width+1):
#         for right in range(width, -1, -1):
#             if arr[left] > k and arr[right] > k:
#                 if left == right:
#                     print(result)
#                     exit()
#
#                 print(left, right)
#                 result += (right - left + 1)
#                 k += 1
#                 break
#


'''
1. 제일 큰 수를 가진 idx를 찾는다.
2. 그 idx를 기준으로 왼쪽과 오른쪽으로 나누어 계산한다.
3. 왼쪽과 오른쪽에서 각각 가운데로 순회하며 자기보다 높은 기둥이 있을 때,
    (1) 이때까지의 width 와 heigth를 곱해 넓이 계산
    (2) 자기보다 높은 기둥을 만나면 반복
'''

# idx 가 현재 위치, h는 저장된 높이, w는 저장된 가로 좌표
def left_area(idx, h, w):
    global area
    while idx <= max_h:
        if h < arr[idx]:
            area += (idx-w) * h
            return left_area(idx, arr[idx], idx)
        else:
            idx += 1
    else:
        return

def right_area(idx, h, w):
    global area
    while idx >= max_h:
        if h < arr[idx]:
            area += (w-idx) * h
            return right_area(idx, arr[idx], idx)
        else:
            idx -= 1
    else:
        return


n = int(input())
col = []

# 값 받아오기
for _ in range(n):
    l, h = map(int, input().split())
    col.append((l, h))

# 기둥 높이를 나타낸 리스트(arr) 만들기
width = max(col)[0]
arr = [0] * (width+1)
for i in col:
    arr[i[0]] = i[1]

# 가장 높은 기둥을 기준으로 좌우 나누기
max_h = arr.index(max(arr))

area = arr[max_h]
left_area(0, arr[0], 0)
right_area(width, arr[width], width)
print(area)










