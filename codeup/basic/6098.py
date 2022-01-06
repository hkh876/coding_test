import time

space_input = [list(map(int, input().split())) for _ in range(10)]

start_time = time.time()
row_limit = len(space_input)
column_limit = len(space_input[0])
row_index = 1
column_index = 1

while row_index < row_limit and column_index < column_limit:
	space = space_input[row_index][column_index]
	if space != 1:
		space_input[row_index][column_index] = 9
		if space != 0:
			break

		column_index = column_index + 1
	else:
		row_index = row_index + 1
		column_index = column_index - 1
		

for i in space_input:
	for j in i:
		print(j, end=' ')
	print()
	
print()
print(f'running time : {time.time() - start_time}sec')