# 리스트를 굳이 써야할까? 2000*2000 하면 꽤 넓은데
# 시뮬레이션 문제면 조건 내에서 좌표만 신경써서 풀이해보기

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for tc in range(1,int(input())+1):
    N = int(input())
    arr = []
    for _ in range(N):
        a,b,c,d = list(map(int,input().split()))
        a *= 2
        b *= 2
        arr.append([a,b,c,d])
    # arr [0] : x좌표 [1] : y좌표 [2] : 방향 [3] : 에너지
    # 중간에 만나는 경우도 존재해서, 2배씩 늘렸음 (1 0 3 1, 0 0 2 1)

    ans = 0
    while len(arr) > 1 :        # 부딪힐 원자가 없을 때까지 (하나 이하로 남기)
        tmp = []                # 1차적으로 거를 리스트
        temp = []               # 2개 이상 있는 경우 담을 리스트 ( 겹친다는 뜻 )
        trash = []              # remove로 중간중간에 지우니까 오류나서 마지막에 몰아서 지우기로 함
        for ele in arr :        # 시뮬레이션의 각 원자에서
            dr = ele[2]         # 방향을 델타로 정해두고 더해주기
            ele[0] += dx[dr]    
            ele[1] += dy[dr]
            
            
            # 움직인 이후의 조건 : 1) 범위를 벗어났는가? 2) 부딪혔는가?
            if -2000 <= ele[0] <= 2000 and -2000 <= ele[1] <= 2000 :
                if (ele[0],ele[1]) in tmp:          # tmp 에 있으면 (이미 한번 나온 좌표)
                    temp.append((ele[0],ele[1]))    # temp 에 넣어 처리 (40번째줄~)
                else :                              # 처음보는 애면
                    tmp.append((ele[0],ele[1]))     # tmp 에 넣어 비교

            # 범위를 벗어났는가? 그럼 쓰레기통
            else :
                trash.append(ele)

        # '부딪혔는가' 에 대한 조건
        for ele in arr :
            if (ele[0],ele[1]) in temp:
                trash.append(ele)           # 부딪혔으면 쓰레기통으로
                ans += ele[3]

        for garbage in trash :              # 비우기
            arr.remove(garbage)
        
    print(f"#{tc} {ans}")