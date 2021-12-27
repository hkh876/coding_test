# required double array
n, g = map(int, input().split())
number_array = list(map(int, input().split()))
result = [number_array[i * g:(i + 1) * g] for i in range((len(number_array) - 1 + g) // g)]

for numbers in result:
  print(min(numbers), end=' ')
