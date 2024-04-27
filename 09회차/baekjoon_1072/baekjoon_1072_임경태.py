# 1072 게임
# 탐색 대상 : 확률 Z

import sys
sys.stdin = open('input.txt')

X, Y = map(int, input().split())
Z = 100*Y//X
l, r = 0, X
ans = X

if Z > 98:
    print(-1)
else:
    # 최대값과 최소값이 엇갈리지 않는 동안
    while l <= r:
        mid = (l+r)//2
        # mid번 더 해서 확률이 바뀌면 최대값을 감소
        if 100*(Y+mid)//(X+mid) > Z:
            ans = mid
            r = mid - 1
        # 확률이 바뀌지 않으면 최소값을 증가
        else:
            l = mid + 1
    print(ans+1)