def solution(id_list, report, k):
    len_id_list = len(id_list)
    len_report = len(report)

    answer = [0] * len_id_list
    report_dict = {}
    report_cnt_dict = {}

    for i in range(len_report):
        temp = report[i].split()

        if temp[0] in report_dict:
            if temp[1] in report_dict[temp[0]]:
                continue
            report_dict[temp[0]].append(temp[1])
        else:
            report_dict[temp[0]] = [temp[1]]

        if temp[1] in report_cnt_dict:
            report_cnt_dict[temp[1]] += 1
        else:
            report_cnt_dict[temp[1]] = 1

    for i in range(len_id_list):
        if id_list[i] not in report_dict:
            continue

        for user in report_dict[id_list[i]]:
            if report_cnt_dict[user] < k:
                continue
            answer[i] += 1

    return answer