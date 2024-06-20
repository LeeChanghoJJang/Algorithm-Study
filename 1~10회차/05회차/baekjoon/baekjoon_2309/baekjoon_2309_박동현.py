dwarf = [int(input()) for _ in range(9)]
check = False
dwarf.sort()
for i in range(8):
    for j in range(i+1,9):
        if (dwarf[i] + dwarf[j]) == (sum(dwarf) - 100):
            target1, target2 = dwarf[i], dwarf[j]
            dwarf.remove(target1)
            dwarf.remove(target2)
            check = True
            break
    if check:
        break

print(*dwarf, sep = "\n")