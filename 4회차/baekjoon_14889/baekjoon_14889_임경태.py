# 14889 / 스타트와 링크 / 실버1

import sys 
sys.stdin = open('input.txt')

def create_comb(arr, idx):
    global min_v
    # 능력치 차이의 최솟값이 0 or 팀원이 부족하면 고려 안함
    if min_v == 0 or idx - len(arr) > N//2:
        return

    # 팀이 완성되면 능력치 계산
    if len(arr) == N//2:
        opp_arr = [i for i in range(0, N) if i not in arr]
        stat_diff = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                a = arr[i]; b = arr[j]
                c = opp_arr[i]; d = opp_arr[j]
                stat_diff += S[a][b] + S[b][a] - (S[c][d] + S[d][c])
        min_v = min(min_v, abs(stat_diff))
        return

    # 팀원 포함 여부 결정
    if idx < N:
        create_comb(arr + [idx], idx+1)
        create_comb(arr, idx+1)

N = int(input())  # 사람 수
S = [tuple(map(int, input().split())) for _ in range(N)]  # 능력치

# 팀 능력치 배열 완성
min_v = 100
create_comb([0], 1)
print(min_v)

'''
31120KB / 1280ms
'''