import time

rgb_input = input()

start_time = time.time()
r_count, g_count, b_count = map(int, rgb_input.split())
total_count = r_count * g_count * b_count

for i in range(r_count):
	for j in range(g_count):
		for k in range(b_count):
			print(f'{i} {j} {k}')

print(total_count)

print()
print(f'running time : {time.time() - start_time}sec')