n = int(input())
gift = []

for _ in range(n):
    a = list(map(int, input().split()))

    if sum(a) == 0:     # 거점지가 아닌 아이들
        if gift:
            print(gift.pop(gift.index(max(gift))))

        else:
            print(-1)

    else:               # 선물 충전
        gift.extend(a[1:])
