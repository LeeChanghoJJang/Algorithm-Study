text = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
v = list(text.keys())

def solution(s):
    for i in v:
        if i in s:
            s = s.replace(i, text[i])

    return int(s)

print(solution('one4seveneight'))