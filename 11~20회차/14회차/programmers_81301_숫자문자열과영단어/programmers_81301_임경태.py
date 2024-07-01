# 숫자 문자열과 영단어 (2021 카카오 채용연계형 인턴십)

def solution(s):
    charDict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }
    # 모든 문자열 숫자를 replace로 숫자로 변경
    for char, num in charDict.items():
        s = s.replace(char, num)
    return int(s)