import sys

def button(gender,number,switch,N):
    if gender==1:
        for i in range(number-1,N,number):
            switch[i] = 1 - switch[i]

    elif gender==2:
        for i in range(min(number,N-number+1)):
            if i ==0:
                switch[number - 1] = 1 - switch[number - 1]
            elif switch[number - 1 - i] == switch[number - 1 + i]:
                switch[number - 1 - i] = 1 - switch[number - 1 - i]
                switch[number - 1 + i] = 1 - switch[number - 1 + i]
            else:
                break
    return switch

N = int(sys.stdin.readline())
switch = list(map(int,sys.stdin.readline().split()))
T = int(sys.stdin.readline())

for _ in range(T):
    gender, number = map(int,sys.stdin.readline().split())
    switch = button(gender,number,switch,N)
for j in range(N//20+1):
    print(*switch[20*j:20*j+20])