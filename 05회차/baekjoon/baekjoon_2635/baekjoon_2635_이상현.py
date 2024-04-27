num = int(input())
max_cnt, max_num = 0, 0

for next_num in range(1, 30001):
    temp1 = num
    temp2 = next_num
    cnt = 0

    while temp1 >= 0:
        temp1, temp2 = temp2, temp1 - temp2
        cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
        max_num = next_num

print(max_cnt)

while num >= 0:
    print(num, end = ' ')
    num, max_num = max_num, num - max_num