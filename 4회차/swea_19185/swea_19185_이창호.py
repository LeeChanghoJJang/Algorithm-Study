T = int(input())
for tc in range(1,T+1):
    # years는 알고 싶은 년도를 저장하기 위함
    years = []
    # N개와 M개의 문자열마다 반복
    N,M = map(int,input().split())
    str_1 = input().split()
    str_2 = input().split()
    # 알고 싶은 연도 숫자만큼 순회하여 years에 저장
    Q = int(input())
    for _ in range(Q):
        years.append(int(input()))
    print(f'#{tc}',end=' ')
    # 각 문자열을 해당되는 길이만큼 나누고 각 문자열을 합산
    for i in years:
        print(str_1[i%N-1] +str_2[i%M-1],end=' ')
    print()
