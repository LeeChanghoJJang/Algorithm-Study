def solution(record):
    answer = []
    tmp = []
    ID_nick = dict()
    for i in record:
        order, ID, *nick = i.split()
        # 0은 입장 1은 퇴장
        if order == "Enter":
            tmp.append((0,ID))
            ID_nick[ID] = nick[0]

        elif order == "Leave":
            tmp.append((1,ID))
            
        elif order == "Change":
            ID_nick[ID] = nick[0]
    
    for i in tmp :
        nick = ID_nick[i[1]]
        if i[0] == 0 :
            answer.append(f"{nick}님이 들어왔습니다.")
        else :
            answer.append(f"{nick}님이 나갔습니다.")
    
    return answer