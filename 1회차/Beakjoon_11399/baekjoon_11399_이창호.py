# 11399 ATM
# 대기시간이 젤 적은 방법은 빠른사람 순으로 업무를 처리하는 것!
N = int(input())
# 시간이 적게 드는 사람부터 정의한다
waiting_time = sorted(map(int,input().split()))
# 뒷사람은 앞사람의 누적시간만큼 기다리므로,
# 뒷사람은 앞사람의 시간을 계속 순차적으로 누적
for i in range(1,len(waiting_time)):
    waiting_time[i] += waiting_time[i-1]
# 전체 누적시간의 합 도출
print(sum(waiting_time))