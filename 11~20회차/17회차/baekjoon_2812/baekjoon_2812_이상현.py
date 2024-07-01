N, K = map(int, input().split())
num = list(input())
stack = []
k = K

for i in range(N):
    while K and stack and stack[-1] < num[i]:
        stack.pop()
        K -= 1
        
    stack.append(num[i])
    
print(''.join(stack[:N - k]))