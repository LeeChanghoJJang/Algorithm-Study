from math import ceil

# fees[0,1] : 기본 시간, 기본 요금
# fees[2,3] : 단위 시간, 단위 요금
def solution(fees, records):
    answer = []
    
    data,ans = dict(),dict()
    
    for record in records :
        hm,car,stat = record.split()
        h,m = map(int,hm.split(":"))
        time = h*60+m
        
        if stat == "IN":
            data[car] = time
        else :
            ans[car] = ans.get(car,0)+(time-data[car])
            data.pop(car)
    for car,time in data.items():
        ans[car] = ans.get(car,0)+(1439-data[car])
    
    for car,time in sorted(ans.items()):
        total = fees[1]
        if time > fees[0]:
            total += ceil((time-fees[0])/fees[2])*fees[3]
        answer.append(total)
    return answer