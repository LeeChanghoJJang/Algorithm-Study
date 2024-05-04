def solution(today, terms, privacies):
    year, month, day = map(int, today.split('.'))
    term_dict = {}
    answer = []

    for term in terms:
        temp = term.split()
        term_dict[temp[0]] = int(temp[1])

    for i, privacy in enumerate(privacies, start=1):
        temp, type = privacy.split()
        y, m, d = map(int, temp.split('.'))
        m += term_dict[type]
        
        while m > 12:
            m -= 12
            y += 1

        if y > year or (y == year and m > month) or (y == year and m == month and d > day):
            continue
        answer.append(i)

    return answer