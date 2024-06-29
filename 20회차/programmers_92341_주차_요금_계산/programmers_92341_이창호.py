from collections import defaultdict
import math

def solution(fees, records):
    cars = defaultdict(int)
    car_fees = defaultdict(int)

    for record in records:
        time, car_num, inout = record.split()
        hour, minutes = map(int, time.split(':'))
        time_in_minutes = hour * 60 + minutes

        if inout == "IN":
            cars[car_num] = time_in_minutes
        elif inout == "OUT":
            cultime = time_in_minutes - cars[car_num]
            car_fees[car_num] += cultime
            cars[car_num] = -1  # 차가 주차장 밖에 있는 상태 표시

    # "IN" 기록만 있고 "OUT" 기록이 없는 경우를 처리
    for car_num, in_time in cars.items():
        if in_time != -1:
            cultime = 1439 - in_time
            car_fees[car_num] += cultime

    # 요금 계산
    final_fees = {}
    for car_num, total_time in car_fees.items():
        if total_time <= fees[0]:
            final_fees[car_num] = fees[1]
        else:
            final_fees[car_num] = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]

    # 차량 번호순으로 정렬하여 결과 반환
    return [fee for car_num, fee in sorted(final_fees.items())]
