# 16974 레벨 햄버거
#  Lv |   Thickness   |     patty     |
# -------------------------------------
#  0  |  1            |  1            |
#  1  |  5 = 3 + 2*1  |  3 = 1 + 2*1  |
#  2  | 13 = 3 + 2*5  |  7 = 1 + 2*3  |
#  3  | 29 = 3 + 2*13 | 15 = 1 + 2*7  |
#  4  | 61 = 3 + 2*29 | 31 = 1 + 2*15 |
#  5  |125 = 3 + 2*61 | 63 = 1 + 2*31 |

def search(N, X):
    # L-0 까지 도달
    if N == 0:
        return 1

    # 1장 섭취
    if X == 1:
        return 0

    # 절반 미만 섭취
    elif X < burger[N-1] + 2:
        return search(N-1, X-1)

    # 절반 섭취
    elif X == burger[N-1] + 2:
        return patty[N-1] + 1

    # 전체 미만 섭취
    elif X < burger[N]:
        return patty[N-1] + 1 + search(N-1, X - burger[N-1] - 2)

    # 전체 섭취
    else:
        return patty[N]

N, X = map(int, input().split())
burger = [1] * 51; patty = [1] * 51

for i in range(1, N + 1):
    burger[i] = 3 + 2 * burger[i - 1]
    patty[i] = 1 + 2 * patty[i - 1]

print(search(N, X))