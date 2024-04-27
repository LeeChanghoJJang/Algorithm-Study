t = int(input())
cnt = 0
result = [0]
for i in range(t//2,t+1):
    test_list = [t,i]

    while True :
        next = test_list[-2]-test_list[-1]
        if next >= 0 :
            test_list.append(next)
        else :
            if len(test_list) > cnt :
                result = test_list[:]
                cnt = len(result)
                break
            else :
                break
print(cnt)
print(*result)