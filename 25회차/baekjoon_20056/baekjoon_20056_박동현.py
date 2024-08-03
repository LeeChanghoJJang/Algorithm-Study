import sys
input = sys.stdin.readline
# DR: 방향
dr = (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)

# N : arr 크기 
# M : 파이어볼 개수
# K : 이동 명령 수
N,M,K = map(int,input().split())

arr = [[[]for _ in range(N)] for _ in range(N)]

# R,C : 위치
# M : 질량
# S : 속력
# D : 방향

for _ in range(M):
    R,C,M,S,D = map(int,input().split())
    # 인덱스 보정
    arr[R-1][C-1].append((M,S,D))

# K 번의 이동 명령 동안
while K:
    K-= 1
    # 모든 파이어볼이 자신의 방향으로 속력만큼 이동한다. 
    # 중복 이동이 있을 수 있으니 새로 판을 짜주자
    brr = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            while arr[i][j]:
                M,S,D = arr[i][j].pop()
                # 모든 파이어볼은 자신의 방향 d로
                dx,dy = dr[D]
                # 속도 S만큼 이동한다. 
                di,dj = i+dx*S,j+dy*S
                # 0과 N-1은 이어져있다.
                brr[di%N][dj%N].append((M,S,D))

    # 이동이 끝난 뒤, 두 개 이상의 파이어볼이 있는 칸에서 처리를 해야한다.
    arr = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if len(brr[i][j])>1:
                m,s,d = zip(*brr[i][j])
                # 질량은 합//5 이다.
                new_m = sum(m)//5
                # 질량이 0인 파이어볼은 소멸되어 없어진다.
                if new_m == 0 : continue
                # 속도는 합 // 개수 이다.
                new_s = sum(s)//len(brr[i][j])
                # 방향이 모두 홀수이거나 짝수이면 0, 아니면 1
                d = [*map(lambda x: x%2, d)]
                new_d = (0 if all(x == d[0] for x in d) else 1)

                for dt in 0,2,4,6 :
                    arr[i][j].append((new_m,new_s,new_d+dt))
            # 합쳐지지 않은 애들 회수해주기
            elif len(brr[i][j])==1:
                arr[i][j].append(*brr[i][j])

ans = 0
for i in range(N):
    for j in range(N):
        while arr[i][j]:
            M,S,D = arr[i][j].pop()
            ans += M
print(ans)