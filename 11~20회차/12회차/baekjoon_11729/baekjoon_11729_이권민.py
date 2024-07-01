# def Recur(process,cnt,last):
#     print(roll)
#     global min_cnt
#     if min_cnt < cnt:
#         return
#     if not roll[0] and not roll[1]:
#         min_cnt = cnt
#         result = process
#         return
#     for i in range(3):
#         if i != last:
#             for j in range(3):
#                 if i != j and roll[i]:
#                     if not roll[j] or roll[j][-1] > roll[i][-1]:
#                         a = roll[i].pop()
#                         roll[j].append(a)
#                         process.append([i,j])
#                         Recur(process,cnt+1,j)
#                         process.pop()
#                         roll[j].pop()
    
# # 비어있거나 자기보다 큰것들 중에 제일 먼 곳으로 
# # 빈 곳 << 큰것중에 가까운 곳
        
# N = int(input())
# roll =[[] for _ in range(3)]
# for i in range(N,0,-1):
#     roll[0].append(i)
# min_cnt = 10e10
# result = []
# Recur([],0,1)

# print(min_cnt)
# print(result)

def hanoi(n,start,end):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1,start,6-start-end)
    print(start,end)
    hanoi(n-1,6-start-end,end)
    # 2번에 옮겼다가 3번으로 옮기기 
    # inorder
n = int(input())
print(2**n-1)
# a(1) = 1, a(n+1) = 2*a(n)+1
# a는 옮기기 개수 측정.1,3,7,15... 2**n-1 
hanoi(n,1,3)