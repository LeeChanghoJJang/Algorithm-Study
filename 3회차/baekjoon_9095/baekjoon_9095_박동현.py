# 규칙 찾기
# 1: 1 
# 2: 2 (1+1)
# 3: 4 (2+2)
# 4: 7 (4+3) 
# 5: 13 (7+6)
# 6: 24 (13+11)
# 7: 44 (24+20) = (24+13+17) (-1 -2 -3)
test_list = [1,2,4,7,13]

t = int(input())

for _ in range(t) :
    test_case = int(input())
    for tc in range(len(test_list), test_case) :
        test_list.append(test_list[tc-1] + test_list[tc-2] + test_list[tc-3])
    print(test_list[test_case-1])
