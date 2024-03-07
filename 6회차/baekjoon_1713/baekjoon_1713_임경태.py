# 1713 후보 추천하기

N, rec, pic = int(input()), input(), {}

for i, n in enumerate(input().split()):
    n = int(n)
    if n in pic: pic[n][0] += 1  # 사진틀에 있으면 추천수 증가
    else:  # 사진틀에 없으면 사진 추가 [추천수, 순번]
        if len(pic) >= N:  # 공간이 없으면 최소 추천 수 사진 제거
            min_stu = min(pic.items(), key=lambda x: (x[1][0], x[1][1]))
            del pic[min_stu[0]]
        pic[n] = [1, i]

print(*sorted(pic))

'''
31120KB / 44ms
'''