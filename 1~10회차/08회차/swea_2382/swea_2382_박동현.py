# 상 1 하 2 좌 3 우 4

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
reverse = [0,2,1,4,3]

for tc in range(int(input())):
    N,M,K = map(int,input().split())    # N : 크기 M : 시간 K : 원소 수

    data = [list(map(int,input().split())) for _ in range(K)]
    for _ in range(M):                          # M : 시간변화
        tmp = dict()                            # tmp : 25번 줄부터 중복 확인을 위한 임시 딕셔너리
        for idx in range(K):
            i,j, num, dr = data[idx]            # i : x좌표  j : y 좌표, num : 미생물 수, dr : 방향

            if num :
                di = i + dx[dr]
                dj = j + dy[dr]
                data[idx][0], data[idx][1] = di,dj
                if not ( 1 <= di < N-1 and 1 <= dj < N-1):  # 벽에 박은 경우
                    data[idx][2] //= 2                      # 반으로 줄이고
                    data[idx][3] = reverse[dr]              # 뒤집기 
                
            if (di,dj) not in tmp :
                tmp[(di,dj)] = [idx,num]        # 인덱스와 미생물 수를 저장
            else :
                ind,nums = tmp[(di,dj)]         # 기존의 인덱스와 미생물 수를 비교하여
                if num > nums :                 # 지금꺼가 더 크면
                    tmp[di,dj] = [idx,num]
                    data[idx][2] += data[ind][2]
                    data[ind][2] = 0            # 위에 for문을 K로 둬서 계속 순회해야 하니 0 으로 두고 예외처리
                else :
                    data[ind][2] += data[idx][2]
                    data[idx][2] = 0 

                
    ans = 0
    for arr in data:
        ans += arr[2]
    print(f"#{tc+1} {ans}")