# 오픈채팅방 (2019 KAKAO BLIND RECRUITMENT)

# 고려해야 할 것 : 순서, 아이디&&닉네임, 들어옴||나감
def solution(record):
    answer = []
    id_nick = {}

    # 최종 id와 nick 정보 저장
    for cmd in record:
        cmd_char = cmd.split()
        if cmd_char[0] != 'Leave':
            id_nick[cmd_char[1]] = cmd_char[2]

    # 메시지 저장
    for cmd in record:
        cmd_char = cmd.split()
        if cmd_char[0] == 'Enter':
            answer.append(f'{id_nick[cmd_char[1]]}님이 들어왔습니다.')
        if cmd_char[0] == 'Leave':
            answer.append(f'{id_nick[cmd_char[1]]}님이 나갔습니다.')

    return answer
