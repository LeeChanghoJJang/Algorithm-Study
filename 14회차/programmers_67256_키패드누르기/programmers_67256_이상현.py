def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left, right = '*', '#'

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            dist_left = sum(abs(keypad[number][i] - keypad[left][i]) for i in range(2))
            dist_right = sum(abs(keypad[number][i] - keypad[right][i]) for i in range(2))

            if dist_left > dist_right:
                answer += 'R'
                right = number
            elif dist_left < dist_right:
                answer += 'L'
                left = number
            else:
                if hand == 'right':
                    answer +='R' 
                    right = number
                else:
                    answer += 'L'
                    left = number

    return answer