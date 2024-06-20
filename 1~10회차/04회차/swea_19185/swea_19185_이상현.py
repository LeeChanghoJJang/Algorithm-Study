# SWEA 19185번 육십갑자

# 년도가 주어졌을 때, 주어진 규칙에 따라 변환된 이름을 구하는 문제
T = int(input())
 
for tc in range(T):
    N, M = map(int, input().split())
    left = input().split()
    right = input().split()
    Q = int(input())
 
    print(f'#{tc + 1} ', end = '')
 
    for _ in range(Q):
        year = int(input())
 
        # 원형 큐와 비슷하게 생각할 수 있음
        print(f'{left[(year - 1) % N]}{right[(year - 1) % M]}', end = ' ')
 
    print()