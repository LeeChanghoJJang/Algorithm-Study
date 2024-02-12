T = int(input())
for tc in range(1, T+1):
    n, d = map(int, input().split())
    angle = d//45
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [[0] * n for _ in range(n)]

    def rotate(A, D):
        global result
        if D == 0:
            return result
        elif D > 0:
            for i in range(n):
                result[i][((n+1)//2)-1] = A[i][i]
                result[i][n-i-1] = A[i][((n+1)//2)-1]
                result[((n+1)//2)-1][i] = A[n-i-1][i]
                result[i][i] = A[((n+1)//2)-1][i]

            for i in range(n):
                for j in range(n):
                    if result[i][j] == 0:
                        result[i][j] = A[i][j]
            return rotate(result, D-1)
        else:
            for i in range(n):
                result[((n+1)//2)-1][i] = A[i][i]
                result[i][i] = A[i][((n+1)//2)-1]
                result[i][((n+1)//2)-1] = A[i][n-i-1]
                result[n-i-1][i] = A[((n+1)//2)-1][i]

            for i in range(n):
                for j in range(n):
                    if result[i][j] == 0:
                        result[i][j] = A[i][j]
            return rotate(result, D+1)

    answer = rotate(arr, angle)
    for i in range(n):
        print(*answer[i])