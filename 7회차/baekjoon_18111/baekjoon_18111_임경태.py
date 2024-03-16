# 18111 마인크래프트 (실버2)

N, M, B = map(int, input().split())
arr = sorted(int(x) for _ in range(N) for x in input().split())
time = 1e+9; height = 0

# 최소 ~ 최대 땅 높이 사이 순회 (타겟 높이)
for t in range(arr[-1], arr[0]-1, -1):
    # 시간, 소지 블록 개수
    temp = 0; block = B
    for n in arr:
        s = n - t  # 블록 개수 차이
        if s < 0: temp -= s; block += s  # 블록 쌓기
        else: temp += 2*s; block += s  # 블록 파기
    # 소지하는 블록 개수가 0보다 많고, 소요시간이 적다면 갱신
    if block >= 0 and time > temp:
        time = temp
        height = t

print(time, height)

'''
119764KB / 476ms
'''