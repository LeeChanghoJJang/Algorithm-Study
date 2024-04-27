n = int(input())    # 사진틀의 개수
total = int(input())
student = list(map(int, input().split()))
pic = []

for i in range(total):
    check = False
    for j in range(len(pic)):
        if student[i] == pic[j][0]:  # 이미 추천을 받은 경우 횟수 증가
            pic[j][1] += 1
            check = True
            break
    if check:
        continue

    if len(pic) == n:       # 삭제
        pic.pop(pic.index(min(pic, key=lambda x:x[1])))

    pic.append([student[i], 1])     # 사진틀에 새로 게시

pic.sort()
for i in range(len(pic)):
    print(pic[i][0], end=' ')

print()
