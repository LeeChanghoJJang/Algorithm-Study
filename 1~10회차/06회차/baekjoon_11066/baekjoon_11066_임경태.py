# 11066 파일 합치기 (소설의 여러 장들이 연속이어야 함)

import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    K, size = int(input()), list(map(int, input().split()))
    # DP[i][j] => i ~ j번째 합
    DP = [[0] * K for _ in range(K)]

    for d in range(1, K):
        for i in range(K-d):
            j = i + d
            DP[i][j] = sys.maxsize
            for k in range(i, j):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j] + sum(size[i:j+1]))

    print(DP[0][K-1])

'''
< DP >
0  22  47  58  75 144 189 206 222 247 431 571 634 716 864
0   0  24  35  52 120 165 182 198 223 406 546 609 691 839
0   0   0   7  19  66 111 128 144 164 326 466 529 611 739
0   0   0   0   9  53  98 115 128 148 307 447 510 592 717
0   0   0   0   0  40  85  98 111 131 286 426 489 571 692
0   0   0   0   0   0  40  53  66  86 236 376 439 521 637
0   0   0   0   0   0   0   9  19  34 149 285 334 399 515
0   0   0   0   0   0   0   0   7  19 129 260 309 374 490
0   0   0   0   0   0   0   0   0   8 114 241 290 355 471
0   0   0   0   0   0   0   0   0   0 103 227 276 341 457
0   0   0   0   0   0   0   0   0   0   0 119 168 233 349
0   0   0   0   0   0   0   0   0   0   0   0  35  83 167
0   0   0   0   0   0   0   0   0   0   0   0   0  31  94
0   0   0   0   0   0   0   0   0   0   0   0   0   0  49
0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
'''

# 13975 파일 합치기 3 (소설의 여러 장들이 연속일 필요 없음)
''' 
import heapq as h

for _ in range(int(input())):
    K = int(input())
    size = list(map(int, input().split()))
    h.heapify(size)
    min_v = 0

    while len(size) > 1:
        sum_v = h.heappop(size) + h.heappop(size)
        min_v += sum_v
        h.heappush(size, sum_v)

    print(min_v)
'''