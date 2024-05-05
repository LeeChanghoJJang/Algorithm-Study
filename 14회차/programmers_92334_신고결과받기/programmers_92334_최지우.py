id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

def solution(id_list, report, k):
    id_dict = {id_key: [idx, 0] for idx, id_key in enumerate(id_list)}

    n = len(id_list)
    answer = [0 for _ in range(n)]
    arr = [[0] * n for _ in range(n)]
    ban = set()
    for case in report:
        user, report_target = case.split()

        if not arr[id_dict[user][0]][id_dict[report_target][0]]:
            arr[id_dict[user][0]][id_dict[report_target][0]] = 1
            id_dict[report_target][1] += 1

        if id_dict[report_target][1] >= k:
            ban.add(report_target)

    for banned_user in ban:
        for i in range(n):
            if arr[i][id_dict[banned_user][0]] == 1:
                answer[i] += 1

    return answer


print(solution(id_list, report, k))

'''
2차원 배열로 만드는게 나을듯
'''