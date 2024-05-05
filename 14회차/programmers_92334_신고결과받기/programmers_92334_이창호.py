
def solution(id_list, report, k):
    # 신고자들이 신고한 게시판 불량 이용자들
    report_person = {i:[] for i in id_list}
    # 본인이 불량 이용자로 신고 당한 횟수
    reported_count = {i:0 for i in id_list}
    # 정지된 사람들을 신고한 사람들이 받은 메일 횟수
    result = [0] * len(id_list)
    # report : 신고자와 신고 당한자를 분리
    for i in report:
        report_, reported = i.split(' ')
        # 신고 당한자가 신고자의 불량 이용자에 없다면(중복이 없음)
        # 새로이 명단을 추가하고, 신고 당한 횟수에 1 증가시킨다
        if reported not in report_person[report_]:
            report_person[report_].append(reported)
            reported_count[reported] +=1
    # id_list : 모든 신고자들을 순회함
    for num,i in enumerate(id_list):
        # 해당 신고자들의 불량이용자들을 하나씩 순회함
        for j in report_person.get(i):
            # 그 불량이용자들이 k번 이상 신고됬을 때, 신고자들의 정지횟수 1증가시킴
            if reported_count[j] >= k:
                result[num] += 1
    return result

def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x:0 for x in id_list}
    # report : 신고자와 신고 당한자 기록
    for r in set(report):
        # 신고자가 불량이용자 신고하면 신고횟수 1추가
        reports[r.split()[1]] +=1

    for r in set(report):
        # k번 이상 신고당했으면
        if reports[r.split()[1]] >= k:
            # 정지횟수 1추가
            answer[id_list.index(r.split()[0])] += 1
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
print(solution2(id_list,report,k))

