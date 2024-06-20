import sys

length, problem = map(int,sys.stdin.readline().split())
test_list = []
for _ in range(length) :
    test_list.append(sys.stdin.readline().strip("\n"))

for _ in range(problem) :
    quiz = sys.stdin.readline().strip("\n")
    if quiz.isdecimal() :
        print(test_list[int(quiz)-1])
    else :
        print(test_list.index(quiz)+1)
