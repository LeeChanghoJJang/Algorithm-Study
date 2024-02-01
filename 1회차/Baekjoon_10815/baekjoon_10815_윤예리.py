N = int(input())
hv_card = list((map(int, input().split())))

M = int(input())
table = list((map(int, input().split())))

# 시간 초과
result = []
for card in table:
    if card in hv_card:
        result.append(1)
    else:
        result.append(0)

print(*result)