import sys
sys.stdin = open('input.txt')

G = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

def find(bottom, cnt = 0, k = 0):
    global result

    while k < n:
        for i in range(6):
            if bottom == dice_ls[k][i]:
                bottom_idx = i
                top_idx = G[bottom_idx]
                top = dice_ls[k][top_idx]
                break

        tmp = list(dice_ls[k])
        tmp[top_idx] = 0
        tmp[bottom_idx] = 0
        cnt += max(tmp)
        bottom = top
        k += 1
    result = max(result, cnt)


n = int(input())
dice_ls = []
for i in range(n):
    dice = list(map(int, input().split()))
    dice_ls.append(dice)

result = 0
for i in range(6):
    find(dice_ls[0][i])
print(result)




