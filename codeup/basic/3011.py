# bubble sort
def bubble_sort(array):
  end = len(array) - 1
  step = 0
  while end > 0:
    last_swap = 0
    step += 1
    for i in range(end):
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        last_swap = i

    end = last_swap
  
  step -= 1
  if step == 0:
    step = 1

  return step

n = int(input())
numbers = list(map(int, input().split()))
print(bubble_sort(numbers))
