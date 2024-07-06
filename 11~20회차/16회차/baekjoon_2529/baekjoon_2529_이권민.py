def backT(N, cur, num):
    global min_n
    global max_n
    if cur == N:
        if int(min_n) > int(num):
            min_n = num
        if int(max_n) < int(num):
            max_n = num
        return
    

    
    if int(min_n[:cur+1]) <= int(num) and int(num) <= int(max_n[:cur+1]):

        return
    
    for i in range(10):
        if visited[i] == 0:
            visited[i] = 1
            if st_lst[cur] == '<' and int(num[cur]) < i:
                backT(N, cur+1, num+str(i))
            elif st_lst[cur] == '>' and int(num[cur]) > i:
                backT(N, cur+1, num+str(i))
            visited[i] = 0
        
    
N = int(input())
st_lst = input().split()
visited = [0] * 10

# 최소값은 '9876543210'에서 N자리를 선택
min_n = ''.join(sorted('9876543210', reverse=True)[:N+1])
# 최대값은 '0123456789'에서 N자리를 선택
max_n = ''.join(sorted('0123456789')[:N+1])

for i in range(10):
    visited[i] = 1
    backT(N, 0, str(i))
    visited[i] = 0

print(max_n)
print(min_n)
