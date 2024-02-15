# 2346 풍선 터뜨리기
# 목표 : 터진 풍선의 번호를 차례로 나열

# N: 풍선 개수 / B: 풍선 번호와 종이 번호 저장
N = int(input())
B = [(i+1, num) for i, num in enumerate(map(int, input().split()))]

pang = 0
while B:
    print(B[pang][0], end= ' ')
    n, p = B.pop(pang)
    if B:
        # 종이에 적혀있는 숫자만큼 이동
        if p < 0: pang = (pang + p) % len(B)
        else: pang = (pang + p - 1) % len(B)

'''
31120KB / 44ms
'''