# 1931 회의실 배정
# 목표 : 각 회의가 겹치지 않는 회의의 최대 개수 찾기
# 제한 : 1 ≤ N ≤ 100,000, 0 ≤ 시작 시간 & 끝나는 시간 < 2^31-1, 2000ms 이내

# 각 회의 정보 저장
meetings = [tuple(map(int, input().split())) for _ in range(int(input()))]
# 끝나는 시간을 우선 기준으로 오름차순 정렬
meetings.sort(key= lambda x: (x[1], x[0]))
# cnt = 회의개수 / pre_end = 이전 종료시각
cnt = 0; pre_end = 0

# 이전 종료시각이 이번 시작시각보다 빠르거나 같다면 카운트
for open, end in meetings:
    if pre_end <= open:
        cnt += 1; pre_end = end

print(cnt)

'''
51900KB / (튜플 : 236ms) (리스트 : 308ms)

튜플 장점 : 리소스 캐싱 / 빠르게 생성할 수 있고 리스트보다 메모리 부담이 적음
'''