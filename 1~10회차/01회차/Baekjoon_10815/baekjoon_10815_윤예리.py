N = int(input())

# 시간 초과 이슈로 가지고 있는 카드는 set로 설정하였음
hv_card = set((map(int, input().split())))

M = int(input())

# table의 경우 순서가 바뀌면 result가 바뀌기 때문에 list로 설정
table = list((map(int, input().split())))

result = []
for card in table:
    if card in hv_card:
        result.append(1)
    else:
        result.append(0)

print(*result)

