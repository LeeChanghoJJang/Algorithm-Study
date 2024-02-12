N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
p1 = 0  # 파란 종이 수
p0 = 0  # 하얀 종이 수

def num_of_paper(arr, n, a, b):
    start = arr[a][b]   # 가장 왼쪽 위를 기준으로
    global p1
    global p0

    for i in range(a, n+a):     # 달라질 때 마다 1/4
        for j in range(b, n+b):
            if arr[i][j] != start:
                num_of_paper(arr, n//2, a, b)
                num_of_paper(arr, n//2, a+n//2, b)
                num_of_paper(arr, n//2, a, b+n//2)
                num_of_paper(arr, n//2, a+n//2, b+n//2)
                return

    if start == 1:  # 모두 같은 색이면 종이 수 +1
        p1 += 1
    else:
        p0 += 1

num_of_paper(paper, N, 0, 0)
print(p0)
print(p1)