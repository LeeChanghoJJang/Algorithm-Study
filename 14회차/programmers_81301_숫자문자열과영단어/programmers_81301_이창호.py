num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    # 모든 숫자를 순회하여 변경하면 됨
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)