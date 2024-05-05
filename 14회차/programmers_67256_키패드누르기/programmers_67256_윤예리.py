pos = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2],
    '*': [3, 0], 0: [3, 1], '#': [3, 2]
}

def dist(A, B):
    y1, x1 = A
    y2, x2 = B
    return abs(x1-x2) + abs(y1-y2)

def solution(numbers, hand):
    answer = ''

    left = pos['*']
    right = pos['#']

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = pos[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right = pos[n]
        else:
            if dist(left, pos[n]) > dist(pos[n], right):
                answer += 'R'
                right = pos[n]
            elif dist(left, pos[n]) < dist(pos[n], right):
                answer += 'L'
                left = pos[n]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = pos[n]
                else:
                    answer += 'L'
                    left = pos[n]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))