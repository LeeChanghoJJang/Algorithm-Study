# 19185 / 육십갑자 / D3

for tc in range(int(input())):
    N, M = map(int, input().split())  # 문자 개수
    s1, s2 = input().split(), input().split()  # 문자열
    # 알고 싶은 년도 개수로 년도를 입력받음 - 년도를 각각의 문자개수로 나눔 - 문자열로 변환하여 출력
    print(f"#{tc+1} {' '.join([f'{s1[Y % N]}{s2[Y % M]}' for Y in [int(input()) - 1 for _ in range(int(input()))]])}")

'''
60,856KB / 170ms
'''