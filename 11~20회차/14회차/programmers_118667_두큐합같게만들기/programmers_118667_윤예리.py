from collections import deque

def solution(queue1, queue2):
    n = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)

    for i in range(4*n+1):
        if sum1 == sum2:
            return i

        if sum1 < sum2:
            x = q2.popleft()
            sum1 += x
            sum2 -= x
            q1.append(x)
        else:
            x = q1.popleft()
            sum1 -= x
            sum2 += x
            q2.append(x)

    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))