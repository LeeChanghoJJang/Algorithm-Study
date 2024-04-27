import sys
sys.stdin = open('input.txt')

orders = {'W':1,'B':2,'R':3}
def count_repaint_cost(flag, color):
    cost = 0
    for i in range(len(flag)):
        if flag[i] != color:
            cost += 1
    return cost

def backtracking(row, temp):
    global cnt
    global min_repaint_cost
    global N

    if row == N:
        # 첫 줄은 흰색, 마지막 줄은 빨간색으로 고정
        if temp[0] != 'W' or temp[-1] != 'R':
            return

        repaint_cost = 0
        for i in range(N):
            repaint_cost += count_repaint_cost(flag[i], temp[i])

        min_repaint_cost = min(min_repaint_cost, repaint_cost)
        return

    for char in 'WBR':
        if not temp or orders[temp[-1]] <= orders[char] <= orders[temp[-1]]+1:
            temp.append(char)
            backtracking(row + 1, temp)
            temp.pop()

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    cnt = []
    min_repaint_cost = float('inf')
    backtracking(0, [])
    print(f'#{tc} {min_repaint_cost}')