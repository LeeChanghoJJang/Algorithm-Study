# 1931 회의실 정리
import sys
sys.stdin = open('input.txt')

N = int(input())
meetings = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:(x[0],x[1]))
temp = []
for start, end in meetings:
    # 아무것도 없을 때
    if not temp:
        temp.append([start,end])
    # temp가 있고, temp의 마지막 원소의 end값보다 현재의 end값이 더 작은 경우
    # 무조건 기존 꺼 빼내야댐
    elif temp:
        if temp[-1][1] > end:
            temp.pop()
            temp.append([start,end])
        # start,end가 같을 때 적어도 뒤 숫자보다는 커야함
        elif temp[-1][1] <= end and start==end:
            temp.append([start,end])
        # 현재의 start보다는 작아야 삽입가능
        elif temp[-1][1] <= start:
            temp.append([start, end])
print(meetings)
print(temp)

