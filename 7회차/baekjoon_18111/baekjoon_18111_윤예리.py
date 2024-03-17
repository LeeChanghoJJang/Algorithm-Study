'''
min(제일 낮은 높이 ~ 제일 높은 높이만큼 맞추기)
'''

n, m, b = map(int, input().split())
ground = []

for _ in range(n):
    ground += list(map(int, input().split()))       # 1차원으로 받기

result = [[float('INF'), 257]]

min_time = float('inf')
result_height = 0
for height in range(max(ground), min(ground)-1, -1):
    time = 0
    inventory = 0

    # 파서 쌓을 수도 있어서 처음에 인벤토리를 먼저 고려
    if sum(ground) + b >= height * n * m:
        for current in ground:

            # 1번 작업
            if current > height:
                time += 2 * (current-height)

            # 2번 작업
            else:
                time += (height-current)

        if min_time > time:
            min_time, result_height = time, height

print(min_time, result_height)