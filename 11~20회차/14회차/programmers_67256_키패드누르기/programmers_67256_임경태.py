# 키패드 누르기 (2020 카카오 인턴십)

def solution(numbers, hand):
    ans = ''
    L = R = (3, 0)  # 현재 행, 중간 열 유무

    for num in numbers:
        # 1,4,7 이라면 왼손으로 누름
        if num in [1, 4, 7]:
            L = (num//3, 0)
            ans += 'L'
        # 3,6,9 이라면 오른손으로 누름
        elif num in [3, 6, 9]:
            R = ((num-1)//3, 0)
            ans += 'R'
        # 1,5,8,0 이라면 거리순 - 잡이순
        else:
            # 0은 10으로 변환
            if num == 0: num = 10
            # 중간 열에 있다면 거리 1 빼줌
            LD = abs(L[0] - num//3) - L[1]
            RD = abs(R[0] - num//3) - R[1]
            if LD < RD or (LD == RD and hand == 'left'):
                L = (num//3, 1)
                ans += 'L'
            else:
                R = (num//3, 1)
                ans += 'R'
    return ans