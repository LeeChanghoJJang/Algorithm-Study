sb, ds = map(int,input().split()) # sb수빈 ds동생


# 동생을 기준으로
# 1. 나눈다 (짝수 한정)
# 2. 더하거나 뺀다

visit = [0] * 100001
stack = [ds]

while ds != sb :
    tc = stack.pop(0)

    if tc == sb :
        print(visit[tc])                                # 찾은 경우 - visit에 담긴 값 추출
        break
    else :
        if tc > sb :                                    # 현재 수빈의 위치보다 동생의 위치가 큰 경우
            if tc % 2 == 0:                             # 동생이 짝수 위치에 있는 경우
                if visit[tc//2] == 0:                   # 2로 나눈값이 visit 에 없으면
                    stack.append(tc//2)                 # 그대로 추가하고 
                    visit[tc//2] = visit[tc] + 1

            if tc < 100000 and visit[tc+1] == 0 :       # 도대체 어디까지 가는지 인덱스 에러가 계속 나서, 제한했습니다
                stack.append(tc+1)
                visit[tc+1] = visit[tc] +1

            if visit[tc-1] == 0:
                stack.append(tc-1)
                visit[tc-1] = visit[tc] +1

        else :                                          # 현재 수빈의 위치보다 동생의 위치가 작은 경우
            if visit[tc+1] == 0:
                stack.append(tc+1)
                visit[tc+1] = visit[tc] +1
if ds==sb: 
    print(0)