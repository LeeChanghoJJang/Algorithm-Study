N,K = map(int,input().split())

# N 구 멀티탭 구매 완
multitap = [0] * N
items = list(map(int,input().split()))

cnt = 0
for idx in range(K) :     
    if items[idx] in multitap :                         # 쓰려는게 지금 끼워져 있으면 ?
        continue                                        # 넘어가기

    elif 0 in multitap :                                # 빈공간이 있으면 ?
        multitap[multitap.index(0)] = items[idx]        # 빈공간에 끼우기
    
    # 빼야하는 경우

    else :
        tmp = -1
        for using in multitap :                         # 멀티탭에 꽂혀있는 제품들에 대해서
            if using not in items[idx+1:]:              # 뒤에서 쓰지 않는 애면
                target = using                          # 뺄 타겟을 정함
                break
            # 그런게 아니면
            elif items[idx+1:].index(using) > tmp:      # 걍 맨 마지막에 쓰는 애를 먼저 빼기 
                tmp = items[idx+1:].index(using)
                target = using

        multitap[multitap.index(target)] = items[idx]
        cnt+=1
print(cnt)
