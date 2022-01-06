# required double array
def check_rule(locations, x, y):
  search_ranges = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  count = 0
  for x_value, y_value in search_ranges:
    dx = x_value + x
    dy = y_value + y

    if dx < 0 or dy < 0 or dx > 24 or dy > 24:
      continue

    if locations[dx][dy] == 1:
      count += 1

  return count
  
locations = [list(map(int, input().split())) for _ in range(25)]
next_locations = [[0] * 25 for _ in range(25)]

for i in range(25):
  for j in range(25):
    result = check_rule(locations, i, j)
    if locations[i][j] == 0:
      if result == 3:
        next_locations[i][j] = 1
    else:
      if result >= 4 or result <= 1:
        next_locations[i][j] = 0
      elif result == 2 or result == 3:
        next_locations[i][j] = 1

for i in range(25):
  for j in range(25):
    print(next_locations[i][j], end=' ')

  print()