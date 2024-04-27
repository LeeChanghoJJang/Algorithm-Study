temp = []

for i in range(9):
    temp.append(int(input()))
    
for i in range(8):
    for j in range(i+1,9):
        if sum(temp) - temp[i] - temp[j] == 100:
            a, b = temp[i], temp[j]

temp.remove(a)
temp.remove(b)
temp.sort()

for i in temp:
    print(i)