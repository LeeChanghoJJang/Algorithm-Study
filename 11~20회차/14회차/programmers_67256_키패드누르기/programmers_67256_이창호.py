def solution(numbers, hand):
    result =''
    # 두 키보드 위치간에 가까운 거리의 키패드를 반환하는 함수
    def distance(left,right,keypad,hand):
        # 각 거리 재기
        result_l = abs(keypad[1] - left[1]) + abs(keypad[0] - left[0])
        result_r = abs(keypad[1] - right[1]) + abs(keypad[0] - right[0])
        if result_l > result_r:
            return 'R'
        elif result_l < result_r:
            return 'L'
        else:
            if hand =='right':
                return 'R'
            else:
                return 'L'
    # 첫 스타트 지점
    now_l = (3,0)
    now_r = (3,2)
    # 숫자들에서 키패드 숫자를 뺀다.
    for keypad in numbers:
        # 키패드에 따른 좌표 설정
        if keypad ==0:
            location = (3,1)
        else:
            location = ((keypad-1)//3,(keypad-1)%3)
        # 키패드가 어떤 숫자임에 따라 결과값 지정
        if keypad in [1,4,7]:
            result+='L'
            now_l = ((keypad-1)//3,0)
        elif keypad in [3,6,9]:
            result+='R'
            now_r = ((keypad-1)//3,2)
        # 같을 경우 현재 각 손으로부터 거리를 쟤고 가까운쪽 선택
        else:
            temp = distance(now_l,now_r,location,hand)
            result += temp
            if temp=='L':
                now_l = location
            elif temp=='R':
                now_r = location
    return result