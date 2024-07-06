def solution(record):
    answer = []
    user = {}

    for r in record:
        comment = list(r.split())
        if len(comment) == 3:
            user[comment[1]] = comment[2]

    for r in record:
        comment = list(r.split())
        if comment[0] == 'Enter':
            answer.append(f'{user[comment[1]]}님이 들어왔습니다.')
        elif comment[0] == 'Leave':
            answer.append(f'{user[comment[1]]}님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))