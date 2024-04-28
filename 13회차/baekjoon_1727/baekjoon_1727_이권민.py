# #최대한 많은 커플. 적은 성별의 인원 수 만큼
# # 자연수. 순서대로 놓을 수 밖에 없지 않나. 그 안에서 전체적인
# # 순서는 같지만 누구랑 매칭할 지 정도. 그 경우중에 재일 적은 걸로.
import sys

# sys.setrecursionlimit(10**7)
# def BT(me,wo,m_n,w_n,result,passN):
#     global min_n
#     if wo == w_n or me == m_n:
#             min_n = min(min_n,result)
#             return
#     if min_n <= result:
#         return
#     if me >= wo:
        
#         if passN > 0:
#             BT(me,wo,m_n+1,w_n,result,passN-1)
#         BT(me,wo,m_n+1,w_n+1,result+abs(men[m_n]-women[w_n]),passN) 
#     else:
        
#         if passN > 0:
#             BT(me,wo,m_n,w_n+1,result,passN-1)
#         BT(me,wo,m_n+1,w_n+1,result+abs(men[m_n]-women[w_n]),passN) 
        
        
        
    
    
n,m = map(int,input().split())
# pass_n = max(n,m)-min(n,m)
men = list(map(int,input().split()))
men.sort()
women = list(map(int,input().split()))
women.sort()
# m이 더 많은 쪽.
if n > m:
    men,women = women,men
    n,m = m,n
dp = [[0]*m for _ in range(n)]
dp[0][0] = abs(men[0]-women[0])
# 시작점. 
for j in range(1,m-(n-1)):
    dp[0][j] = min(abs(men[0]-women[j]),dp[0][j-1])
for i in range(1,n):
    for j in range(i,m-(n-i-1)):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(men[i]-women[j])
        else:
            dp[i][j] = min(dp[i-1][j-1]+abs(men[i]-women[j]),dp[i][j-1])
print(dp[n-1][m-1])
        
# min_n = 10e10
# BT(n,m,0,0,0,pass_n)
# print(min_n)
