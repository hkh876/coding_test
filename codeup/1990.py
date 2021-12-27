# required string
n = input()

total = 0
for i in range(len(n)):
  total += int(n[i])

if total % 3 == 0:
  print(1)
else:
  print(0)
