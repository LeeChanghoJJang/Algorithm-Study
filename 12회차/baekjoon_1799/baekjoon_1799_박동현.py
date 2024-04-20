# # 비숍 조건 : i-j차이가 같거나 i+j가 같은 경우
# # tmp1 : i-j 의 차이 // tmp 2 : i+j 의 차이
# def backtrack(i=0,j=0,tmp1=[], tmp2=[]):
#     global max_value

#     if j == N :
#         i += 1 
#         j = 0 

#     if i == N-1 and j == N-1 :
#         max_value = max(max_value, len(tmp1))
#         return
    
#     if arr[i][j] == 1 and i-j not in tmp1 and i+j not in tmp2 :
#         backtrack(i,j+1,tmp1+[i-j], tmp2+[i+j])
#     backtrack(i,j+1,tmp1,tmp2)

# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]

# max_value = 0 
# backtrack()
# print(max_value)


######
# 블록을 나누기 : 흰 블럭과 검은 블럭 (비숍은 같은 칸에서만 논다.)
# 0 : 흰칸 (i+j % 2 == 0)
# 1 : 검은칸 (i+j % 2 == 1)

def backtrack(color, i=0,j=0, tmp1=[], tmp2=[]) :
    global max_value

    if i == N-1 and j == N :
        max_value = max(max_value, len(tmp1))
        return
    
    if j == N :
        i += 1
        j = 0

    if (i+j) % 2 == color and arr[i][j] == 1 and i-j not in tmp1 and i+j not in tmp2 :
        backtrack(color , i , j+1 , tmp1+[i-j] , tmp2+[i+j])
    backtrack(color , i , j+1 , tmp1 , tmp2)


N = int(input())
arr = [ list(map(int,input().split())) for _ in range(N) ]

ans = 0
for i in range(2) :
    max_value = 0
    backtrack(i)
    ans += max_value

print(ans)

# python 31132kb, 17596ms ? / pypy 132436kb, 752ms