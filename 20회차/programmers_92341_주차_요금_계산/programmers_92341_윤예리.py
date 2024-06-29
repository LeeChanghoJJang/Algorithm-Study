import math

def solution(fees, records):
    answer = []

    parking_lot = {}
    stacks = []
    for record in records:
        time, car_num, com = record.split()
        hour = int(time[:2])
        minute = int(time[3:])
        total_time = hour * 60 + minute

        if com == "IN":
            if car_num not in parking_lot:
                parking_lot[car_num] = 0
            stacks.append([total_time, car_num])
        
        else:
            for stack in stacks:
                if stack[1] == car_num:
                    parking_lot[car_num] += (total_time - stack[0]) 
                    stacks.remove(stack)
                    break

    for stack in stacks:
        parking_lot[stack[1]] += (1439 - stack[0])
    
    parking_lot = sorted(parking_lot.items())

    for x in parking_lot:
        if x[1] <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + (math.ceil((x[1] - fees[0]) / fees[2]) * fees[3])
            answer.append(fee)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))