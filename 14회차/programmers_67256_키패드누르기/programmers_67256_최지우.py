def solution(numbers, hand):
    answer = ''
    curL = (3, 0)
    curR = (3, 2)
    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            curL = (num//3, 0)
        elif num in (3, 6, 9):
            answer += 'R'
            curR = (num//3-1, 2)
        else:
            if not num:
                num = 11
            target = (num//3, 1)
            moveL = abs(curL[0] - target[0]) + abs(curL[1] - target[1])
            moveR = abs(curR[0] - target[0]) + abs(curR[1] - target[1])
            if hand == 'right':
                if moveL >= moveR:
                    answer += 'R'
                    curR = target
                else:
                    answer += 'L'
                    curL = target
            else:
                if moveL <= moveR:
                    answer += 'L'
                    curL = target
                else:
                    answer += 'R'
                    curR = target

    return answer


n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
h = 'right'
print(solution(n, h))