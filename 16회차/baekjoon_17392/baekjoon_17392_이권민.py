n, m = map(int, input().split()) # n: 약속 개수, m: 방학 일수
expected_happiness = list(map(int, input().split()))

# 우울함의 합이 0인 최대 m
max_m = n + sum(expected_happiness)

if m <= max_m:
  print(0)
else:
  days = m - max_m
  iter, remain = divmod(days, n+1)
#   몫과 나머지 한번에

  ans = 0
  idx = 0
  for idx in range(1, iter+1):
    ans += (idx)**2 * (n+1)
  ans += (idx+1)**2 * (remain)
  print(ans)
