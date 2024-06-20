N, M = list(input()), list(input())
lenn,lenm = len(N), len(M)

DP = [0] * lenm                             # DP의 각 인덱스를 M의 원소라 치고

for i in range(lenn):                       # n과 m의 인덱스를 순회하면서
    cnt = 0 
    for j in range(lenm):
        if cnt < DP[j]: cnt = DP[j]         # 각 DP에 cnt를 갱신하거나
        elif N[i] == M[j]: DP[j] = cnt+1    # 같은 값이 뒤에 나오면 하나씩 올려주기
print(max(DP))