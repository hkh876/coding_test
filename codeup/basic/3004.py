# binary_search
def binary_search(target, array):
  start = 0
  end = len(array) - 1

  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1

  return None

n = int(input())
numbers = list(map(int, input().split()))
sorted_list = sorted(numbers)

for number in numbers:
  index = binary_search(number, sorted_list)
  print(index, end=' ')
  