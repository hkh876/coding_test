# required double array
def get_ranges(count, x, y):
  min_row = x - count
  max_row = x + count 
  min_col = y - count
  max_col = y + count

  if min_row < 0:
    min_row = 0
  if max_row > 9:
    max_row = 9
  if min_col < 0:
    min_col = 0
  if max_col > 9:
    max_col = 9

  return min_row, max_row, min_col, max_col
    
game_maps = [list(map(int, input().split())) for _ in range(10)]
n = int(input())
players = [tuple(map(int, input().split())) for _ in range(n)]
players_status = []

for i in range(10):
  for j in range(10):
    if game_maps[i][j] > 0:
      count = game_maps[i][j]
      min_row, max_row, min_col, max_col = get_ranges(count, i, j)

      # for debug
      '''
      print(f'count: {count}, x: {i}, y:{j}')
      print(f'{min_row}, {max_row}, {min_col}, {max_col}')
      '''

      game_maps[i][j] = -2
      
      for row in range(i, min_row - 1, -1):
        if game_maps[row][j] == -1:
          break
        elif game_maps[row][j] >= 0:
          game_maps[row][j] = -2

      for row in range(i, max_row + 1):
        if game_maps[row][j] == -1:
          break
        elif game_maps[row][j] == 0:
          game_maps[row][j] = -2

      for col in range(j, min_col - 1, -1):
        if game_maps[i][col] == -1:
          break
        elif game_maps[i][col] >= 0:
          game_maps[i][col] = -2

      for col in range(j, max_col + 1):
        if game_maps[i][col] == -1:
          break
        elif game_maps[i][col] == 0:
          game_maps[i][col] = -2

for i in range(len(players)):
  player_x = players[i][0] - 1
  player_y = players[i][1] - 1
  if game_maps[player_x][player_y] == 0:
    game_maps[player_x][player_y] = i + 1
    players_status.append('survive')
  else:
    players_status.append('dead')
  
for i in range(10):
  for j in range(10):
    print(game_maps[i][j], end=' ')
    
  print()

print('Character Information')
for i in range(len(players_status)):
  print(f'player {i + 1} {players_status[i]}')
