# required if ~ else
lotto_numbers = list(map(int, input().split()))
number_list = list(map(int, input().split()))

bonus = lotto_numbers.pop()
result = [0, 0, 0, 5, 4, 3, 1, 2]
count = 0

for number in number_list:
  if number in lotto_numbers:
    count += 1

if count == 5:
  if bonus in number_list:
     count = 7

print(result[count])