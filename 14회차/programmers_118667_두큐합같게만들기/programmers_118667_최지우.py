from collections import deque

def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    diff = sum(queue1) - sum(queue2)
    n = len(queue1)

    if diff%2 == 1:
        return -1

    diff //= 2

    while diff != 0:
        if diff > 0:
            if queue1:
                p = queue1.popleft()
                diff -= p
                queue2.append(p)
            else:
                return -1
        else:
            if queue2:
                p = queue2.popleft()
                diff += p
                queue1.append(p)
        answer += 1

        if answer > 4*n:
            return -1

    return answer


queue1 = [2, 2]
queue2 = [2, 4]
print(solution(queue1, queue2))