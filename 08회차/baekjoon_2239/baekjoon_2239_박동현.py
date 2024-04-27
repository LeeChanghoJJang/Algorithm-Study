
def backtrack(idx=0):
    # 종료조건 : empty를 모두 썼다 (idx == empty의 길이)
    if idx == len(empty):                           
        for i in range(9):
            print("".join(map(str,arr[i])))
        exit()

    # 백트래킹 
    i, j = empty[idx][0], empty[idx][1]
    used = set(arr[i] + [arr[x][j] for x in range(9)] + [arr[x][y] for x in range(3*(i//3),3*(i//3)+3) for y in range(3*(j//3), 3*(j//3) +3)])
    # used에 각 행, 렬, 사각형에 쓰인 숫자를 담고    
    nums = set(range(1,10))                             
    # 1~9까지 담긴 nums와의 차집합을 이용해 숫자를 넣고 백트래킹
    # 이 경우 차집합이 공집합이면 백트래킹이 종료된다.
    for num in sorted(nums - used):
        arr[i][j] = num
        backtrack(idx+1)
        arr[i][j] = 0


arr = [list(map(int,list(input()))) for _ in range(9)]

empty = [(i,j) for i in range(9) for j in range(9) if not arr[i][j]]    # 0인 칸의 인덱스 저장

backtrack()