def cal_time(in_time, out_time):
    in_hr, in_min = map(int, in_time.split(':'))
    out_hr, out_min = map(int, out_time.split(':'))
    
    if in_min > out_min:
        return 60 * (out_hr - in_hr - 1) + out_min - in_min + 60
    return 60 * (out_hr - in_hr) + out_min - in_min

def solution(fees, records):
    parking_dict = {}
    dict_ = {}
    
    for record in records:
        time_, car_num, history = record.split()
        car_num = int(car_num)
        
        if history == 'IN':
            parking_dict[car_num] = time_
        else:
            parking_time = cal_time(parking_dict[car_num], time_)
            
            if car_num in dict_:
                dict_[car_num] += parking_time
            else:
                dict_[car_num] = parking_time
                
            del parking_dict[car_num]
    
    for car_num in parking_dict:
        parking_time = cal_time(parking_dict[car_num], '23:59')

        if car_num in dict_:
            dict_[car_num] += parking_time
        else:
            dict_[car_num] = parking_time
            
    def cal_fee(parking_time):
        if parking_time <= fees[0]:
            return fees[1]
        fee = fees[1]
        parking_time -= fees[0]
        fee += ((parking_time - 1) // fees[2] + 1) * fees[3]
        return fee
    
    for car_num in dict_:
        dict_[car_num] = cal_fee(dict_[car_num])
    
    answer = [v for k, v in sorted(dict_.items())]
    
    return answer