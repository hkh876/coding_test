# required if ~ else
number = list(map(int, input().split()))

for i in range(3):
  min_index = i
  for j in range(i + 1, 3):
    if number[min_index] > number[j]:
      min_index = j

  number[i], number[min_index] = number[min_index], number[i]

print(number[1])