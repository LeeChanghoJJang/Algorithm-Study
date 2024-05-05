def solution(today, terms, privacies):
    answer = []
    Y, m, d = map(int, today.split('.'))

    term_dict = {}
    for term in terms:
        name, period = term.split()
        term_dict[name] = int(period)

    for idx, privacy in enumerate(privacies):
        idx += 1
        date, name = privacy.split()
        p_Y, p_m, p_d = map(int, date.split('.'))
        period = term_dict[name]
        p_m += period
        p_d -= 1

        if not p_d:
            p_m -= 1
            p_d = 28

        while p_m > 12:
            p_m -= 12
            p_Y += 1
        
        # if p_m > 12:
        #     p_Y += p_m//12
        #     p_m %= 12

        if p_Y > Y:
            continue

        if p_Y < Y:
            answer.append(idx)
            continue

        if p_m > m:
            continue

        if p_m < m:
            answer.append(idx)
            continue

        if p_d > d:
            continue

        if p_d < d:
            answer.append(idx)
            continue

    return answer


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(today, terms, privacies))