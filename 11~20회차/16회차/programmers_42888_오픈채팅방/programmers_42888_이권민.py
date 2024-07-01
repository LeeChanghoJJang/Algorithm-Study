def solution(record):
    answer = []
    names = {}
    for query in record:
        query_lst = query.split()
        if query_lst[0] == 'Change':
            names[query_lst[1]] = query_lst[2]
        elif query_lst[0] == 'Enter':
            names[query_lst[1]] = query_lst[2]
            answer.append(query_lst[:2])
        else:
            answer.append(query_lst[:2])
    for i in range(len(answer)):
        if answer[i][0] == 'Enter':
            answer[i] = f'{names[answer[i][1]]}님이 들어왔습니다.'
        else:
            answer[i] = f'{names[answer[i][1]]}님이 나갔습니다.'
            
    return answer
            