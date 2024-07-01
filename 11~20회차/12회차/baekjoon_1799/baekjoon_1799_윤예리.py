# visited를 대각선 방향별로 두 개로 나눠서 계산

import sys
input = sys.stdin.readline

def find(k):
    global cnt, max_value
    bishop = 0
    max_value = max(max_value, cnt)

    # 모든 위치 확인
    if k == n*2-1:
        return

    for i in range(k+1):
        if 0 <= k-i < n and 0 <= i < n:
            if arr[k-i][i] == 1:
                a = k - i*2 + n - 1
                b = k

                # 대각선 비숍 확인
                if not visited1[a] and not visited2[b]:
                    bishop += 1    # 비숍 개수
                    visited1[a] = 1
                    visited2[b] = 1     # 비숍 놓았다고 체크
                    cnt += 1
                    find(k+1)

                    # 넣고 돌렸던 거 빼주기
                    cnt -= 1
                    visited1[a] = 0
                    visited2[b] = 0

    # 비숍 없으면 다음 위치로 이동
    if not bishop:
        find(k+1)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited1 = [0] * (n*2-1)
visited2 = [0] * (n*2-1)
cnt = 0
max_value = 0

find(0)
print(max_value)