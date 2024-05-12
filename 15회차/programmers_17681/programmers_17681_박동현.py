def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        # 1. arr1[i] | arr2[i] : 비트 OR 변산
        # 2. bin(a)[2:] : 이진수 변환
        # 3. zfill(n) : 자리수 유지를 위해 앞자리에 0채우기
        # 4. replace : 1은 #으로, 0은 " "로 변환
        clue = bin(arr1[i] | arr2[i])[2:].zfill(n).replace("1", "#").replace("0", " ")
        answer.append(clue)
        
    return answer