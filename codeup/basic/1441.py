n = int(input())
a = []

for _ in range(n):
  a.append(int(input()))

# bubble sort, SC = O(1), TC = O(N^2) -> O(N)
# method common
'''
for i in range(len(a) - 1, 0, -1):
  for j in range(i):
    if a[j] > a[j + 1]:
      a[j], a[j + 1] = a[j + 1], a[j]
'''

# method optimize
'''
end = len(a) - 1
while end > 0:
  last_swap = 0
  for i in range(end):
    if a[i] > a[i + 1]:
      a[i], a[i + 1] = a[i + 1], a[i]
      last_swap = i

  end = last_swap
'''

# python function
a.sort()

for number in a:
  print(number)