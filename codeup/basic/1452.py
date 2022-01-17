# quick sort
def quick_sort(array):
  if len(array) <= 1:
    return array

  pivot = array[len(array) // 2]
  low_array, equal_array, high_array = [], [], []
  for number in array:
    if number < pivot:
      low_array.append(number)
    elif number > pivot:
      high_array.append(number)
    else:
      equal_array.append(number)

  return quick_sort(low_array) + equal_array + quick_sort(high_array)
  
n = int(input())
a = []

for _ in range(n):
  a.append(int(input()))

sorted_array = quick_sort(a)

# python function
#a.sort()

for number in sorted_array:
  print(number)