# [1차] 비밀지도 (2018 KAKAO BLIND RECRUITMENT)

def solution(n, arr1, arr2):
    ans = []
    for num1, num2 in zip(arr1, arr2):
        binNum = f"{num1|num2:{n}b}"
        binNum = binNum.replace('1', '#')
        binNum = binNum.replace('0', ' ')
        ans.append(binNum)
    return ans