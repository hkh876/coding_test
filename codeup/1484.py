# required double array
n, m = map(int, input().split())
number_array = [[0] * m for _ in range(n)]

row = 0
col = -1
count = 1
total_count = n * m
method = [(0, 1, m), (1, 0, n), (0, -1, m), (-1, 0, n)]
method_index = -1

while count <= total_count:
  method_index += 1
  if method_index % 4 == 0:
    method_index = 0

  for _ in range(method[method_index][2]):
    new_row = row + method[method_index][0]
    new_col = col + method[method_index][1]

    if new_row < 0 or new_row > n - 1 or new_col < 0 or new_col > m - 1:
      break
    elif count > 0 and number_array[new_row][new_col] != 0:
      break
    
    row = new_row
    col = new_col

    number_array[row][col] = count
    count += 1  
 
for i in range(n):
  for j in range(m):
    print(number_array[i][j], end=' ')

  print()
