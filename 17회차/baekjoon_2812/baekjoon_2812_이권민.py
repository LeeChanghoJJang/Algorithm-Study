# def erase(cur, k):
#     global tem
#     if cur >= len(num) :
#         return
#     if  k <= 0:  # 현재 위치가 리스트의 길이를 초과하거나 k가 0 이하인 경우 종료
#         tem += ''.join(map(str, num[cur:]))
#         return
#     erase_expect = num[cur:cur+k+1].index(max(num[cur:cur+k+1])) + cur
#     tem += str(num[erase_expect])
#     return erase(erase_expect + 1, k - (erase_expect - cur))

# N, K = map(int, input().split())
# n = input()
# num = [int(nn) for nn in n]
# tem = ''
# erase(0, K)
# print(tem)

N, K = map(int, input().split())
num = list(input())
k = K
stack = []

for i in range(N):
    while(k > 0 and stack and stack[-1] < num[i]):
        stack.pop()
        k-=1
    stack.append(num[i])
    
print(''.join(stack[:N-K]))