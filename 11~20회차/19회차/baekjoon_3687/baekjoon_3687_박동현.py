# 최소치 초기 구성 (테케 값이 지정되어 돌기 때문에 미리 구해두면 편하다.)
stick={2:'1',3:'7',4:'4',5:'2',6:'6',7:'8'}
DP=[float('inf')]*101
for i in stick:
    DP[i] = int(stick[i])

for i in range(2,101):
    for j in range(2, i-1):
        DP[i] = min(DP[i], int(str(DP[j])+str(DP[i-j])))
        if j == 6:
            DP[i] = min(DP[i], int(str(DP[i-j])+'0'))

for _ in range(int(input())):
    N = int(input())
    # 최대치는 1로 자릿수 최대한 많이 올리는게 최대치
    # 홀수인경우 맨 앞의 수를 7로 바꾸기
    if N%2:
        ans = '7'+'1'*((N//2)-1)
    else:
        ans = '1'*(N//2)
    print(DP[N], ans)