# 파일명 정렬 (2018 KAKAO BLIND RECRUITMENT)

def solution(files):
    file_info = []
    answer = []

    for idx, file in enumerate(files):
        HEAD = ''
        NUMBER = ''
        flag = False

        for char in file:
            if char.isdecimal():
                NUMBER += char
                flag = True
            else:
                if flag: break
                HEAD += char.upper()

        file_info.append((idx, HEAD, int(NUMBER)))

    file_info.sort(key=lambda x: (x[1], x[2]))
    
    for idx, *_ in file_info:
        answer.append(files[idx])

    return answer