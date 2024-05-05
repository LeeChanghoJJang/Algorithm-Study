def solution(id_list, report, k):
    report_dic = {}
    answer = []
    for id in id_list:
        report_dic[id] = [0,[]]
    for men in report:
        attack,defense = men.split()
        if defense not in report_dic[attack][1]:
            report_dic[attack][1].append(defense)
            report_dic[defense][0] += 1
    for id in id_list:
        cnt = 0
        for man in report_dic[id][1]:
            if report_dic[man][0] >= k:
                cnt += 1
        answer.append(cnt)
    
    return answer