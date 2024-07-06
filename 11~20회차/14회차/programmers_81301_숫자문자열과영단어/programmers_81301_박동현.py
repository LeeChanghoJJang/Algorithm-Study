def solution(s):
    answer = 0
    eng_to_num = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
    
    for i in eng_to_num:
        s = s.replace(i,str(eng_to_num[i]))
    answer = int(s)
    return answer