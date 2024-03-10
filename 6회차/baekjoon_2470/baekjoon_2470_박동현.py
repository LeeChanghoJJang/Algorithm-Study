t = int(input())

arr = list(map(int,input().split()))
arr.sort()

left = 0                                    # 투 포인터
right = t-1
ans = abs(arr[left] + arr[right])           # ans : 표적값
answer = [arr[left],arr[right]]             # answer : 표적값을 담은 리스트

while left < right :                        # 종료조건 : left >= right 가 되는 순간
    if ans > abs(arr[left] + arr[right]) :  # 표적값이 새로 계산한 값보다 클 경우
        ans = abs(arr[left] + arr[right])   # ans 갱신
        answer = [arr[left], arr[right]]    # answer 갱신
        if ans == 0 :                       # 0 인 경우 더 작을 수 없으므로 break
            break
    if arr[left]+arr[right] < 0 :           # 절대값이 아닌 기준으로 0보다 작으면 왼쪽값을 올리고
        left += 1
    else :                                  # 0 보다 크면 오른쪽 내리기
        right -= 1

print(*sorted(answer))                      # answer 정렬해서 출력
