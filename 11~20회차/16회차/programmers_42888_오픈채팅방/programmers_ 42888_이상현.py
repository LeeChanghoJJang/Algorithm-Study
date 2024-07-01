def solution(record):
    answer = []
    uid_dict = {}

    for rec in record:
        temp = rec.split()

        if temp[0] == 'Leave':
            continue

        uid_dict[temp[1]] = temp[2]

    for rec in record:
        temp = rec.split()

        if temp[0] == 'Enter':
            answer.append(f'{uid_dict[temp[1]]}님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(f'{uid_dict[temp[1]]}님이 나갔습니다.')

    return answer