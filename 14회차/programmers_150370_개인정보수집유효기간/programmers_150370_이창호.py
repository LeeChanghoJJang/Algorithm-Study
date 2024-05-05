
def to_days(date):
    year, month, day = map(int,date.split('.'))
    return year* 28 * 12 + month * 28 + day

def solution(today,terms,privacies):
    # store_term : 약관별 저장할 수 있는 기간
    store_term= {v[0]:int(v[2:]) * 28 for v in terms}
    # 오늘 일자로 전환
    today = to_days(today)
    # expire에 보관기한을 넘긴 건들 인덱스 저장
    expire = [
        i for i, privacy in enumerate(privacies,1)
        # 시작지점을 일자로 변환한것과 보관기한을 더한게 오늘보다 짧으면 파기!
        if to_days(privacy[:-2]) + store_term[privacy[-1]] <= today
    ]
    return expire


today = "2009.12.20"
terms = ["A 13"]
privacies =["2008.11.03 A"]
print(solution(today,terms,privacies))