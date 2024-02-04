# 3986 좋은 단어
# 조건 1 : A와 B의 개수는 각각 짝수여야 함
# 조건 2 : 같은 글자를 만나면 사라진다 할때 마지막에 남는 글자가 없어야 함


def good_words(word): 
    # 조건 1 평가
    if (word.count('A') % 2 == 0) and (word.count('B') % 2 == 0):
        # 조건 2 평가 - 회문
        if word == word[::-1]:
            return 1
    
        # 조건 2 평가 - 소거
        while ('AA' in word) or ('BB' in word):
            if 'AA' in word:
                word = word.replace('AA', '')
            elif 'BB' in word:
                word = word.replace('BB', '')

    # 좋은 단어인지 평가
    if word: return 0
    else: return 1


# 진행
ans = 0
for _ in range(int(input())):
    ans += good_words(input())
print(ans)

'''
31120KB / 52ms
'''