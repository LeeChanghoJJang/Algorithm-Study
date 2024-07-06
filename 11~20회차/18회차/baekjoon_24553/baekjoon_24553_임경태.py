# 24553 팰린드롬 게임
for _ in range(int(input())):
    # N이 10의 배수인 경우 선공이 무조건 승리
    print(0 if int(input()) % 10 else 1)