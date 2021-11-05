import time

number_input = int(input())
start_time = time.time()

for i in range(1, number_input + 1):
	to_str = str(i)

	clap_count = to_str.count('3') + to_str.count('6') + to_str.count('9')
	if clap_count > 0:
		result = 'X'
		for j in range(clap_count - 1):
			result += 'X'

		print(result, end=' ')
	else:
		print(to_str, end=' ')			
	
print()
print(f'running time : {time.time() - start_time}sec')