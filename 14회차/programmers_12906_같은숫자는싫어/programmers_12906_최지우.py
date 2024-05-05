def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr:
        if answer and answer[-1] == i:
            continue
        else:
            answer.append(i)

    return answer


arr = [1,1,3,3,0,1,1]

print(solution(arr))