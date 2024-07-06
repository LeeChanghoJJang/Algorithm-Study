def solution(today, terms, privacies):
    result = []
    today = today.strip().split('.')
    today = list(map(int, today))
    terms_dict = {}

    for t in terms:
        t = list(t.split())
        terms_dict[t[0]] = int(t[1])

    for i in range(len(privacies)):
        p = privacies[i].split()

        a = terms_dict[p.pop()]
        b = list(map(int, p[0].split('.')))
        b[1] += int(a)
        while b[1] > 12:
            b[0] += 1
            b[1] -= 12

        if b[0] > today[0]:
            continue
        elif b[0] == today[0]:
            if b[1] > today[1]:
                continue
            elif b[1] == today[1]:
                if b[2] > today[2]:
                    continue
        result.append(i+1)

    return result

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))