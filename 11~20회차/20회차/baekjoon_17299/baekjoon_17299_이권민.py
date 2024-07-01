N = int(input())
seq = list(map(int, input().split()))

count = [0] * 1000001
stack = []
res = [-1] * N
for num in seq:
    count[num] += 1

for i in range(N):
    while stack and count[seq[stack[-1]]] < count[seq[i]]:

        res[stack.pop()] = seq[i]
    stack.append(i)
# 앞에 있는 수의 카운트가 뒤에 있는 수의 카운트보다 작으면 앞에있는 수의 인덱스에
# 뒤에있는 수의 인덱스 저장하고 pop. stack[-1]의 count가 제일 작을거기 떄문
print(" ".join(map(str,res)))


