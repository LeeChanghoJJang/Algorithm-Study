def recursion(temp):
    len_ = len(temp)
    result  = []

    for row in temp:
        result.append(' ' * len_ + row + ' ' * len_)

    for row in temp:
        result.append(row + ' ' + row)

    return result

N = int(input())
temp = [
    '  *  ',
    ' * * ',
    '*****',
]

while len(temp) != N:
    temp = recursion(temp)

[print(row) for row in temp]