a,b,c = map(int, input().split())
result_sum = a + b + c
result_div = round(result_sum/3, 2)
print(f'{result_sum} {result_div:.2f}')