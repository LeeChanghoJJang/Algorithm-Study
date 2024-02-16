# 1931 회의실 정리
import sys
sys.stdin = open('input.txt')

N = int(input())
# 배정된 회의실을 시작점 기준으로 먼저 정렬하고, 도착점 기준으로 정렬한다.
# 그리디 알고리즘을 적용할 것
meetings = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:(x[0],x[1]))
# 가능한 회의시간을 담을 temp 설정
temp = []
# 미팅에서 시작점과 끝점을 모두 순회
for start, end in meetings:
    # 아무것도 없을 때는 일단 추가
    if not temp:
        temp.append([start,end])
    # temp가 있을 때는?
    elif temp:
        # 시작시간은 오름차순이므로 뒤로 갈수록 시작시간은 같거나 더 늦음 가정
        # 이번 회의 시간보다 이전 회의시간 끝날 때가 더 느리다?
        # 그러면 이전꺼를 빼고 이번 꺼를 넣어서 최대한 회의시간 확보 필요
        if temp[-1][1] > end:
            temp.pop()
            temp.append([start,end])
        # 이전 회의 시간이 현재의 start보다는 작아야 삽입가능
        elif temp[-1][1] <= start:
            temp.append([start, end])
'''
59444KB / 288ms
'''
print(len(temp))


