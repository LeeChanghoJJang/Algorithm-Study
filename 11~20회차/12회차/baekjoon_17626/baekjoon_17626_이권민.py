# def counting(cnt,left):
#     if left == 0:
        
#         return cnt
#     print(int(left**0.5))
#     left = left-(int(left**0.5))**2
#     print(left)
#     return counting(cnt+1,left)
        
# n = int(input())
# min_cnt = 10e10
# # 자연수는 n <= 4 인 n개의 제곱수의 합
# # 크게 빼고 나머지에서 크게 크게

# print(counting(0,n))
# # 1 1, 2 1 1, 3 1 1 1, 4 2, 5 2 1, 6 2 1 1, 7 2 1 1 1, 8 2 2, 9 3, 10 3 1, 11 3 1 1, 12 2 2 2, 13 3 2

n = int(input())
arr = [0 if i**0.5%1 else 1 for i in range(n+1)]
# 제곱근이 정수가 아닌 애들은 0
min_num = 4
for i in range(int(n**0.5),0,-1):
    if arr[n]:
        min_num = 1
        break
    elif arr[n-i**2]:
        min_num = 2
        break
    # i**2 을 뺀 게 제곱근이 정수인 값이라면
    else:
        for j in range(int((n-i**2)**0.5),0,1):
            if arr[(n-i**2)-j**2]:
                min_num = 3
            # 한번 뺀거에서 j**2을 뺀 게 제곱근이 정수인 값이라면
#  다 아니면 4
print(min_num)