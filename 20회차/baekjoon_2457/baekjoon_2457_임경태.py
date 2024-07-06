# 2457 공주님의 정원
N = int(input())
flowers = sorted(tuple(map(int, input().split())) for _ in range(N))
now_end = (3, 1)
max_end = (3, 1)
ans = idx = 0

while now_end <= (11, 30):
    # 커버 가능 꽃 중 가장 멀리 끝나는 꽃을 찾기 위한 루프
    while idx < N and (flowers[idx][0], flowers[idx][1]) <= now_end:
        max_end = max(max_end, (flowers[idx][2], flowers[idx][3]))
        idx += 1

    # 더 이상 커버할 수 있는 꽃이 없을 경우
    if now_end == max_end: exit(print(0))

    # 종료 시점 갱신
    now_end = max_end
    ans += 1

print(ans)

'''
    핵심 : 주어진 데이터를 효율적으로 관리하고, 꽃이 개화하는 구간을 정확하게 파악하는 것
'''