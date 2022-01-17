n = int(input())
a = []

for _ in range(n):
  a.append(int(input()))

# insertion sort, SC = O(1), TC = O(N^2) -> O(N)
# method common
'''
for end in range(1, len(a)):
  for i in range(end, 0, -1):
    if a[i - 1] > a[i]:
      a[i - 1], a[i] = a[i], a[i - 1]
'''

# method optimize
'''
for end in range(1, len(a)):
  to_insert = a[end]
  i = end
  while i > 0 and a[i - 1] > to_insert:
    a[i] = a[i - 1]
    i -= 1

  a[i] = to_insert
'''

# python function
a.sort()

for number in a:
  print(number)