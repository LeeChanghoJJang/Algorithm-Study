from collections import deque

N,t = int(input()), int(input())

students = deque(map(int,input().split()))

pic = deque()                             # 1. 모든 사진들은 비어있다.

star = [0] * 101

while students:
    student = students.popleft()        # 2. 어떤 학생이 특정 학생을 추천하면
    star[student] +=1                   # 4. 이러나 저러나 추천수는 증가시키면 된다.
    if student not in pic :
        if len(pic) < N:
            pic.append(student)         # 2. 추천 받은 학생의 사진이 반드시 게시되어야한다.
        else:                           # 3. 비어있는 사진들이 없는 경우
            min = 1000                  
            for i in pic:               
                if star[i] < min :      # 3. 가장 오래된 사진을 삭제한다(앞부터 순차적으로 순회해서 해결)
                    min = star[i]
                    target = i          
            pic.remove(target)          # 3. 가장 추천 수가 낮은 학생의 사진을 삭제하고
            star[target] = 0            # 5. 삭제되는 경우 추천수는 0으로 바뀐다.
            pic.append(student)         # 2. 16번 줄과 동일
print(*sorted(pic))