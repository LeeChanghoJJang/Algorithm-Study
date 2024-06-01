def solution(record):
    answer = []
    
    dic = {}
    record = [rec.split() for rec in record]

    for rec in record :
        if (rec[0] == 'Change' and rec[1] in dic) :
            dic[rec[1]] = rec[2]

        elif (rec[0] == 'Enter' and rec[1] in dic) or (rec[0] == 'Enter' and rec[1] not in dic) :
            dic[rec[1]] = rec[2]

    for j in record :
        if j[0] == 'Enter' :
            answer.append('%s님이 들어왔습니다.' % dic[j[1]])
        elif j[0] == 'Leave' :
            answer.append('%s님이 나갔습니다.' % dic[j[1]])

    return answer