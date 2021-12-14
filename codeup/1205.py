# required if ~ else
a,b = map(float, input().split())
operators = ['+', '-', '*', '/', '**']
array = []

for operator in operators:
  if operator == '+':
    array.append(a + b)
  elif operator == '-':
    array.append(a - b)
    array.append(b - a)
  elif operator == '*':
    array.append(a * b)
  elif operator == '/':
    if a != 0 and b != 0:
      array.append(a / b)
      array.append(b / a)
  elif operator == '**':
      array.append(a ** b)
      array.append(b ** a)

max_value = max(array)
print(f'{max_value:.6f}')
