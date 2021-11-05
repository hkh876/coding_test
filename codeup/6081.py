import time

hex_input = input()
to_number = int(hex_input, 16)

start_time = time.time()
for i in range(15):
	to_hex = format(i + 1, 'X')
	result = format(to_number * (i + 1), 'X')
	print(f'{hex_input}*{to_hex}={result}')

print()
print(f'running time : {time.time() - start_time}sec')