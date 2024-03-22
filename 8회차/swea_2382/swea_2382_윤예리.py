import sys
sys.stdin = open("input.txt")

def check():
    for i in range(k):
        for j in range(k):
            tmp = []
            for h in range(len(arr)):
                if arr[h][0] == i and arr[h][1] == j and arr[h][2] != 0:
                    tmp.append([arr[h], h])

            if len(tmp) > 1:
                tmp.sort(key= lambda x:-x[0][2])
                arr.append([i, j, sum(tmp[i][0][2] for i in range(len(tmp))), tmp[0][0][3]])

                for c in range(len(tmp)):
                    arr[tmp[c][1]][2] = 0

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n, m, k = map(int, input().split())
    arr = []
    for idx in range(k):
        r, c, num, d = map(int, input().split())
        d -= 1
        arr.append([r, c, num, d])

    t = 0
    while t < m:


        for idx in range(len(arr)):
            if arr[idx][2] == 0:
                continue

            arr[idx][0] += di[arr[idx][3]]
            arr[idx][1] += dj[arr[idx][3]]

            if 0<arr[idx][0]<n-1 and 0<arr[idx][1]<n-1:
                pass

            else:
                arr[idx][2] //= 2
                if arr[idx][3] == 0 or arr[idx][3] == 2:
                    arr[idx][3] += 1
                else:
                    arr[idx][3] -= 1

        check()

        t += 1

    result = 0
    for cluster in arr:
        result += cluster[2]

    print(result)


