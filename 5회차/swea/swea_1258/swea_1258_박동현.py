import sys
sys.stdin = open("1258.txt")


t = int(input())

for tc in range(t):
    size = int(input())

    arr = [list(map(int,input().split())) for _ in range(size)]
    result = []
    for i in range(size):
        for j in range(size):
            if arr[i][j] != 0:
                w = 0
                while arr[i+w][j] != 0 :
                    w += 1
                else :
                    ww = w
                h = 0 
                while arr[i][j+h] != 0 :
                    h += 1
                else :
                    hh = h 
                
                for idx in range(i,i+ww):
                    for jdx in range(j,j+hh):
                        arr[idx][jdx] = 0


                result.append((ww,hh))
    result.sort(key= lambda x: (x[1]*x[0], x[0]))
    print(f"#{tc+1}", len(result), end=" ")
    for ans in result :
        print(*ans, end=" ")
    print()
