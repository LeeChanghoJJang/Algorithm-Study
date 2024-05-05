def solution(id_list, report, k):
    id_dict = {}
    cnt = {}
    for id in id_list:
        id_dict[id] = []
        cnt[id] = 0

    for i in report:
        i = list(i.split())
        if i[0] not in id_dict[i[1]]:
            id_dict[i[1]].append(i[0])

    for id in id_dict:
        if len(id_dict[id]) >= k:
            for i in id_dict[id]:
                cnt[i] += 1
    return list(cnt.values())

# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))