def flip(lst,i,j) :
    for a in range(i,i+3):
        for b in range(j,j+3):
            lst[a][b] = 1-lst[a][b]

N,M = map(int,input().split())
A = [list(map(int,list(input()))) for _ in range(N)]    # 수정할 행렬
B = [list(map(int,list(input()))) for _ in range(N)]    # 비교할 행렬

cnt = 0
if N < 3 or M < 3 :     # 1) 주어진 행렬이 3 보다 짧은 경우
    if A!=B :              # 똑같이 생긴게 아니면
        print(-1)
    else :                 # 똑같이 생겼으면
        print(0)
else :                  # 2) 일반적인 비교 경우

    for i in range(N-2):
        for j in range(M-2):
            # # 수정할 행렬 
            # ai = [A[i+x][j] for x in range(3)]  # 세로열 
            # aj = [A[i][j+x] for x in range(3)]  # 가로열

            # # 비교할 행렬 (뒤집어서 같은지 비교)
            # bi = [1- B[i+x][j] for x in range(3)] # 세로열
            # bj = [1- B[i][j+x] for x in range(3)] # 가로열
            # if ai == bi or aj == bj:
            if A[i][j] != B[i][j] :
                flip(A, i, j)
                cnt += 1
    # 순회 후 같은지 비교 
    if A==B :
        print(cnt)
    else :
        print(-1)