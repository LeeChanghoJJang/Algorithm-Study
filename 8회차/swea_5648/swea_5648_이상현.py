import time
start_time = time.time()

#---------------------------------------------------

import sys
sys.stdin = open('input.txt')

T = int(input())
# d_dict = {0 : 1, 1 : 0, 2 : 2, 3 : 3}

for tc in range(T):
    N = int(input())
    atom_dict = {}
    visited = set()
    result = 0

    for _ in range(N):
        x, y, d, e = map(int, input().split())
        # d = d_dict[d]
        atom_dict[-y, x] = (e, d)

    for atom1 in atom_dict:
        e, d = atom_dict[atom1]
        temp = []

        for atom2 in atom_dict:
            if atom1 == atom2 or d == atom_dict[atom2][1]:
                continue

            if d == 0:
                if atom1[0] < atom2[0]:
                    continue

                if atom_dict[atom2][1] == 1 and atom1[1] == atom2[1]:
                    temp.append(((atom1[0] - atom2[0]) / 2, atom2))
                elif atom_dict[atom2][1] == 2 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom1[0] - atom2[0], atom2))
                elif atom_dict[atom2][1] == 3 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom1[0] - atom2[0], atom2))

            elif d == 1:
                if atom1[0] > atom2[0]:
                    continue

                if atom_dict[atom2][1] == 0 and atom1[1] == atom2[1]:
                    temp.append(((atom2[0] - atom1[0]) / 2, atom2))
                elif atom_dict[atom2][1] == 2 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom2[0] - atom1[0], atom2))
                elif atom_dict[atom2][1] == 3 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom2[0] - atom1[0], atom2))

            elif d == 2:
                if atom1[1] < atom2[1]:
                    continue

                if atom_dict[atom2][1] == 3 and atom1[0] == atom2[0]:
                    temp.append(((atom1[1] - atom2[1]) / 2, atom2))
                elif atom_dict[atom2][1] == 0 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom1[1] - atom2[1], atom2))
                elif atom_dict[atom2][1] == 1 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom1[1] - atom2[1], atom2))

            elif d == 3:
                if atom1[1] > atom2[1]:
                    continue

                if atom_dict[atom2][1] == 2 and atom1[1] == atom2[1]:
                    temp.append(((atom2[1] - atom1[1]) / 2, atom2))
                elif atom_dict[atom2][1] == 0 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom2[1] - atom1[1], atom2))
                elif atom_dict[atom2][1] == 1 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom2[1] - atom1[1], atom2))

            if temp:
                temp.sort()
                stack = {}

                print(temp)

                for elem in temp:
                    if elem[0] in stack:
                        stack[elem[0]].add((elem[1], atom_dict[elem[1]][0]))
                    else:
                        stack[elem[0]] = {(elem[1], atom_dict[elem[1]][0])}

                for time_ in stack:
                    len_ = sum(1 for e in stack for set_ in stack[e] if set_[0] not in visited)

                    for i in stack[time_]:
                        if i[0] not in visited:
                            result += i[1]
                            visited.add(i[0])

    print(f'#{tc + 1} {result}')

#---------------------------------------------------

end_time = time.time()
print(f'실행시간: {end_time - start_time}')