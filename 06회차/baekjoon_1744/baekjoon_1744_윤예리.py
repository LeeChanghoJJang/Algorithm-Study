# 묶어서 계산 / 아닐 때 계산
n = int(input())
pos = []
neg = []

for _ in range(n):
    a = int(input())
    if a > 0:
        pos.append(a)
    else:
        neg.append(a)
pos.sort()
neg.sort(reverse=True)

result = 0
while len(pos) > 1:
    num2 = pos.pop()
    num1 = pos.pop()
    result += max(num1+num2, num1*num2)
if pos:
    result += pos.pop()

while len(neg) > 1:
    num2 = neg.pop()
    num1 = neg.pop()
    result += max(num1 + num2, num1 * num2)
if neg:
    result += neg.pop()

print(result)


# 틀렸습니다.
#
# def find(i = 0, value = 0):
#     global max_v
#
#     if i >= n:
#         if value > max_v:
#             max_v = value
#         return
#
#     for j in range(n):
#         try:
#             find(i+2, value+(arr[i]*arr[i+1]))
#             find(i+1, value + arr[i])
#         except:
#             find(i+1, value + arr[i])
#
# n = int(input())
# arr = []
# for _ in range(n):
#     k = int(input())
#     arr.append(k)
# max_v = -1000*50
# find()
# print(max_v)
