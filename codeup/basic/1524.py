# required double array
def get_mine_count(maps, x, y):
  search_ranges = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  count = 0
  for x_value, y_value in search_ranges:
    dx = x_value + x
    dy = y_value + y

    if dx < 0 or dy < 0 or dx > 8 or dy > 8:
      continue

    if maps[dx][dy] == 1:
      count += 1

  return count

mine_maps = [list(map(int, input().split())) for _ in range(9)]
r, c = map(int, input().split())

if mine_maps[r - 1][c - 1] == 1:
  print(-1)
else:
  print(get_mine_count(mine_maps, r - 1, c - 1))