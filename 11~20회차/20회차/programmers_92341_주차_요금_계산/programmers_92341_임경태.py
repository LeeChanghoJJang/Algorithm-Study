# 92341 주차 요금 계산
from math import ceil

# 시간 계산
def cal_time(time, in_time):
    h = int(time[:2]) - int(in_time[:2])
    m = int(time[3:]) - int(in_time[3:])
    return h * 60 + m

def solution(fees, records):
    record_dict = {}
    cost_dict = {}

    for record in records:
        time, num, io = record.split()

        # 입차
        if io == 'IN':
            record_dict[num] = time
        # 출차
        else:
            cost_dict[num] = cost_dict.get(num, 0) + cal_time(time, record_dict[num])
            record_dict[num] = None

    n_time, n_cost, u_time, u_cost = fees

    for num, time in record_dict.items():
        # 출차 기록이 없는 차량의 주차 시간 계산
        if time: cost_dict[num] = cost_dict.get(num, 0) + cal_time("23:59", time)

        # 주차 요금 계산
        cost_dict[num] = n_cost + ceil(max(cost_dict[num]-n_time, 0) / u_time) * u_cost

    # 차량 번호순으로 정렬한 후 요금 리스트 반환
    return list(zip(*sorted(cost_dict.items())))[1]

'''
    핵심 : 입차와 출차 기록을 이용해 차량별 주차 시간을 계산하고, 주차 요금 정책에 따라 총 요금을 산정한다.
'''