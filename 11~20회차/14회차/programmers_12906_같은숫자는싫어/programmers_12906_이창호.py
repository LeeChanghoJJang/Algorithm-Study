def solution(arr):
    numbers = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            numbers.append(arr[i])
    return numbers