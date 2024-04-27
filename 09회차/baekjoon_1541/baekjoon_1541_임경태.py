# 1541 잃어버린 괄호

# '-'를 기준으로 분리 후 각각 합산 후 빼줌
equ = list(map(lambda x: sum(map(int, x.split('+'))), input().split('-')))
print(equ[0] - sum(equ[1:]))