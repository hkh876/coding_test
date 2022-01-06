# required string
a, b = input().split()

if len(a) > len(b):
  a, b = b, a
elif len(a) == len(b):
  for i in range(len(a)):
    if a[i] != b[i]:
      if a[i] > b[i]:
        a, b = b, a
      break

print(f'{a} {b}')