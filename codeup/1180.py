# required if ~ else
n_str = input().zfill(2)
swap_str = n_str[1] + n_str[0]
number = int(swap_str)
result = number * 2

if result >= 100:
  result %= 100

print(result)
if result <= 50:
  print('GOOD')
else:
  print('OH MY GOD')
