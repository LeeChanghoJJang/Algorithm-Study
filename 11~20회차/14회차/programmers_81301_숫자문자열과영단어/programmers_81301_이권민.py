def solution(s):
    word_to_num = {
        "zero":"0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    answer = ''
    temp = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            temp += s[i]
            
            if temp in word_to_num:
                answer += word_to_num[temp]
                temp = ''
            
    
    return int(answer)