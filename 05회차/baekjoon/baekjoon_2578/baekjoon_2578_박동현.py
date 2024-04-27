test_list = [list(map(int,input().split())) for _ in range(5)]
count = 0
rotation = 0
checker = False
target = [map(int,input().split()) for _ in range(5)]
for l in target :
    for i in l :
        for arr in test_list :
            for j in range(len(arr)) :
                if arr[j] == i :
                    arr[j] = 0 # 빙고 칠하기
                    count += 1
                    # 여기서부터 칠할때마다 카운트 올리기
    # 카운트 올릴때마다 빙고 검증하기
        

                    tilted_list = [char for char in zip(*test_list)] # 회전 리스트
                    sub_count=0
                    for i in test_list :    # 가로열의 합이 0이면 빙고
                        if sum(i) == 0 :
                            sub_count+=1    # 빙고면 카운트 +1
                    for j in tilted_list :    # 세로열 합이 0이면 빙고
                        if sum(j) == 0 : 
                            sub_count+=1 
                            
                    eorkr = 0   # 대각선 카운트 설정
                    dureorkr = 0
                    for k in range(5) :
                        eorkr += test_list[k][k]    # 대각선 / 역대각선 합이 0이면 카운트
                        dureorkr += test_list[k][4-k]
                    if eorkr == 0 :
                        sub_count += 1
                    if dureorkr == 0:
                        sub_count += 1
                        
                    if sub_count >= 3 :     # 위의 카운트가 3 이상이면 출력
                        print(count)
                        checker = True  # 체커를 통해 이후 for 문 강종 
                        break
        if checker :
            break
    if checker: 
        break
