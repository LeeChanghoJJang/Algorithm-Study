n = int(input())
num = list(map(int, input().split()))
student = []

for i in range(n):
    student.insert(i-num[i], i+1)

print(*student)
