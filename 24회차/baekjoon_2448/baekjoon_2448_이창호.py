import sys
sys.stdin = open('input.txt')

n = int(input())
graph = [[' '] * 2 * n for _ in range(n)]

def back(x, y, n):
    if n==3:
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    else:
        next = n // 2
        back(x,y,next)
        back(x + next,y - next,next)
        back(x + next,y + next,next)

back(0,n-1,n)
for i in graph:
    print("".join(i))