# required for
def eratosthenes_algorithm(x):
  a = [False, False] + [True] * (x - 1)
  primes = []

  for i in range(2, x + 1):
    if a[i]:
      primes.append(i)
      for j in range(2 * i, x + 1, i):
        a[j] = False

  return primes

n = int(input())
number_list = eratosthenes_algorithm(n)
result = False

for number in number_list:
  value = n / number
  if value in number_list:
    print(f'{number} {int(value)}')
    result = True
    break
    
if not result:
  print('wrong number')