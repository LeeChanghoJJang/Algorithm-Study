# 백준 3986번
N = int(input())
cnt = 0
for i in range(N):
    word = input()
    if len(word)%2:
        continue
    temp = []
    for j in word:
        if len(temp) !=0 and temp[-1] ==j:
            temp.pop()
        else:
            temp.append(j)

    if len(temp) ==0:
       cnt+=1
print(cnt)