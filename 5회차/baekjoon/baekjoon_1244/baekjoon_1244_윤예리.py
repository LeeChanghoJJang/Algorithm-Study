import sys
sys.stdin = open('input.txt')

num_switch = int(input())
switch = list(map(int, input().split()))
num_student = int(input())
for n in range(num_student):
    m, received = map(int, input().split())

    if m == 1:  # 남자일 때
        for i in range(1, num_switch+1):    # 스위치 번호를 순회하다가
            if i % received == 0:   # 배수이면
                switch[i-1] = abs(switch[i-1]-1)    # 상태를 바꿔준다.
    else:   # 여자일 때
        switch[received-1] = abs(switch[received-1]-1)  # 받은 번호의 스위치의 상태를 바꿔준다.

        i = 1   # 좌우 스위치를 확인하면서
        while 0<=received-1-i<num_switch and 0<=received-1+i<num_switch and switch[received-1-i] == switch[received-1+i]: # 대칭이면
            switch[received-1-i] = abs(switch[received-1-i]-1)  # 상태 변경
            switch[received-1+i] = abs(switch[received-1+i]-1)
            i+=1

for i in range(num_switch//20+1):
    for j in range(i*20, (i+1)*20):
        if 0<=j<num_switch:
            print(switch[j], end=' ')
    print()