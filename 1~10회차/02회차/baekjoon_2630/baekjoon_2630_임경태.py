# 2630 색종이 만들기

# 색이 같은지 판단하는 함수 - 첫 원소와 모두 색이 같으면 됨
def test_color(N, paper):
    for i in range(N):
        for j in range(N):
            if paper[0][0] != paper[i][j]:
                return 0
    return 1


# 종이를 4개로 나누는 함수
def cut_paper(N, paper, ans):
    # 모두 같은 색일 경우 함수 종료
    if test_color(N, paper):
        color = int(paper[0][0])
        ans[color] += 1
        return

    cut_paper(N//2, [paper[i][:N//2] for i in range(N//2)], ans)     # 1사분면
    cut_paper(N//2, [paper[i][N//2:] for i in range(N//2)], ans)     # 2사분면
    cut_paper(N//2, [paper[i][:N//2] for i in range(N//2, N)], ans)  # 3사분면
    cut_paper(N//2, [paper[i][N//2:] for i in range(N//2, N)], ans)  # 4사분면


# 메인 실행문
N = int(input())
paper = [input().split() for _ in range(N)]
ans = [0, 0]   # 하얀색, 파란색
cut_paper(N, paper, ans)
print(f'{ans[0]}\n{ans[1]}')

'''
31120KB / 68ms
'''