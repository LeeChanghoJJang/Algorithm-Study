def solution(record):
    id_dict = {}
    for command in record:
        if 'Enter' in command or 'Change' in command:
            command, id, nickname = command.split()
            id_dict[id] = nickname
    result = []
    for idx, command in enumerate(record):
        if 'Enter' in command:
            command, id, nickname = command.split()
            result.append(f'{id_dict[id]}님이 들어왔습니다.')
        elif 'Leave' in command:
            command, id = command.split()
            result.append(f'{id_dict[id]}님이 나갔습니다.')
        elif 'Change' in command:
            command, id, nickname = command.split()
    return result