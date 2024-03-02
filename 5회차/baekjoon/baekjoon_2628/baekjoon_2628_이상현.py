h, w = map(int, input().split())
max_ = 0
w_list = [0, w]
h_list = [0, h]

N = int(input())
for _ in range(N):
    type_, temp = map(int, input().split())

    if type_:
        h_list.append(temp)
    else:
        w_list.append(temp)

w_list.sort()
h_list.sort()

for i in range(len(w_list) - 1):
    for j in range(len(h_list) - 1):
        max_ = max(max_, (w_list[i + 1] - w_list[i]) * (h_list[j + 1] - h_list[j]))

print(max_)