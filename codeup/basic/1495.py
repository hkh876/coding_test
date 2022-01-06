# required double array
n, m, k = map(int, input().split())
array_d = [[0] * 1001 for _ in range(1001)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(k):
  x1, y1, x2, y2, u = map(int, input().split())

  array_d[x1][y1] = array_d[x1][y1] + u
  array_d[x2 + 1][y2 + 1] = array_d[x2 + 1][y2 + 1] + u
  array_d[x1][y2 + 1] = array_d[x1][y2 + 1] - u
  array_d[x2 + 1][y1] = array_d[x2 + 1][y1] - u

for i in range(1, n + 1):
  for j in range(1, m + 1):
    dp[i][j] = array_d[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

for i in range(n):
  for j in range(m):
    print(array_d[i][j], end=' ')

  print()

print()
for i in range(1, n + 1):
  for j in range(1, m + 1):
    print(dp[i][j], end=' ')

  print()