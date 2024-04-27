import sys
from collections import Counter
# 표준 입력을 파일로 변경
sys.stdin = open('input.txt')

# 입력을 한 번에 읽기
lines = sys.stdin.readlines()

# Counter를 사용하여 단어 빈도 계산
info = Counter(lines)
total = sum(info.values())

# 결과 출력
for key in sorted(info.keys()):
    print(f'{key.strip()} {info[key]*100/total:.4f}')
