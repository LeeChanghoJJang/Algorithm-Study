import sys
input = sys.stdin.readline

for _ in range(int(input())):
    size = int(input())
    sticker = [[0,0] + list(map(int,input().split())) for _ in range(2)]

    # 대각선 한칸 반대 or 대각 두칸 전 반대

    for j in range(2,size+2):
        for i in range(2) :
            sticker[i][j] += max(sticker[i-1][j-1], sticker[i-1][j-2])
    print(max([max(x) for x in sticker]))