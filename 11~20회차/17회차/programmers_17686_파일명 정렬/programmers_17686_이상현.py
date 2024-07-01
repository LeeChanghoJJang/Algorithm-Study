def custom_split(file):
    head, number, tail = '', '', ''

    for i, char in enumerate(file):
        if char.isdigit():
            head = file[:i]
            file = file[i:]
            break

    for i, char in enumerate(file):
        if not char.isdigit():
            number = file[:i]
            tail = file[i:]
            break
    else:
        number = file
        tail = ''

    return head, number, tail

def solution(files):
    answer = []
    
    for file in files:
        answer.append(custom_split(file))
        
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(e) for e in answer]